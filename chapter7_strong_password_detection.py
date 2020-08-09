# Strong Password Detection
#
# Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password is defined as one that is at least eight characters long,
# contains both uppercase and lowercase characters, and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.


def test_password(pwd):
	import re
	return True if re.search(r"[a-z]", pwd) and re.search(r"[A-Z]", pwd) and re.search(r"\d", pwd) else False

print(test_password("abcdA1"))
print(test_password("abcdA"))
print(test_password("abcd1"))