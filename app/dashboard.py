import streamlit as st
import pandas as pd
from pathlib import Path
from evaluator import run_evaluation

ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = ROOT / "reports"

st.set_page_config(page_title="LLM Red Team Risk Evaluator", layout="wide")

st.title("LLM Red Team Risk Evaluator")
st.write("Run adversarial prompt tests and review model risk reports.")

if st.button("Run Evaluation"):
    run_evaluation()
    st.success("Evaluation completed. Report generated.")

reports = sorted(REPORTS_DIR.glob("*.csv"), reverse=True)

if reports:
    latest_report = reports[0]
    df = pd.read_csv(latest_report)

    total_tests = len(df)
    failed_tests = len(df[df["status"] == "FAIL"])
    pass_rate = round((len(df[df["status"] == "PASS"]) / total_tests) * 100, 2)
    avg_risk = round(df["risk_score"].mean(), 2)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Tests", total_tests)
    col2.metric("Failed Tests", failed_tests)
    col3.metric("Pass Rate", f"{pass_rate}%")
    col4.metric("Avg Risk Score", avg_risk)

    st.subheader("Latest Report")
    st.caption(str(latest_report))
    st.dataframe(df, width="stretch")

    st.subheader("Failure Categories")
    failed_df = df[df["status"] == "FAIL"]

    if not failed_df.empty:
        st.bar_chart(failed_df["category"].value_counts())
    else:
        st.success("No failures detected.")
else:
    st.info("No reports found. Run an evaluation first.")