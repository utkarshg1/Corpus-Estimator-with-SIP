## Corpus Estimator Streamlit App

#### Overview
The **Corpus Estimator** is a Streamlit app designed to help users estimate the corpus needed for retirement and the required monthly SIP to achieve it, based on inputs like monthly expenses, inflation, asset growth rate, and more.

#### Features
- **Input Parameters**:
  - **Monthly Expense (INR)**: Your current monthly expenses.
  - **Date of Birth**: Used to calculate your current age.
  - **Inflation Rate (%)**: Expected inflation rate.
  - **Withdrawal Rate (%)**: Annual withdrawal rate post-retirement.
  - **Asset Growth Rate (%)**: Expected growth rate of your investments.
  - **Retirement Age**: Desired age to retire.
  - **Safety Multiplier**: A buffer multiplier to account for uncertainties.

- **Results**:
  - **Current Age**
  - **Years to Retirement**
  - **Estimated Corpus Needed**
  - **Estimated Monthly SIP**

#### How to Use
1. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:
   ```bash
   python -m streamlit run app.py
   ```

3. Enter your details and click **"Calculate"** to get your results.

#### Calculation Logic
The app calculates:
- **Estimated Corpus**: Total money needed for retirement.
- **Estimated SIP**: Monthly amount needed to save for your retirement.

#### Example
For a 30-year-old planning to retire at 60 with ₹30,000 monthly expenses, the app will calculate the required corpus and the monthly SIP based on inflation, growth rate, and other parameters.

---