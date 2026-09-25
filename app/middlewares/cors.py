from fastapi.middleware.cors import CORSMiddleware


def include_cors_middleware(app):
    app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])
