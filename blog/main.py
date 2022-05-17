from fastapi import FastAPI
from . import models
from . routes import blog, user, category, authentication


app = FastAPI()

models.Base.metadata.create_all(models.engine)
        
# Todo: application parts route definition
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(category.router)
app.include_router(authentication.router)

    





