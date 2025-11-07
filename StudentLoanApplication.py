class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        """
        Initialize the bank account with an account holder's name and an initial balance.
        """  
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.
        """
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        self.balance += amount
        print(f"${amount} deposited successfully. Current balance: ${self.balance:.2f}")
        return True

    def withdraw(self, amount):  
        """
        Withdraw a specified amount from the account.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.balance:
            print("Insufficient funds.")
            return False
        self.balance -= amount
        print(f"${amount} withdrawn successfully. Current balance: ${self.balance:.2f}")
        return True

    def check_balance(self):
        """
        Check the current balance of the account.
        """
        print(f"Current balance: ${self.balance:.2f}")
        return self.balance

# Example usage:
if __name__ == "__main__":
    account = BankAccount ("Sean Rhee", 100.0)  # Create an account with $100 initial balance
    account.check_balance()                   # Check balance
    account.deposit(50)                       # Deposit $50
    account.withdraw(30)                      # Withdraw $30
    account.withdraw(200)                     # Attempt to withdraw more than the balance


def calculate_loan_info(principal, annual_rate, years):
    """
    Calculate loan information including monthly payment, total payment, and total interest.

    Args:
        principal (float): The loan amount.
        annual_rate (float): Annual interest rate as a percentage (e.g., 5 for 5%).
        years (int): Loan term in years.

    Returns:
        dict: A dictionary with monthly payment, total payment, and total interest.      
    """
    # Convert annual rate to monthly rate
    monthly_rate = (annual_rate / 100) / 12
    # Total number of payments
    total_payments = years * 12
    
    # Monthly payment formula: M = P[r(1 + r)^n] / [(1 + r)^n – 1]
    if monthly_rate == 0:
        # If interest rate is 0%, payments are simply the loan divided by the term
        monthly_payment = principal / total_payments
    else:
        monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** total_payments) / \
                          ((1 + monthly_rate) ** total_payments - 1)
    
    # Total payment over the loan term
    total_payment = monthly_payment * total_payments
    # Total interest paid
    total_interest = total_payment - principal
    
    return {
        "Monthly Payment": round(monthly_payment, 2),   
        "Total Payment": round(total_payment, 2),
        "Total Interest": round(total_interest, 2),
    }

# Example usage of code being used
if __name__ == "__main__":
    print("Loan Calculator")
    principal = float(input("Enter the loan amount (principal): "))
    annual_rate = float(input("Enter the annual interest rate (in %): "))
    years = int(input("Enter the loan term (in years): "))
    
    loan_info = calculate_loan_info(principal, annual_rate, years)
    print("\nLoan Information:")
    for key, value in loan_info.items():
        print(f"{key}: ${value}")

# Sample data: list of loans used to represent fictional data
loans = [
    {"loan_id": 1, "amount": 5000, "type": "government"},
    {"loan_id": 2, "amount": 10000, "type": "private"},
    {"loan_id": 3, "amount": 7500, "type": "government"},
    {"loan_id": 4, "amount": 12000, "type": "private"},
    {"loan_id": 5, "amount": 3000, "type": "government"},
]

# Function to separate loans
def separate_loans(loans):
    government_loans = []
    private_loans = []

    for loan in loans:
        if loan["type"] == "government":
            government_loans.append(loan)
        elif loan["type"] == "private":
            private_loans.append(loan)

    return government_loans, private_loans

# Separate the loans into private and government            
government_loans, private_loans = separate_loans(loans)

# Display the results of government loans and private loans 
print("Government Loans:")        
for loan in government_loans:
    print(loan)

print("\nPrivate Loans:")  #Print Private Loans
for loan in private_loans:
    print(loan)


import requests

def fetch_irs_tax_forms(form_type):
    """     
    Fetch information about specific tax forms from the IRS API.
    """
    api_url = "https://api.irs.gov/forms"
    params = {
        "form_number": form_type,  # Example: "1098" or "1099-C"
        "tax_year": "2023"  # Specify the tax year of the 
    }
    
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        forms_data = response.json()
        
        # Display the fetched information about specific tax forms 
        for form in forms_data:
            print(f"Form Number: {form['form_number']}")  
            print(f"Form Title: {form['form_title']}")
            print(f"Description: {form['description']}")
            print(f"Download URL: {form['form_url']}\n")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage
fetch_irs_tax_forms("1098")
