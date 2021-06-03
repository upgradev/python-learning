class SBI:
    def rate_of_interest(self):
        return 8


class ICICI:
    def rate_of_interest(self):
        return 4


class HDFC:
    def rate_of_interest(self):
        return 7

def common_interest(bank):
    return bank.rate_of_interest()

s =SBI()
ic = ICICI()
h=HDFC()

print(common_interest(s))

print(common_interest(ic))