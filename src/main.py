from fastapi import FastAPI, Request
import time
import requestvars

app = FastAPI()

user = None

# adiciona tempo de resposta no header


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


# injeta um user "global" na request pelo middleware que pode ser consumido no filho
@app.middleware("http")
async def get_user_by_token(request: Request, call_next):
    requestvars.user.set({"name": "Aguinelo"})
    return await call_next(request)


@app.get('/')
async def main(request: Request):
    return {'message': 'hello', "user": requestvars.request_user()}
