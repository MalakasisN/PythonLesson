import datetime
import re

def check_date(year, month, day):
	try:
		datetime.datetime(year=year,month=month,day=day)
	except ValueError:
		return False

	return True
def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0
def f(x):
    if len(x)==11:
        date=re.compile('(\d{6})\d{3}\d{1}\d{1}')
        matches=date.findall(x)
        amkadate=list(matches)[0]
        amkayear=int('19'+amkadate[4:6])
        amkamonth=int(amkadate[2:4])
        amkaday=int(amkadate[0:2])
        if is_luhn_valid(x) and check_date(amkayear, amkamonth, amkaday):
            gender=re.compile('\d{6}\d{3}(\d{1})\d{1}')
            matches1=gender.findall(x)
            amkagendernum=int(list(matches1)[0])
            if amkagendernum%2==0:
                return True
            else:
                return False
        else:
            print('Wrong Amka')
    else:
        raise Exception('This is not AMKA format')
f('18076020025')