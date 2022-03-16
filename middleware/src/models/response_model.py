from typing import Optional

from pydantic import BaseModel


def get_formatted_response(klass) -> dict:
    return {
            'model': type(klass),
            'description': 'Incorrect username and password',
            'content': {
                'application/json': {
                    'example': klass.dict()
                }
            }
        }

class ErrorResponse(BaseModel):
    code: str
    message: str
    detail: str
    
    class Config:
        schema_extra = {
            "example": {
                "code": "auth-0001",
                "message": "Incorrect username and password",
                "detail": "Ensure that the username and password included in the request are correct"
            }
        }



class SuccessResponse(BaseModel):
    code: str
    message: str
    
    class Config:
        schema_extra = {
            "example": {
                "code": "success",
                "message": "Successfully logged in"
            }
        }
