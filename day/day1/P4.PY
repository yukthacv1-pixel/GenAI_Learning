import os
from dotevn import load_dotenv,dotenv_values,find_dotenv

#Loads .env from current directory
load_dotenv()
congif = dotenv_values(".env")
api_key = config.get("GEMINI_API_KEY")

api_key = config.getenv("GEMINI_API_KEY","")
api_key = config.environ["GEMINI_API_KEY"]
