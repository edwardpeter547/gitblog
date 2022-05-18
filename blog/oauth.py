from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from . import jwtoken


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')

def get_current_user(data: str = Depends(oauth2_scheme)):
    exception_credentials = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail= f"could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"})
    
    return jwtoken.verify_jwt_token(token=data, httpcredential_exception=exception_credentials)
    