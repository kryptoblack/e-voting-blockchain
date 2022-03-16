from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from src.models.candidate_model import Candidate, AddCandidatePostModel, CastVotePostModel
from src.models.response_model import SuccessResponse, ErrorResponse

from src.dependencies import Web3Client

from typing import List

import pprint


router = APIRouter()

@router.get("", response_model=List[Candidate])
def get_candidate(account: str, w3_client: Web3Client = Depends(Web3Client.get_client)):
    '''Used to get all candidates'''
    try:
        result = list()

        for i in range(w3_client.get_candidate_count()):
            # w3_client.get_candidate(i) -> list(account, name, party, vote, winner)
            if account == w3_client.get_candidate(i)[0]:
                data = w3_client.get_candidate(i)
                
                result.append(Candidate(
                    candidate_id=i,
                    name=data[1],
                    party=data[2],
                    votes=data[3],
                ).dict())

        return JSONResponse(content=result, status_code=status.HTTP_200_OK)
    except Exception as e:
        return JSONResponse(content=ErrorResponse(code="internal-server-error", message="Internal Server Error", detail="Something went wrong").dict(), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.post("", response_model=SuccessResponse)
def add_candidate(body: AddCandidatePostModel, w3_client: Web3Client = Depends(Web3Client.get_client)):
    '''Used to add candidates'''
    try:
        assert w3_client.add_candidate(body.name, body.party, body.account)

        return JSONResponse(content=SuccessResponse(code="success", message="Successful").dict(), status_code=status.HTTP_200_OK)
    except Exception as e:
        return JSONResponse(content=ErrorResponse(code="internal-server-error", message="Internal Server Error", detail="Something went wrong").dict(), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.post("/caste-vote", response_model=SuccessResponse)
def caste_vote(body: CastVotePostModel, w3_client: Web3Client = Depends(Web3Client.get_client)):
    '''Used to caste vote'''
    try:
        assert w3_client.caste_vote(body.candidate_id, body.name, body.party, body.account)

        return JSONResponse(content=SuccessResponse(code="success", message="Successful").dict(), status_code=status.HTTP_200_OK)
    except Exception as e:
        return JSONResponse(content=ErrorResponse(code="internal-server-error", message="Internal Server Error", detail="Something went wrong").dict(), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@router.get("/winner", response_model=Candidate)
def get_winner(account: str, w3_client: Web3Client = Depends(Web3Client.get_client)):
    '''Used to get the winner'''
    try:
        winners = w3_client.get_winner(account)
        
        if len(winners) == 0:
            return JSONResponse(content=ErrorResponse(code="no-winner", message="Bad Data", detail="No winner found").dict(), status_code=status.HTTP_400_BAD_REQUEST)
        
        if len(winners) > 1:
            return JSONResponse(content=ErrorResponse(code="multiple-winners", message="Multiple Winner", detail="Multiple winners found").dict(), status_code=status.HTTP_400_BAD_REQUEST)

        winner = winners[0]

        return JSONResponse(content=Candidate(candidate_id=winner[4], name=winner[1], party=winner[2], votes=winner[3]).dict(), status_code=status.HTTP_200_OK)
    except Exception as e:
        return JSONResponse(content=ErrorResponse(code="internal-server-error", message="Internal Server Error", detail="Something went wrong").dict(), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)



