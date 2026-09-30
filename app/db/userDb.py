from app.db.connectDb import userDB
from bson import ObjectId

from secrets import token_hex


def create_user(phone: str):
    user_collection = userDB["Users"]
    res = user_collection.insert_one({"phone_no": phone, "_id": str(ObjectId())})
    print(res)

    if res.acknowledged:
        return res.inserted_id
    else:
        return None


def read_user(phone: str):
    user_collection = userDB["Users"]
    res = user_collection.find_one({"phone_no": phone}, {"_id": 0})

    if not res:
        return

    token = str(token_hex(8))

    tokenRes = user_collection.update_one(
        {"phone_no": phone}, {"$set": {"token": token}}
    )

    if tokenRes.acknowledged == False:
        return

    res["token"] = token

    return res


def validateUser(token: str, phone: str):
    user_collection = userDB["Users"]

    print(phone, token)

    res = user_collection.find_one({"phone_no": phone, "token": token})
    print(res)

    if not res:
        return False

    return True


def create_profile_db(data: dict):
    user_collection = userDB["Users"]
    res = user_collection.update_one({"phone_no": data["phone"]}, {"$set": data})

    if not res.acknowledged:
        return

    return res.acknowledged


def update_profile_db(data: dict):
    user_collection = userDB["Users"]
    res = user_collection.update_one({"phone_no": data["phone"]}, {"$set": data})

    if not res.acknowledged:
        return

    return res.acknowledged


def delete_profile_db(phone: str):
    user_collection = userDB["Users"]
    res = user_collection.delete_one({"phone_no": phone})

    if not res.acknowledged:
        return

    return res.acknowledged


def update_dp_db(data: dict, phone: str):
    user_collection = userDB["Users"]
    res = user_collection.update_one({"phone_no": phone}, {"$set": data})

    if not res.acknowledged:
        return

    return res.acknowledged


def read_profile_db(phone: str | None = None):
    user_collection = userDB["Users"]

    if not phone:
        res = user_collection.find({}, {"_id": 0, "token": 0})

        if not res:
            return

        return list(res)
    else:
        res = user_collection.find({"phone_no": phone}, {"_id": 0, "token": 0})

        if not res:
            return

        return list(res)
