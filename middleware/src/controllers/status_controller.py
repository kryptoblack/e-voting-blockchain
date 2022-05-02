from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from src.models.candidate_model import Candidate, AddCandidatePostModel, CastVotePostModel
from src.models.response_model import SuccessResponse, ErrorResponse


router = APIRouter()

@router.get("", response_model=SuccessResponse)
def get_status():
    '''Used to check status of the server'''
    try:
        return JSONResponse(content=SuccessResponse(message="Server is working fine!").dict(), status_code=status.HTTP_200_OK)
    except Exception as e:
        return JSONResponse(content=ErrorResponse(code="internal-server-error", message="Internal Server Error", detail="Something went wrong").dict(), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

