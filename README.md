\# LLM Red Team Risk Evaluator



A lightweight red-teaming dashboard and API for testing LLM responses against adversarial prompts such as prompt injection, hallucination, privacy leakage, toxicity, and jailbreak attempts.



\## Dashboard Preview



!\[LLM Red Team Risk Evaluator Dashboard](assets/dashboard.png)



\## Features



\- Runs adversarial prompt evaluations

\- Scores responses as PASS or FAIL

\- Generates CSV risk reports

\- Provides FastAPI endpoint for triggering evaluations

\- Includes Streamlit dashboard for visual inspection



\## Tech Stack



Python, FastAPI, Streamlit, Pandas



\## Run Locally



```bash

pip install -r requirements.txt

python app/evaluator.py

streamlit run app/dashboard.py

