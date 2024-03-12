# Apparently all I need was @staticmethod.
# This is a decorator that is used to define a static method within a class.
# I'm still not clear on how to use it but this was all I needed.

class Rental_cal():
    def __init__(self):
        self.income = []
        self.expenses = []
        self.cash_flow = []
        self.annual_cash_flow = []    
        self.roi = []

    def rental_cal(self):
        rent_amnt = int(input("Enter rent amount: "))
        ti_misc_amnt = int(input("Enter any miscellaneous income amount: "))

        total_income_var = rent_amnt + ti_misc_amnt
        self.income.append(total_income_var)
        
        tax_amnt = int(input("Enter taxes amount: "))
        ins_amnt = int(input("Enter insurance amount: "))
        uty_amnt = int(input("Enter utilities amount: "))
        vcy_amnt = int(input("Enter vacancy amount: "))
        rep_amnt = int(input("Enter repair amount: "))
        mgr_amnt = int(input("Enter property manager amount: "))
        te_misc_amnt = int(input("Enter any miscellaneous expenses amount: "))

        total_expenses_var = tax_amnt + ins_amnt + uty_amnt + vcy_amnt + rep_amnt + mgr_amnt + te_misc_amnt
        self.expenses.append(total_expenses_var)

        self.cash_flow.append(total_income_var - total_expenses_var)

        annual_cash_flow_var = sum(self.cash_flow) * 12
        self.annual_cash_flow.append(annual_cash_flow_var)

        dwn_amnt = int(input("Enter down payment amount: "))
        cls_amnt = int(input("Enter closing costs amount: "))
        fix_amnt = int(input("Enter fixing/rehab amount: "))
        tr_misc_amnt = int(input("Enter any miscellaneous investment amounts: "))

        invest_amnt = dwn_amnt + cls_amnt + fix_amnt + tr_misc_amnt
        
        roi_var = round(sum(self.annual_cash_flow) / invest_amnt, 4) * 100
        
        self.roi.append(roi_var)

        print(f"ROI: {self.roi}")
        print(f"Total Income: {self.income}")
        print(f"Total Expenses: {self.expenses}")
        print(f"Monthly Cash Flow: {self.cash_flow}")
        print(f"Annual Cash Flow: {self.annual_cash_flow}")

    # Apparently this is what I was missing.
    # This is a decorator that is used to define a static method within a class.
    # I'm still not clear on how to use it but this was all I needed.
    @staticmethod
    def runner():
        while True:
            menu_i = input("Type 'A' to start or 'Q' to quit: ").lower()
            if menu_i == "a":
                rental_calculator.rental_cal()
            elif menu_i == "q":
                print("Thank you for stopping by!")
                print(f"ROI: {rental_calculator.roi}")
                break
            else:
                print("Please enter 'A' or 'Q'")

rental_calculator = Rental_cal()
rental_calculator.runner()
