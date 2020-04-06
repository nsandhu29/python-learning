class EMIClaculation():
    '''
    EMI = [P x R x (1+R)^N]/[(1+R)^N - 1], where P stands for the loan amount or principal,
    R is the interest rate per month [if the interest rate per annum is 11%, then the rate of interest will be 11/(12 x 100)],
    and N is the number of monthly instalments.
    '''

    def __init__(self, loan_amount, rate_of_interest, loan_duration, down_payment):
        self.loan_amount = loan_amount
        self.rate_of_interest = rate_of_interest
        self.loan_duration = loan_duration
        self.down_payment = down_payment

    def minimum_emi(self):
        principal = self.loan_amount - self.down_payment
        rate = self.rate_of_interest / (12 * 100)
        emi_number = self.loan_duration * 12
        emi = round((principal * rate * pow(1 + rate, emi_number)) / (pow(1 + rate, emi_number) - 1), 2)
        print('Monthly installment = ', emi)
        print('Total amount paid = ', round(emi * emi_number))
        print('You pay extra =', round((emi * emi_number) - principal))


emi1 = EMIClaculation(1200000, 11.9, 2, 0)

print("Calculated EMI ", emi1.minimum_emi())

# Derivation of EMI formula??



