from pydantic import BaseModel
from typing import Union,Optional,List

class Developer(BaseModel):
    name: str
    experience: Optional[int] = None


class Projects(BaseModel):
    title: str
    description: Optional[str] = None
    language: Optional[List[str]] = None
    lead_developer: Developer


#constrants jan do kufizime qe munesh mjau ba data typeve si p.sh conint per integer constr per string
#api ur komunikuese,lidhse mes dy komponentave p.sh client dhe server
#identation eshte hapsira qe shtohet para rreshtit me kallxu qe o ne te njejten klas, funksion etj
#200 response eshte ne rregull
#400 client crash
#500 server crash