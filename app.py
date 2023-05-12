#!/usr/bin/python3
import urllib

import requests

# url = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json"
url = "https://httpbin.org/post"


def checkHTTP(response_code):
    if 400 <= response_code < 600:
        raise Exception("error")


def HTTP_GET(url_link):
    r = requests.get(url_link)
    checkHTTP(r.status_code)
    return r.json()


def HTTP_POST(url_link):
    body = {"name": "natalia"}
    request = requests.post(url_link, json=body)
    checkHTTP(request.status_code)
    return request.json()


if __name__ == '__main__':
    print(HTTP_POST("https://httpbin.org/post"))
