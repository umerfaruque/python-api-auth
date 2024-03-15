from fastapi import FastAPI
from routers import mainapi, authapi

app = FastAPI()
# Mount routers
app.include_router(authapi.router)
app.include_router(mainapi.router)

if __name__ == "__main__":
    import uvicorn
    # uvicorn.run(app, host="0.0.0.0", port=8001)
    uvicorn.run(app, host="localhost", port=8001)