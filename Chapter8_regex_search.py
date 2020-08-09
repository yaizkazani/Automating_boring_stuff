"""
What: regex search in strings
Where: in all files with selected suffix in selected folder
Input: path, file suffix, regex
Return: list of strings where regex match was found
"""


def regex_search(path_to_folder, file_type, regex):
	import re, pathlib, sys
	result = []
	reg = re.compile(r"%s" % regex)
	if pathlib.Path(path_to_folder).exists() and pathlib.Path(path_to_folder).is_absolute():
		p = pathlib.Path(path_to_folder)
	elif pathlib.Path(pathlib.Path.cwd() / path_to_folder).exists():
		p = pathlib.Path.cwd() / path_to_folder
	else:
		print("Path to folder was not found, exiting")
		sys.exit(1)
	for _ in pathlib.Path(p).glob("*.%s" % file_type):
		with open("%s" % _, mode="r") as file:
			strings = file.readlines()
			for s in strings:
				if reg.findall(s):
					result.append(s.rstrip())
	return result


ret = regex_search(r"../", "txt", r"\w{3}\d{5}41")
for _ in ret:
	print(_)
