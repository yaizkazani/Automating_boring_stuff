# Deleting Unneeded Files
#
# It’s not uncommon for a few unneeded but humongous files or folders to take up the bulk of the space on your hard drive.
# If you’re trying to free up room on your computer, you’ll get the most bang for your buck by deleting the most massive of the unwanted files.
# But first you have to find them.
#
# Write a program that walks through a folder tree and searches for exceptionally large files or folders—say,
# ones that have a file size of more than 100MB. (Remember that to get a file’s size, you can use os.path.getsize() from the os module.)
# Print these files with their absolute path to the screen.


def delete_big_files(start_path):
	"""
	:param start_path: root folder to start scan from and go through all child folders
	:return: list of big files(>100 MB) and folders(>2 GB)
	"""

	import os, send2trash, pyinputplus, sys
	from pathlib import Path

	files_large = []
	folders_large = []
	start_path = Path(start_path) if Path.is_absolute(Path(start_path)) else Path.joinpath(Path.cwd() / Path(start_path))
	if not Path.exists(start_path):
		sys.exit("Target path was not found")
	for folder, subfolder, files in os.walk(start_path):
		folder_size = 0
		folder_path = Path(folder)
		for file in files:
			file_path = Path.joinpath(Path(folder) / Path(file))
			file_size = os.path.getsize(file_path)
			folder_size += file_size
			if file_size > 104857600:
				files_large.append(file_path)
				print(f"Large file found, path: {file_path} , size is {file_size / 1048576} MB")
		if folder_size / 1048576 > 2048:
			folders_large.append(folder_path)
			print(f"Large folder found, path: {folder_path}, size is {folder_size / 1048576} MB")
	return files_large, folders_large


delete_big_files(r"C:\Users\yaizk\Downloads\Microsoft Office 2016-2019 (2019.10) RePack by KpoJIuK")
