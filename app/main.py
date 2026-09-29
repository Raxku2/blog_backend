from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.middlewares.cors import include_cors_middleware

from app.routes.authRouter import router as AuthRouter
from app.routes.imagekitRouter import router as ImagekitRouter
from app.routes.postRoute import router as PostRouter
from app.routes.profileRouter import router as ProfileRouter
from app.routes.otpRouter import router as OTPRouter

from app.db.connectDb import test_db

app = FastAPI(title="Blog app API", version="0.1")

include_cors_middleware(app)


app.include_router(AuthRouter)
app.include_router(ImagekitRouter)
app.include_router(PostRouter)
app.include_router(ProfileRouter)
app.include_router(OTPRouter)


@app.get("/")
def root():
    return JSONResponse({"message": "ok"})


@app.get("/health")
def check_health():
    db_status = test_db()
    return JSONResponse(
        {"message": "API is running", "status": "ok", "db_status": db_status}
    )
