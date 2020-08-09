# Get the text off the clipboard.
# Find all phone numbers and email addresses in the text.
# Paste them onto the clipboard.


def clipboard(option, data=""):
	"""
	:param option: "paste" returns clipboard contents, "copy" - send data to clipboard
	:param data: data that need to be sent to clipboard
	:return: clipboard contents if "paste" option is used
	"""
	import pyperclip
	if option == "paste":
		return pyperclip.paste()
	elif option == "copy" and data:
		pyperclip.copy(data)
	else:
		pyperclip.copy("Empty data or invalid argument")


def reg_find_email_or_phone(option, text=""):
	"""
	:param option: "email" - to find emails that look like address@something.something
				   "phone" - to find phone numbers like +7-123-456-10-23 or +79196123456
	:param text: text to process (actually data from clipboard)
	:return: processed regex matches
	"""
	import re
	if option == "email":
		email_re = re.compile(r"""(
		[a-zA-z0-9._%+-]+  # username
		@  # at
		[a-zA-z0-9.-]+  # domain
		\.  # dot
		[a-zA-z]{2,4} # country domain
		)""", re.VERBOSE)
		return "emails found: " + ",".join(re.findall(email_re, text))
	elif option == "phone":
		phone_re = re.compile(r"\+?([7|8])-?\(?(\d{3,}?)\)?\-?(\d{3}\-?\-?\d{2,}\-?\d{0,2})")
		return "phones found: " + ",".join(["-".join([phone.group(1), phone.group(2), phone.group(3)]) for phone in re.finditer(phone_re, text) if len(str(phone.group(0)).replace("-", "").replace("+", "").replace("(", "").replace(")", "")) <= 11])

	else:
		return text


data = clipboard("paste")
clipboard("copy", reg_find_email_or_phone("email", data) + "\n" + reg_find_email_or_phone("phone", data))
print("Found emails and phones copied to clipboard")

