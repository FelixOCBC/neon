from cgitb import text
from sqlite3 import Timestamp
from time import time
from pydantic import BaseModel
from typing import Optional, List


class RequestCIF(BaseModel):
    cif: str = None


class CIF(BaseModel):
    loanid: str = None
    loan_type: int = None
    loan_amount: int = None
    loan_tenure: int = None
    interest: int = None
    cif: str  = None
    idno: int = None
    fname: str = None
    lname: str = None
    dob: Timestamp = None
    gender: str = None
    marital_status: str = None
    income: int = None
    phone: str = None
    email: str = None
    isphoneverified: int = None
    isemailverified: int = None
    createdate: Timestamp = None
    updatedate: Timestamp = None
    source: str = None


    #tambahin sisa kolom


class ResponseCIF(BaseModel):
    cif_list: List[CIF]