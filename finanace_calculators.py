import math

#program that allows user to access two different financial calculators.
#investment and home loan repayment.


#user input which calculator they choose
calculator_choice = input("""
Choose either 'investment' or 'bond' from the menu below to proceed: 

investment     - to calculate the amount of interest you'll earn on interest
bond           - to calculate the amount you'll have to pay on a home loan
       """)

#use str.casefold() to make input non case sensitive - learned on freecodecamp
calculator_choice = calculator_choice.casefold()

#investment follow-up questions

if calculator_choice == "investment":
    deposit = float(input("What is the amount that you want to deposit? eg.10000:  \n"))
    invest_interest = float(int(input("What is your preferred interest rate? eg.8:  \n")))
    years = int(input("How long in years do you want to invest? eg. 5:  \n"))
    sim_comp = input("Would you like 'simple' or 'compound' interest? eg. simple or compund:  \n")
#use str.casefold() to make input non case sensitive - learned on freecodecamp
    sim_comp = sim_comp.casefold()
    
#simple interest calculation
    if sim_comp == "simple":
        invest_calculation = deposit * (1+invest_interest * years)
#compound interest calculation
    elif sim_comp == "compound":
        invest_calculation = deposit * math.pow((1+invest_interest),years)
#Calculations for investment
    print(f"Your total investment in {years} years on {invest_interest}% {sim_comp} interest will be R{invest_calculation}.")

#bond follow-up questions
elif calculator_choice == "bond":
    house_value = int(input("What is the present value of the house? eg.1000000:  \n"))
    bond_interest = float(int(input("What is your preferred interest rate? eg.8:  \n")))
    months_repay_bond = int(input("What is the number of months you would like to repay the bond? eg.72:  \n"))
#bond repayment calculation
    bond_calculation = round((bond_interest/12 * house_value) / (1 - math.pow((1+ bond_interest/12), (-1 * months_repay_bond))))
    print(f"You will pay R{bond_calculation} each month for {months_repay_bond} months.")

#display error message if input is invalid
else:
    print("Please enter a valid input: 'investment' or 'bond'.") 
