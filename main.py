from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import requests
from urllib.parse import urlencode


app = FastAPI()


@app.get('/')
def root(url: str, request: Request):
    try:
        params = dict(request.query_params)
        del params['url']
        headers = dict(request.headers)
        del headers['host']
        if params.get('host'):
            headers['host'] = params.get('host')
        del headers['accept-encoding']
        headers['accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        cookies = dict(request.cookies)
        if len(params) > 0:
            url += f'?{urlencode(params)}'
        return str(requests.get(url, headers=headers, cookies=cookies, timeout=5).text)
    except:
        return 'Request failed!'
