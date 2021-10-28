from fastapi import FastAPI, Depends, HTTPException
from auth import AuthHandler
from schemas import LogInDetails, SignUpDetails


app = FastAPI()


auth_handler = AuthHandler()
users = []


@app.post('/register', status_code=201)
def register(auth_details: SignUpDetails):
    if any(x['email'] == auth_details.email for x in users):
        raise HTTPException(status_code=400, detail='email is taken')
    hashed_password = auth_handler.get_password_hash(auth_details.password)
    users.append({
        'email': auth_details.email,
        'password': hashed_password,
        'name': auth_details.name
    })
    return {"user created successfully"}


@app.post('/login')
def login(auth_details: LogInDetails):
    user = None
    for x in users:
        if x['email'] == auth_details.email:
            user = x
            break

    if (user is None) or (not auth_handler.verify_password(auth_details.password, user['password'])):
        raise HTTPException(
            status_code=401, detail='Invalid email and/or password')
    token = auth_handler.encode_token(user['email'])
    return {'token': token}


@app.get('/unprotected')
def unprotected():
    return {'hello': 'world'}


@app.post('/protected')
def protected(email=Depends(auth_handler.auth_wrapper)):
    return {'name': email}
