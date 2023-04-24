def userEntity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "sub_number": str(user["sub_number"]),
        "name": user["name"],
        "email": user["email"],
        "password": user["password"],
        "birthday": user["birthday"],
        "region": user["region"],
        "termconditions": user["termconditions"],
        "document": user["document"],
        "photo": user["photo"],
        "video": user["video"],
        "created_at": user["created_at"],
        "updated_at": user["updated_at"]
    }


def userListEntity(users) -> list:
    return [userEntity(user) for user in users]
