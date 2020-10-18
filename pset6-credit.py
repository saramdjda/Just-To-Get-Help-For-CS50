# A program to report if a credit card is valid

from cs50 import get_int


def main():

    # Ask for the credit card number
    card_number = get_card_number()

    # Results
    if (validation(card_number) == True):
        type_of_card(card_number)
    else:
        print("INVALID")


# Ask for the credit card number
def get_card_number():
    while True:
        n = get_int("Credit card number: ")
        if n > 0:
            break
    return n


# Validation
def validation(ccn):
    length = len(str(ccn))
    if (length == 13 or length == 15 or length == 16) and check(ccn):
        return True
    else:
        return False


# Luhn's algorithm
def check(ccn):
    luhn = 0
    for i in range(len(str(ccn))) and ccn != 0:
        if i % 2 == 0:
            luhn += ccn % 10
        else:
            digit = 2 * (ccn % 10)
            luhn += digit / 10 + digit % 10
        ccn /= 10
    if luhn % 10 == 0:
        return True
    else:
        return False


# Say the report (valid or invalid)
def type_of_card(ccn):
    if ((ccn >= 34e13 and ccn < 35e13) or (ccn >= 37e13 and ccn < 38e13)):
        print("AMEX")
    elif (ccn >= 51e14 and ccn < 56e14):
        print("MASTERCARD")
    elif ((ccn >= 4e12 and ccn < 5e12) or (ccn >= 4e15 and ccn < 5e15)):
        print("VISA")
    else:
        print("INVALID")


main()
