from fastapi import FastAPI
import logging
import random
import time

app = FastAPI()

# Configure logging
logging.basicConfig(
    format='{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}',
    level=logging.INFO,
)

@app.get("/")
def root():
    logging.info("Root endpoint accessed.")
    return {"message": "Hello World!"}

@app.get("/error")
def error():
    logging.error("An error occurred!")
    return {"message": "Error simulated!"}

@app.get("/debug")
def debug():
    logging.debug("Debug message logged.")
    return {"message": "Debugging log message"}

@app.get("/warn")
def warn():
    logging.warning("Warning issued!")
    return {"message": "Warning log message"}
