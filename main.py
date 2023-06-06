import requests
from fastapi import FastAPI
import uvicorn
import json
import os, binascii

app = FastAPI()


def get_joke():
    joke_list = {"id" : "",
                 "value": ""}
    response = requests.get('https://api.chucknorris.io/jokes/random')
    response = response.json()
    joke_list = {"id": response['id'],
                 "joke": response['value']}
    return joke_list


@app.get("/hello")
@app.get("/hello/")
def start():
    for_json = {'id': str(binascii.b2a_hex(os.urandom(15)).decode('utf8')),
                'value': 'Hello, world!'}
    return json.dumps(for_json)


@app.get("/health/readiness")
@app.get("/health/liveness")
def status():
    return json.dumps({"status": "UP"})


@app.get("/joke")
def joke():
    fun_name = get_joke()
    return json.dumps(fun_name)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8091)
