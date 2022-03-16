from typing import Optional

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from src.controllers.candidate_controller import router as candidate_router

from src.models.response_model import get_formatted_response, ErrorResponse

from src.dependencies import Web3Client


app = FastAPI(
    title="E-Voting-Middleware",
    description="Blockchain middleware is used to apply blockchain to use cases in industries that are not well served by existing blockchain technologies. Here it is used as a bridge between the blockchain and the industry.",
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