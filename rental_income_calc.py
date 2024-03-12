# 1st Version with Class but didn't work

class Rental_cal():
    def __init__(self):
        self.income = []
        self.expenses = []
        self.cash_flow = []
        self.annual_cash_flow = []
        self.roi = []
        

    def total_income(self):
        rent_amnt = int(input("Enter rent amount."))
        ti_misc_amnt = int(input("Enter any miscellaneous income amount."))
        total_income_var = rent_amnt + ti_misc_amnt
        self.income.append(total_income_var)


    def total_expenses(self):
        tax_amnt = int(input("Enter taxes amount."))
        ins_amnt = int(input("Enter insurance amount."))
        uty_amnt = int(input("Enter utilities amount."))
        vcy_amnt = int(input("Enter vacancy amount."))
        rep_amnt = int(input("Enter repair amount."))
        mgr_amnt = int(input("Enter property manager amount."))
        te_misc_amnt = int(input("Enter any miscellaneous expenses amount."))
        total_expenses_var = tax_amnt + ins_amnt + uty_amnt + vcy_amnt + rep_amnt + mgr_amnt + te_misc_amnt
        self.expenses.append(total_expenses_var)


    def cash_flow(self):
        total_income_var = sum(self.income)
        total_expenses_var = sum(self.expenses)
        self.cash_flow.append(total_income_var + total_expenses_var)


    def annual_cash_flow(self):
        annual_cash_flow_var = sum(self.annual_cash_flow) * 12
        self.annual_cash_flow.append(annual_cash_flow_var)


    def total_roi(self):
        dwn_amnt = int(input("Enter down payment amount."))
        cls_amnt = int(input("Enter closing costs amount."))
        fix_amnt = int(input("Enter fixing/rehab amount."))
        tr_misc_amnt = int(input("Enter any miscellaneous investment amounts"))
        invest_amnt = dwn_amnt + cls_amnt + fix_amnt + tr_misc_amnt
        roi_var = sum(self.annual_cash_flow) / invest_amnt
        self.roi.append(roi_var)
        print(f"Total Income: {self.income}")
        print(f"Total Expenses: {self.expenses}")
        print(f"Monthly Cash Flow: {self.cashflow_list}")
        print(f"Annual Cash Flow: {self.annual_cash_flow_list}")
        print(f"ROI: {self.roi}")



    def runner(self):
        while True:
            menu_i = input("Type 'A' to start or 'Q' to quit: ").lower()
            if menu_i == "a":
                self.total_income()
                self.total_expenses()
                self.cash_flow()
                self.annual_cash_flow()  
                self.total_roi()
                print(f"Total Income: {self.income}")
                print(f"Total Expenses: {self.expenses}")
                print(f"Monthly Cash Flow: {self.cash_flow}")
                print(f"Annual Cash Flow: {self.annual_cash_flow}")
                print(f"ROI: {self.roi}")
            elif menu_i == "q":
                print("Thank you for stopping by!")
                break
            else:
                print("Please enter 'A' or 'Q'")



rental_calculator = Rental_cal()
rental_calculator.runner()

