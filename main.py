from fastapi import FastAPI,HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse  
from fastapi.middleware.cors import CORSMiddleware
import sympy
from sympy import *
import requests 


app = FastAPI()

NUMBERS_API_URL = "http://numbersapi.com"


# Custom error handler for invalid inputs
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    number_str = request.query_params.get('number')
    return JSONResponse(
        status_code=400,
        content={"number": number_str, "error": True}
    )

@app.get ("/api/classify-number")

def mth_num(number:int):
    
          
    response = requests.get(f"{NUMBERS_API_URL}/{number}/math?json")
    data = response.json() if response.status_code == 200 else {"error": "Could not fetch fact"}
    text = data.get('text', 'No text key found')

    
    is_prime = sympy.isprime(number)

    is_perfect = sympy.is_perfect(number)


    num_str=str(abs(number))
    num_list = list(map(int,num_str))
    digit_sum= sum(num_list)


    # # Armstrong
    n= len(num_list)
    new_list= []
    property = []
    for i in num_list:
        x = i**n
        new_list.append(x)
    numbers = abs(number)
    if (sum(new_list)== numbers) & (numbers % 2 == 0):
        property = ["armstrong","even"]
    elif (sum(new_list)== numbers) & (numbers % 2 != 0):
        property = ["armstrong","odd"]
    elif (sum(new_list)!= numbers) & (numbers % 2 == 0):
        property = ["even"]
    elif (sum(new_list)!= numbers) & (numbers % 2 != 0):
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