import os
from dotenv import load_dotenv

load_dotenv()
def Pratham(name):
    return f"Hello {name}"
name = "Pratham"
print(Pratham(name))

SECRET = os.getenv("SECRET")
print(SECRET)