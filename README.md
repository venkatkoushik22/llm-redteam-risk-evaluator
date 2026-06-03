

<h1 align="center">LLM Red Team Risk Evaluator</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue">
  <img src="https://img.shields.io/badge/FastAPI-API-green">
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-red">
  <img src="https://img.shields.io/badge/LLM%20Safety-Red%20Teaming-purple">
</p>

 **Live Demo:** https://huggingface.co/spaces/Venkatkoushik22/llm-redteam-risk-evaluator

A lightweight red-teaming dashboard and API for testing LLM responses against adversarial prompts such as prompt injection, hallucination, privacy leakage, toxicity, and jailbreak attempts.

## Why This Project

Most LLM projects focus only on generating answers. This project focuses on what happens before deployment: testing where an AI system fails.

The evaluator runs adversarial prompts across common LLM risk categories and generates structured reports with pass/fail scoring, risk scores, and dashboard-based failure analysis.

The current version uses a simulated LLM response layer for safe local testing, but the design allows real model APIs or local models to be plugged in later.


<p align="center">
  <img src="./assets/dashboard.png" alt="LLM Red Team Risk Evaluator Dashboard" width="900">
</p>

## Features

* Runs adversarial prompt evaluations
* Tests prompt injection, hallucination, privacy leakage, toxicity, and jailbreak behavior
* Generates CSV risk reports
* Provides a FastAPI endpoint for triggering evaluations
* Includes a Streamlit dashboard for reviewing failures
* Tracks pass rate, failed tests, and average risk score

## Tech Stack

Python, FastAPI, Streamlit, Pandas

## Project Structure

```text
llm-redteam-risk-evaluator/
├── app/
│   ├── dashboard.py
│   ├── evaluator.py
│   └── main.py
├── prompts/
│   └── test_prompts.json
├── reports/
├── assets/
│   └── dashboard.png
├── requirements.txt
└── README.md
```

## Run Locally

```bash
pip install -r requirements.txt
```

Run the evaluator:

```bash
python app/evaluator.py
```

Run the dashboard:

```bash
streamlit run app/dashboard.py
```

Run the API:

```bash
uvicorn app.main:app --reload
```

Open API docs:

```text
http://127.0.0.1:8000/docs
```

## Output

The system creates structured CSV reports with:

* Prompt category
* Test prompt
* Model response
* Risk score
* PASS or FAIL status

## Future Improvements

* Add real LLM API integration
* Add local model support with Ollama
* Add DeepEval or DeepTeam based scoring
* Export reports as JSON and PDF
* Add historical comparison across evaluation runs

