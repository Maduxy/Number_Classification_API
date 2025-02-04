from fastapi import FastAPI,HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse  
from fastapi.middleware.cors import CORSMiddleware
import sympy
from sympy import *
import requests 


app = FastAPI()

NUMBERS_API_URL = "http://numbersapi.com"


@app.get ("/api/classify-number")

def mth_num(number:int):

    if number < 0:
        # raise HTTPException(status_code=400, detail="Number must be a positive integer.")
        return JSONResponse(
        status_code=400,
        content={"number": "alphabet","error": "true"},
        )
    
          
    response = requests.get(f"{NUMBERS_API_URL}/{number}/math?json")
    data = response.json() if response.status_code == 200 else {"error": "Could not fetch fact"}
    text = f"{data.get('text', 'No text key found')} //gotten from the numbers API"

    
    is_prime = sympy.isprime(number)

    is_perfect = sympy.is_perfect(number)

    
    num_str=str(number)
    num_list = list(map(int,num_str))
    digit_sum= sum(num_list)
    

    # # Armstrong
    n= len(num_list)
    new_list= []
    property = []
    for i in num_list:
        x = i**n
        new_list.append(x)

    if (sum(new_list)== number) & (number % 2 == 0):
        property = ["Armstrong","even"]
    elif (sum(new_list)== number) & (number % 2 != 0):
        property = ["Armstrong","odd"]
    elif (sum(new_list)!= number) & (number % 2 == 0):
        property = ["even"]
    elif (sum(new_list)!= number) & (number % 2 != 0):
        property = ["odd"]

    return { "number": number,
        "is_prime": is_prime,
        "is_perfect": is_perfect,
        "properties": property,
        "digit_sum": digit_sum, 
        "fun_fact": text }


# Adding CORS Handling
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)