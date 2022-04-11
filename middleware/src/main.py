from typing import Optional

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from src.controllers.candidate_controller import router as candidate_router

from src.models.response_model import get_formatted_response, ErrorResponse

from src.dependencies import Web3Client


app = FastAPI(
    title="E-Voting-Middleware",
    description="Middlware is the software that sits between the user and the blockchain. It is used to verify the authenticity of the user and to ensure that the user is authorized to vote. The middleware is used to make it easier for the developer of the application to integrate with the blockchain without having any knowledge of the blockchain.",
    version="0.0.1",
)

# * Change for deployment
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    candidate_router, 
    prefix="/candidate", 
    tags=["Candidate"],
    # dependencies=[Depends(Web3Client.get_client)],
    responses={
        500: get_formatted_response(ErrorResponse(code="internal-server-error", message="Internal Server Error", detail="Something went wrong")),
    }
)