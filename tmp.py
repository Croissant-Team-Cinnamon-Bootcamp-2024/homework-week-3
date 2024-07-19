from fastapi import FastAPI

app = FastAPI()

@app.get('/greeting/{name}')
async def hello(name:str):
    return {'message': f'Hello, {name}!'}