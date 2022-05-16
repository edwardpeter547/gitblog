from passlib.context import CryptContext

class Hash():
    
    @classmethod
    def encrypt(cls, plain_password: str):
        pwd_context = CryptContext(schemes=['bcrypt'], deprecated = 'auto')
        return pwd_context.hash(plain_password)
    
    
    @classmethod
    def verify(cls, plain_password, hashed_password):
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")
        return pwd_context.verify(plain_password, hashed_password)
        