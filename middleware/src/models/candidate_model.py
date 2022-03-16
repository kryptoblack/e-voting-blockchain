from typing import Optional

from pydantic import BaseModel


class Candidate(BaseModel):
    candidate_id: int
    name: str
    party: str
    votes: int
    
    class Config:
        schema_extra = {
            "example": {
                "candidate_id": 1,
                "name": "Ritesh",
                "party": "BJP",
                "votes": 10,
            }
        }


class AddCandidatePostModel(BaseModel):
    name: str
    party: str
    account: str
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Ritesh",
                "party": "BJP",
                "account": "0x0"
            }
        }


class CastVotePostModel(BaseModel):
    candidate_id: int
    name: str
    party: str
    account: str
    
    class Config:
        schema_extra = {
            "example": {
                "candidate_id": 2,
                "name": "Pat",
                "party": "The Greens",
                "account": "0x0"
            }
        }