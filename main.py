#!/usr/bin/env python3
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json
import requests

app = FastAPI()


@app.post("/")
async def root(request: Request):
    body = await request.json()
    requests.get("https://api.day.app/JbPripgUKKNzbELvwURvrD/{body}")

    return JSONResponse(
        content={"message": "Request received successfully"}, status_code=200
    )


@app.get("/")
async def root(request: Request):
    data = request.query_params
    if "hub.mode" in data:
        if (
            data["hub.mode"] != "subscribe"
            or data["hub.verify_token"] != "STRAVA_KJGONG"
        ):
            return "Invalid request", 401

        return JSONResponse(
            content={"hub.challenge": data["hub.challenge"]}, status_code=200
        )
