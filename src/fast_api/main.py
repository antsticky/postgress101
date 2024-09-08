import requests

import uvicorn

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2AuthorizationCodeBearer

from jwt import PyJWKClient
import jwt
from typing import Annotated

app = FastAPI()

oauth_2_scheme = OAuth2AuthorizationCodeBearer(
    tokenUrl="http://localhost:7080/realms/MyRealm/protocol/openid-connect/token",
    authorizationUrl="http://localhost:7080/realms/MyRealm/protocol/openid-connect/auth",
    refreshUrl="http://localhost:7080/realms/MyRealm/protocol/openid-connect/token",
)

async def valid_access_token(
    access_token: Annotated[str, Depends(oauth_2_scheme)]
):
    try:
        # login: http://localhost:7080/realms/MyRealm/account
        # https://keycloak.discourse.group/t/issue-on-userinfo-endpoint-at-keycloak-20/18461/2
        # https://saurav-samantray.medium.com/securing-rest-api-with-role-based-access-control-rbac-using-keycloak-part-i-nodejs-8f59be925a42
        headers = {'Authorization': 'bearer ' + access_token}
        r_user = requests.get(
            'http://localhost:7080/realms/MyRealm/protocol/openid-connect/userinfo',
            headers=headers,
            verify=True
        )
        
        if r_user.status_code != 200:
            raise jwt.exceptions.InvalidTokenError("Invalid token")
        
        json_data = r_user.json()
        return json_data
        
    except jwt.exceptions.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Not authenticated")


@app.get("/public")
def get_public():
    return {"message": "Most látsz"}


@app.get("/private", dependencies=[Depends(valid_access_token)])
def get_private():
    return {"message": "Már megint látsz"}

def main():
    uvicorn.run("fast_api.main:app", host="0.0.0.0", port=8000, reload=True)