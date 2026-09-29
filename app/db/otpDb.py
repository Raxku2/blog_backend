from app.db.connectDb import authDB
from datetime import datetime, timedelta


def saveOtp(phone_no: str, otp: str):

    coll = authDB["otp_collection"]

    res = coll.insert_one({"phone_no": phone_no, "otp": otp, "date": datetime.now()})
    print(res)
    if res.acknowledged:
        return res.acknowledged
    else:
        return False


def validateOtp(phone_no: str, otp: str):
    coll = authDB["otp_collection"]
    res = coll.find_one({"phone_no": phone_no, "otp": otp})

    if not res:
        return False

    five_min_ago = datetime.now() - timedelta(minutes=5)
    print(five_min_ago)
    print(res["date"])

    if five_min_ago >= res["date"]:
        return False

    res = coll.delete_one({"phone_no": phone_no, "otp": otp})

    if res.deleted_count:
        return True
    else:
        return False
