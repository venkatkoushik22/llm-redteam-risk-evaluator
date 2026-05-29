from fastapi import FastAPI
from app.evaluator import run_evaluation

app = FastAPI(
    title="LLM Red Team Risk Evaluator",
    description="API for running basic LLM red-team safety evaluations.",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "LLM Red Team Risk Evaluator is running",
        "endpoints": ["/run-evaluation"]
    }


@app.post("/run-evaluation")
def evaluate():
    run_evaluation()
    return {
        "status": "success",
        "message": "Evaluation completed. Check the reports folder."
    }