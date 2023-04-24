from fastapi import FastAPI
from fastapi import HTTPException, status
from server.models import *
from server.database import User
from server.serializer import userListEntity,userEntity
from random import randint
from pymongo.collection import ReturnDocument

app = FastAPI()

@app.get("/", response_model=ListUserResponse, tags=["Root"])
def get_all():
    pipeline = [
        {'$match': {}}]
    result = userListEntity(User.aggregate(pipeline))
    return {'status': 'success', 'results': len(result), 'users': result}

@app.get("/user/{email}", response_model=UserResponse)
def get_user(email):
    user = User.find_one({'email': email})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Usuário {email} não encontrado.")
    return {"status": "success", "user": userEntity(user)}


@app.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(payload: UserBaseSchema):
    payload.created_at = datetime.utcnow()
    payload.updated_at = payload.created_at
    payload.sub_number = str(str(randint(1000, 9999)) + str(payload.document))
    try:
        result = User.insert_one(payload.dict(exclude_none=True))
        new_user = User.find_one({'_id': result.inserted_id})
        return {"status": "success", "user": userEntity(new_user)}
    except:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"E-mail {payload.email} já existe!")
    

@app.patch('/user/{email}', response_model=UserResponse)
def update_user(email: str, payload: UpdateUserSchema):
    if not email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"E-mail inválido: {email}.")
    updated_user = User.find_one_and_update(
        {'email': str(email)}, {'$set': payload.dict(exclude_none=True)}, return_document=ReturnDocument.AFTER)
    if not updated_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Usuário {email} não encontrado.')
    return {"status": "success", "user": userEntity(updated_user)}


@app.delete('/user/{email}')
def delete_note(email: str):
    if not email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"E-mail inválido: {email}.")
    user = User.find_one_and_delete({'email': email})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Usuário {email} não encontrado.')
    return {"status": "success", "msg": "Deletado com sucesso."}

