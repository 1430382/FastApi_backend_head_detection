from fastapi import FastAPI
from database import *
app = FastAPI()
#connect on startup to DB

@app.get("/")
async def root():
		detect = Detect.select()
		return list(detect)
		#return {"meesage":"hello world"}
