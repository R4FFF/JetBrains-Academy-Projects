import math
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--type", help="type", type=str)
parser.add_argument("--principal", help="principal", type=int)
parser.add_argument("--periods", help="periods", type=int)
parser.add_argument("--interest", help="interest", type=float)
parser.add_argument("--payment", help="payment", type=int)

args = parser.parse_args()
n1 = args.type
n2 = args.principal
n3 = args.periods
n4 = args.interest
n5 = args.payment

m = 1
month = 0
result_list = []

if n1 == "diff" and (n2 is not None and n2 > 0) and (n3 is not None and n3 > 0) and (n4 is not None and n4 > 0):
    for _ in range(n3):
        i = n4 / 12 / 100
        month += 1
        result = math.ceil(n2 / n3 + i * (n2 - ((n2 * (m - 1)) / n3)))
        m += 1
        result_list.append(result)
        print(f"Month {month}: payment is {result}")
    print(f"\nOverpayment = {sum(result_list) - n2}")
elif n1 == "annuity" and (n2 is not None and n2 > 0) and (n3 is not None and n3 > 0) and (n4 is not None and n4 > 0):
    i = n4 / 12 / 100
    annuity = n2 * ((i * math.pow(1 + i, n3)) / (math.pow(1 + i, n3) - 1))
    print(f"Your annuity payment = {math.ceil(annuity)}!\nOverpayment = {math.ceil(annuity) * n3 - n2}")
elif n1 == "annuity" and (n3 is not None and n3 > 0) and (n4 is not None and n4 > 0) and (n5 is not None and n5 > 0):
    i = n4 / 12 / 100
    n2 = n5 / ((i * math.pow(1 + i, n3)) / (math.pow(1 + i, n3) - 1))
    print(f"Your loan principal = {math.floor(n2)}!\nOverpayment = {math.ceil(n3 * n5 - n2)}")
elif n1 == "annuity" and (n2 is not None and n2 > 0) and (n4 is not None and n4 > 0) and (n5 is not None and n5 > 0):
    i = n4 / 12 / 100
    months = math.ceil(math.log(float(n5) / (float(n5) - i * float(n2)), i + 1))
    year = divmod(months, 12)
    print(f"It will take {year[0]} years to repay this loan!\nOverpayment = {(n5 * 24) - n2}")
else:
    print("Incorrect parameters.")


