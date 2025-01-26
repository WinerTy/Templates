from core import settings

from api.router import router as api_router


from create_app import create_application


app = create_application()
app.include_router(api_router, prefix=settings.api.prefix)


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=settings.server.host,
        port=settings.server.port,
        reload=True,
    )
