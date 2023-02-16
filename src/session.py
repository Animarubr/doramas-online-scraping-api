import httpx
from httpx import Request

class Session:
    
    def __init__(self):
        self.client = httpx.Client()
    
    def make_request(self, url:str) -> Request:
        
        with self.client as client:
            r = client.get(url)
        return r.content
