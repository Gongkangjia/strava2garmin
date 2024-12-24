#!/usr/bin/env python3
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def print_request(request: Request):
    body = await request.json()
    print("Received request body:", body)
    return JSONResponse(
        content={"message": "Request received successfully"}, status_code=200
    )
