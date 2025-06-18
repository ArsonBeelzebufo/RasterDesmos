import dotenv
import os

dotenv.load_dotenv()
filepath=os.getenv("BMPPath")
with open(filepath,'rb') as file:
    content=file.read()
    fileHead=content[:14]
    