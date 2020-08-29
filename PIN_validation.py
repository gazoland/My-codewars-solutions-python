"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6
digits.
If the function is passed a valid PIN string, return true, else return false.

eg:

validate_pin("1234") == True
validate_pin("12345") == False
validate_pin("a234") == False
"""

def validate_pin(pin):
    a = len(pin)
    count = 0
    for x in pin:
        if x in '0123456789':
            count += 0
        else:
            count += 1
    if count == 0:
        return a == 4 or a == 6
    else:
        return False


print(validate_pin('723944'))

"""
Solution:

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()
"""