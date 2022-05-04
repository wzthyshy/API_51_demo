"""
dafault模块的关键字封装
"""
import os

from api_service.user_jwt_controller import UserController, us


def login_user(username, password, rememberMe):

    payload = {

        "username": username,
        "password": password,
        "rememberMe": rememberMe
    }
    header = {
        "Content-Type": "application/json"

    }
    res = us.login(data=payload, headers=header)

    print(res)





