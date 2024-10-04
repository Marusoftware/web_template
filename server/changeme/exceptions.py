from pydantic.dataclasses import dataclass

@dataclass
class APIError(Exception):
    status_code:int =400
    detail:str ="Something Wrong"

@dataclass
class Forbidden(APIError):
    status_code:int =401
    detail:str ="Not authenticated"

@dataclass
class NotFound(APIError):
    status_code:int =404
    detail:str ="Not found"