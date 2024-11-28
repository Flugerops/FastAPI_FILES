from uvicorn import run as run_asgi


if __name__ == "__main__":
    run_asgi("app:app", reload=True)
