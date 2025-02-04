from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import sympy
import requests

app = FastAPI()

NUMBERS_API_URL = "http://numbersapi.com"

# Adding CORS Handling
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/classify-number")
async def classify_number(request: Request):
    number_str = request.query_params.get('number')

# Validate the input
    if not number_str:
        # No number provided
        return JSONResponse(
            status_code=400,
            content={"number": None, "error": True},
        )

    try:
        number = int(number_str)
    except ValueError:
        # Input is not an integer
        return JSONResponse(
            status_code=400,
            content={"number": number_str, "error": True},
        )

    if number < 0:
        # Negative number provided
        return JSONResponse(
            status_code=400,
            content={"number": number, "error": True},
        )

    # Now process the valid positive integer
    is_prime = sympy.isprime(number)
    is_perfect = sympy.is_perfect(number)
    digit_sum = sum(int(digit) for digit in str(number))

    # Check if the number is an Armstrong number
    num_digits = len(str(number))
    sum_of_powers = sum(int(digit) ** num_digits for digit in str(number))
    is_armstrong = sum_of_powers == number

    # Determine properties
    if is_armstrong:
        properties = ["armstrong", "even" if number % 2 == 0 else "odd"]
    else:
        properties = ["even" if number % 2 == 0 else "odd"]


    # Fetch a fun fact from Numbers API
    response = requests.get(f"{NUMBERS_API_URL}/{number}/math?json")
    if response.status_code == 200:
        data = response.json()
        fun_fact = data.get('text', 'No fun fact available.')
    else:
        fun_fact = 'No fun fact available.'

    # Construct the response
    result = {
        "number": number,
        "is_prime": is_prime,
        "is_perfect": is_perfect,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }

    return JSONResponse(
        status_code=200,
        content=result
    )
