from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from .schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return Message(message='Hello World')


@app.get('/home', status_code=HTTPStatus.OK)
def read_home():
    return HTMLResponse(
        content="""
    <html>
        <head>
            <title>Home</title>
        </head>
        <body>
            <p>Ola mundo!</p>
        </body>
    </html>
    """
    )
