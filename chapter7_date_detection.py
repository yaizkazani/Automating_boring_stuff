# Date Detection
#
# Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days range from 01 to 31, the months range from 01 to 12,
# and the years range from 1000 to 2999. Note that if the day or month is a single digit, it’ll have a leading zero.
#
# The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept nonexistent dates like 31/02/2020 or 31/04/2021.
# Then store these strings into variables named month, day, and year, and write additional code that can detect if it is a valid date. April, June, September, and November have 30 days,
# February has 28 days, and the rest of the months have 31 days. February has 29 days in leap years. Leap years are every year evenly divisible by 4, except for years evenly divisible by 100,
# unless the year is also evenly divisible by 400. Note how this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date.


def get_date_from_text(text):
	"""
	:param text: text where we look for dates
	:return: list of dates
	"""
	import re
	ans = []
	date_re = re.compile(r"""
	\b # boundary
	(0[1-9]|[1-2][0-9]|3[0-1]) # days: 01-09 OR 10-29 OR 30-31
	\/  # / 
	(0[1-9]|1[1-2]) # months 01-09 OR 11-12
	\/
	([1-2][0-9]{3}) # years 1000 - 2999
	\b
	""", re.VERBOSE)
	matches = date_re.finditer(text)
	if len(str(matches)) > 0:
		for date in matches:
			ans.append(date.group(0))
	else:
		return None
	return ans


def check_date_validity(dates):
	"""
	:param dates: list of dates
	:return: dictionary where found dates is keys and "valid"/"invalid" is values
	"""
	ans = dict()
	for date in dates:
		tmp = date.split("/")
		day, month, year = int(str(tmp[0])), str(tmp[1]), int(str(tmp[2]))
		isleap = True if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else False
		ans[str(date)] = "invalid" if (day > 28 and str(month) == "02" and not isleap) or (day > 29 and str(month) == "02" and isleap) or (day > 30 and month in ["04", "06", "09", "11"]) else "valid"
	return ans

text ="""
	01/11/1986 12/12/2999 31/13/1999 00/12/1999 32/11/1999 31/02/2020 or 31/04/2021
	31/01/1999
	"""

result = check_date_validity(get_date_from_text(text))
for key in result.keys():
	print(key, result[key])