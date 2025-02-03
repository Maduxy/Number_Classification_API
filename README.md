# info_retriever
1. # Project Overview
 This is a FastAPI-based API that classifies a given integer by returning various properties such as:
- Whether the number is prime (using the `sympy` library)
- Whether the number is perfect (using the `sympy` library)
- The sum of its digits
- Its Armstrong property (if applicable)
- Its parity (even or odd)
- A fun math fact fetched from the [Numbers API](http://numbersapi.com)

2. # How to Run Locally
git clone https://github.com/Maduxy/Number_Classification_API
cd Number_Classification_API
pip install -r requirements.txt
uvicorn main:app --reload

3. # API Endpoint
GET /api/classify-number/?number = 5 → Returns:
    
{"number":5,
"is_prime":true,
"is_perfect":false,
"properties":["Armstrong","odd"],
"digit_sum":5,
"fun_fact":"5 is the number of Platonic solids. //gotten from the numbers API"
}

4. # Live API
Base URL: https://number-classification-api-rxos.onrender.com

5. # [Python Developers]
(https://hng.tech/hire/python-developers)