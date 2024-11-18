from calculations import CorpusEstimator
import streamlit as st
from datetime import date

# Setup page config and title
st.set_page_config(page_title="Corpus Estimator")
st.title("Corpus Estimator")
st.subheader("by Utkarsh Gaikwad")

# Inputs
monthly_expense = st.number_input(
    "Monthly Expense (INR)", min_value=1000, step=1000)
dob = st.date_input(
    "Date of Birth", min_value=date(1990, 1, 1), max_value=date.today())
inflation_rate = st.number_input(
    "Inflation Rate (%)", min_value=0.0, max_value=100.0, value=6.0)
withdrawal_rate = st.number_input(
    "Withdrawal Rate (%)", min_value=0.0, max_value=100.0, value=4.0)
asset_growth_rate = st.number_input(
    "Asset Growth Rate (%)", min_value=0.0, max_value=100.0, value=12.0)
retirement_age = st.number_input(
    "Retirement Age", min_value=18, max_value=100, value=60)
safety_multiplier = st.number_input(
    "Safety Multiplier", min_value=1.0, max_value=5.0, value=1.5)


if st.button("calculate"):
    # Create an instance of CorpusEstimator
    corpus_estimator = CorpusEstimator(
        monthly_expense=monthly_expense,
        dob=dob,
        inflation_rate=inflation_rate,
        withdrawal_rate=withdrawal_rate,
        asset_growth_rate=asset_growth_rate,
        retirement_age=retirement_age,
        safety_multiplier=safety_multiplier
    )

    # Results
    current_age = corpus_estimator.calculate_age()
    years_to_retire = corpus_estimator.calculate_years_to_retire()
    estimated_corpus = corpus_estimator.estimate_corpus()
    estimated_sip = corpus_estimator.estimate_sip()

    # Display Results
    st.write(f"### Current Age: {current_age} years")
    st.write(f"### Years to Retirement: {years_to_retire} years")
    st.write(f"### Estimated Corpus Needed: ₹{estimated_corpus:,.0f}")
    st.write(f"### Estimated Monthly SIP: ₹{estimated_sip:,.0f}")
