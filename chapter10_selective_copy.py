# Selective Copy
#
# Write a program that walks through a folder tree and searches for files
# 	with a certain file extension (such as .pdf or .jpg). Copy these files
# 	from whatever location they are in to a new folder.


def selective_copy(extension, from_path, to_path):
	import sys, shutil, os
	from pathlib import Path
	"""
	:param extension: extension to be used by .glob()
	:param from_path: path to get files 
	:param copy_path: path to copy files
	:return: None
	"""
	from_path, to_path = Path(from_path), Path(to_path)

	abs_path_from = from_path if Path.is_absolute(from_path) else Path.joinpath(Path.cwd() / from_path)  # making paths absolute
	abs_path_to = to_path if Path.is_absolute(to_path) else Path.joinpath(Path.cwd() / to_path)

	if not abs_path_from.exists():
		sys.exit("Target directory not found")
	if not abs_path_to.exists():
		os.mkdir(abs_path_to)

	for folder, subfolder, files in os.walk(from_path):
		if Path.joinpath(Path.cwd() / Path(folder)) != abs_path_to:  # Prevent errors when copy_path is a child of from_path, otherwise we will try to copy files from and into the same dir.
			for file_to_move in Path(folder).glob(f"*{extension}"):  # filtering files
				shutil.move(str(Path.joinpath(Path.cwd(), file_to_move)), abs_path_to)  # NB !!! This str() requited because .move need a string for .rstrip(), not WindowsPath object. However .copy works fine w/o str()
				print(f"File {file_to_move} moved to {abs_path_to}")


selective_copy(".jpg", r"C:\temp", r"C:\temp\test")