# Filling in the Gaps
#
# Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt,
# and so on, in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt
# and spam003.txt but no spam002.txt). Have the program rename all the later files to close this gap.
#
# As an added challenge, write another program that can insert gaps into numbered files so that a new file can be added.
# spam001.txt  // spam56.txt // 10spam.txt // spam00123spam.txt
#
# Generating files for test↓
# folderpath = Path(r"C:\temp\testing")
# for i in range(10):
# 	filename1 = "1stpattern" + str(i).rjust(3, "0") + "file.txt"
# 	filename2 = "2ndpattern___" + str(i).rjust(3, "0") + "file.txt"
# 	Path.touch(Path.joinpath(folderpath, filename1))
# 	Path.touch(Path.joinpath(folderpath, filename2))

def name_parser(file_name):
	"""
	!NB we assume that filename does_not start with counter like 123spam.txt,
	!!!The last digit[s] found will be treated as counter!!!
	:param file_name: name of file that need to be analyzed to find counter part that used to count files
	:return: indices of counter's start and counter's end are returned
	"""

	import re, sys
	# https://regex101.com/r/3EVqQR/1
	reg = re.compile(r"""
	([a-zA-Z0-9._%+-]*)?  # 1st optional capturing group of name
	([a-zA-Z._%+ -]) # 2nd capturing group used to get non digit separator between name and counter
	(\d{1,20})  # 3rd capturing group - counter
	([a-zA-Z._%+-]*)? # 4rd optional capturing group - stuff after counter
	(\.[a-z]*) # 5th capturing group - suffix
					""", re.VERBOSE)
	try:
		count = reg.search(r"%s" % file_name).group(3)
	except AttributeError:
		print("""
		You have provided weird filename.
		It either starts with counter or just weird
		""")
		return "Error"

	return re.search(r"%s" % count, str(file_name)).start(), re.search(r"%s" % count, str(file_name)).end()


def folder_filter(path_to_folder, file_extension):
	"""
	We go through files to find 1st counter pattern meaning that name_parser has returned 2 digits for indices of start and end of counter
	then we create a folder named after these digits and move all files that meet that pattern (meaning that elements with start/end indices are digits)
	to this folder, then we repeat the process until there are no files that has counter pattern in them left in target folder
	:param path_to_folder: path to folder that need to be filtered
	:param file_extension:  file extension that we work with
	:return: list of created folders
	"""
	from pathlib import Path
	import shutil, os
	path_to_folder = Path(path_to_folder)
	new_folders = []
	while True:
		for file in Path(path_to_folder).glob(f"*{file_extension}"):
			if all(map(lambda x: str(x).isdigit(), name_parser(file))):  # if file has counter pattern in it
				pattern = tuple(name_parser(file))
				foldername = Path.joinpath(path_to_folder, str(pattern))
				new_folders.append(str(foldername))
				try:
					os.mkdir(foldername)  # try to create a new folder for this pattern
					break
				except FileExistsError:
					break
				finally:
					for file in Path(path_to_folder).glob(f"*{file_extension}"):  # move all files that meet that pattern to this folder
						if str(file)[pattern[0]:pattern[1]].isdigit() and not str(file)[pattern[0] - 1:pattern[1] + 1].isdigit():  # and not to fix possible issue when files with bigger pattern put in same folder as files with smaller pattern
							shutil.move(str(file), foldername)
					continue

		print("Done")
		return new_folders


def gap_filler(path_to_folder, file_extension):
	"""
	This function do the following:
	1. call folder_filter to separate files to different folders by their counter patterns
	2. go through these folders
	3. extract counter from the first file, then go through files and change their names so counters are in arithmetic progression of 1
	:param path_to_folder: path to folder with files
	:param file_extension: file extension to process
	:return:
	"""

	from pathlib import Path
	import sys, os, shutil
	path_to_folder = Path(path_to_folder)
	path_to_folder = path_to_folder if Path.is_absolute(path_to_folder) else Path.joinpath(Path.cwd() / path_to_folder)
	if not Path.exists(path_to_folder):
		sys.exit("Target folder was not found")
	filenames = []
	new_folders = folder_filter(path_to_folder, file_extension)
	for folder, subfolder, filenames in os.walk(path_to_folder):
		if filenames:
			counter_index_start, counter_index_end = name_parser(filenames[0])  # get counter indices for files in current directory. Actually we assume that it contains ONLY our files since its newly created :)
			prev_counter = 0 if not filenames[0][counter_index_start:counter_index_end].lstrip("0") else filenames[0][counter_index_start:counter_index_end].lstrip("0") # 0 if counter is 00..0, else cut it by indices
			first = True
			for file in filenames:
				if str(file).endswith(file_extension) and folder in new_folders:  # ensure that we process only our files in our folders
					counter = 0 if not file[counter_index_start:counter_index_end].lstrip("0") else int(file[counter_index_start:counter_index_end].lstrip("0"))
					if prev_counter != counter - 1 and not first:  # okay - we're on the 2+ cycle iteration so we can check now
						counter = prev_counter + 1
						shutil.move(Path.joinpath(Path(folder), file), Path.joinpath(Path(folder), f"{file[:counter_index_start]}{str(counter).rjust(counter_index_end - counter_index_start, str(0))}{file[counter_index_end:]}"))
					prev_counter = counter
					first = False
	print("Done")


gap_filler(r"C:\temp\testing", ".txt")
