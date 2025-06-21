# Create an API endpoint using the FastAPI framework that accepts a JSON payload in a POST request

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
app = FastAPI()
class Payload(BaseModel):
    data: Dict[str, Any]
@app.post("/process")
async def process_payload(payload: Payload):
    try:
        # Simulate processing the payload
        processed_data = {k: v for k, v in payload.data.items() if isinstance(v, (int, float))}
        return {"status": "success", "processed_data": processed_data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
@app.get("/")
async def read_root():
    return {"message": "Welcome to the API. Use POST /process to send data."}
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
@app.get("/info")
async def info():
    return {
        "name": "Intermediate API",
        "version": "1.0.0",
        "description": "An API to process JSON payloads."
    }
@app.get("/docs")
async def get_docs():
    return {
        "message": "API documentation is available at /docs",
        "documentation_url": "/docs"
    }
@app.get("/openapi.json")
async def get_openapi():
    return {
        "message": "OpenAPI schema is available at /openapi.json",
        "schema_url": "/openapi.json"
    }