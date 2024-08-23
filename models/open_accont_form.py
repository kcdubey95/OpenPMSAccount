from datetime import datetime,date

from pydantic import BaseModel, Field


class Mobile(BaseModel):
    mobile: int


class Step_One(BaseModel):
    fname: str
    lname: str
    email: str


class Step_Tow(BaseModel):
    fullname: str
    dob: str
    gender: int
    address: str
    occupation: int


class Step_Three(BaseModel):
    nfull_name: str
    dob: datetime
    address: str
    Occupation: str



