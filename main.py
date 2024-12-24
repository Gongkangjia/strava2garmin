#!/usr/bin/env python3
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json
import requests

from stravaweblib import WebClient, DataFormat
from stravalib.client import Client


client_id = "143364"
client_secret = "881bd288ff7d2c0e0291c6ab73c4998d2dbfadea"
refresh_token = "791c1275cece1e6f0e0ef21fb3625f53d7364fe3"
strava_email = "gongkangjia@gmail.com"
strava_password = "Gg801300"


def upload(activity_id):

    client = Client()
    refresh_response = client.refresh_access_token(
        client_id=client_id, client_secret=client_secret, refresh_token=refresh_token
    )
    client.access_token = refresh_response["access_token"]

    strava_web_client = WebClient(
        access_token=strava_client.access_token,
        email=strava_email,
        password=strava_password,
    )
    data = strava_web_client.get_activity_data(activity_id, fmt=DataFormat.ORIGINAL)

    garth.configure(domain="garmin.cn")
    garth.login("gongkangjia@qq.com", "Gg801300")
    garth.save(".garth")

    res = requests.post(
        f"https://connectapi.{garth.client.domain}/upload-service/upload",
        files={"file": (data.filename, data.content)},
        headers={"authorization": str(garth.client.oauth2_token)},
    )

    return res


app = FastAPI()


@app.post("/")
def root(request: Request):
    data = request.json()
    requests.get(f"https://api.day.app/JbPripgUKKNzbELvwURvrD/{data}")

    if (
        data["object_type"] == "activity"
        and data["owner_id"] == 67158138
        and data["subscription_id"] == 270657
    ):
        # 开始处理
        if data["aspect_type"] == "create":
            try:
                upload(data["object_id"])
                requests.get(
                    f"https://api.day.app/JbPripgUKKNzbELvwURvrD/上传成功=>{data["object_id"]}"
                )

                return JSONResponse(
                    content={"message": "Request received successfully"},
                    status_code=200,
                )
            except Exception as e:
                return JSONResponse(
                    content={"message": "上传失败!"},
                    status_code=500,
                )


@app.get("/")
def root(request: Request):
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
