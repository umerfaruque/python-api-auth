from fastapi import FastAPI
from routers import mainapi, authapi

app = FastAPI()
# Mount routers
app.include_router(authapi.router)
app.include_router(mainapi.router)