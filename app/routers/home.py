from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.responses import JSONResponse

home = APIRouter()

@home.get("/regional-sports")
async def regional_sports():
    return "test"
