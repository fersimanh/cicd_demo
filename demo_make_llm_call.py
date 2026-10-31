import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

prompt = (
    "Write a Python function calculate_loan_payment(principal, annual_rate, years) "
    "that returns the monthly payment for a fixed-rate loan. "
    "Return only the Python code, with no markdown fences."
)

response = client.models.generate_content(model="gemini-3.8-flash", contents=prompt)

code = response.text.strip()
if code.startswith("```"):
    code = "\n".join(code.splitlines()[1:-1])

with open("loan_payment.py", "w") as f:
    f.write(code + "\n")

print("Wrote loan_payment.py")
