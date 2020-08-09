# Regex Version of the strip() Method
#
# Write a function that takes a string and does the same thing as the strip() string method. If no other arguments are passed other than the string to strip,
# then whitespace characters will be removed from the beginning and end of the string.
# Otherwise, the characters specified in the second argument to the function will be removed from the string.


def regex_strip(string, s=" "):
	"""
	:param string: string that we work on
	:param s: substring to be replaced with ""
	:return: string with removed substring
	"""
	import re
	return re.sub(re.compile(re.escape(s)), "", string)

print(regex_strip("abcd e z", "d e"))