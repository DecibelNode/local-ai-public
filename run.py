from fastapi import FastAPI as fah
from fastapi import security, HTTPException
import requests as rs 
import functions.detectinterface as di 

server = fah()

if di.process("ollama"):
    @server.get("/v1")
    async def ollama_api():
        OLLAMA_URL = "http://127.0.0.1:11434"
        
