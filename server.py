#!/usr/bin/env python

import asyncio
import websockets
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello this is the new version!"

@asyncio.coroutine
def hello():
    websocket = yield from websockets.connect('ws://localhost:8765/')

    try:
        name = input("What's your name? ")
        yield from websocket.send(name)
        print("> {}".format(name))

        greeting = yield from websocket.recv()
        print("< {}".format(greeting))

    finally:
        yield from websocket.close()

asyncio.get_event_loop().run_until_complete(hello())
index()