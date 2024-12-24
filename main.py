#!/usr/bin/env python3
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/")
async def root(request: Request):
    body = await request.json()
    print("Received request body:", body)
    return JSONResponse(
        content={"message": "Request received successfully"}, status_code=200
    )


@app.get("/")
async def root(request: Request):
    return JSONResponse(content={"message": "get successfully"}, status_code=200)
