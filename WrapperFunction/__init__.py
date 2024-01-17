import azure.functions as func
import asyncio
import fastapi
import random.random as rand
from fastapi import WebSocket
import json


app = fastapi.FastAPI()


@app.post("/sample")
def main(req: func.HttpRequest) -> func.HttpResponse:
    
    # Set the content type to text/event-stream
    headers = {
        'Content-Type': 'text/event-stream',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive'
    }

    # Send the headers to the client
    response = func.HttpResponse(headers=headers)

    # Send the response to the client in real-time using SSE
    response.streaming = True

    # Send the initial SSE event to the client
    response.write('event: message\n')

    # Send the SSE events to the client
    i: int = 0
    while True:
        payload = {'random': rand()}
        i += 1
        if i > 1000:
            break

    # Send the final SSE event to the client
    response.write('event: message\n')
    response.write('data: {}\n\n'.format(json.dumps(payload)))

    return response

# async def index():
#     await websocket.accept()
#     i: int = 0
#     while True:
#         await asyncio.sleep(0.5)
#         payload = {'random': rand()}
#         await websocket.send_json(payload)
#         i += 1
#         if i > 1000:
#             break

@app.get("/hello/{name}")
async def get_name(name: str):
    return {
        "name": name,
    }
