from pydantic import BaseModel, Field
from datetime import date


class CorpusEstimator(BaseModel):
    monthly_expense: float = Field(gt=0.0)
    inflation_rate: float = Field(gt=0.0, default=6.0)
    withdrawal_rate: float = Field(gt=0.0, default=4.0)
    asset_growth_rate: float = Field(gt=0.0, default=12.0)
    retirement_age: int = Field(gt=0, default=60)
    dob: date = Field(le=date.today())
    safety_multiplier: float = Field(gt=0.0, default=1.5)

    def calculate_age(self) -> int:
        """Calculates the current age based on the date of birth."""
        today = date.today()
        age = today.year - self.dob.year
        if (today.month < self.dob.month) or (today.month == self.dob.month and today.day < self.dob.day):
            age -= 1
        return age

    def calculate_years_to_retire(self) -> int:
        """Calculates the number of years remaining until retirement."""
        current_age = self.calculate_age()
        if current_age >= self.retirement_age:
            raise ValueError(f"Already at or past retirement age: \
                             {self.retirement_age}")
        return self.retirement_age - current_age

    def estimate_corpus(self) -> float:
        """Estimates the corpus required to retire."""
        annual_expense = self.monthly_expense * self.safety_multiplier * 12
        years_to_retire = self.calculate_years_to_retire()
        future_value = annual_expense * \
            (1 + self.inflation_rate / 100) ** years_to_retire
        corpus = future_value / (self.withdrawal_rate / 100)
        return corpus

    def estimate_sip(self) -> float:
        """Estimates the monthly SIP required to reach the required corpus."""
        corpus = self.estimate_corpus()
        months_to_retire = self.calculate_years_to_retire() * 12
        rate_of_return = self.asset_growth_rate / 1200  # Monthly growth rate
        factor = ((1 + rate_of_return) ** months_to_retire - 1) * \
            (1 + rate_of_return) / rate_of_return
        estimated_sip = corpus / factor
        return estimated_sip


if __name__ == "__main__":
    c1 = CorpusEstimator(monthly_expense=50_000.0, dob=date(1994, 12, 16))
    current_age = c1.calculate_age()
    years_to_retire = c1.calculate_years_to_retire()
    estimated_corpus = c1.estimate_corpus()
    estimated_sip = c1.estimate_sip()
    print(c1)
    print(f"Current Age : {current_age} years")
    print(f"Years to retire : {years_to_retire} years")
    print(f"Estimated Corpus : {estimated_corpus:,.2f} INR")
    print(f"Estimated SIP : {estimated_sip:,.2f} INR")
