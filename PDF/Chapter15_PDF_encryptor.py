# Using the os.walk() function from Chapter 10, write a script that will go through every
# PDF in a folder (and its subfolders) and encrypt the PDFs using a password provided on the command line.
# Save each encrypted PDF with an _encrypted.pdf suffix added to the original filename.
# Before deleting the original file, have the program attempt to read and decrypt the file to ensure that it was encrypted correctly.
#
# Then, write a program that finds all encrypted PDFs in a folder (and its subfolders) and
# creates a decrypted copy of the PDF using a provided password. If the password is incorrect,
# the program should print a message to the user and continue to the next PDF.

import PyPDF2, os, sys, send2trash, pathlib


def encrypt(filename, password):
    """
    :param filename: filename to encrypt
    :param password: password to use
    :return: None if failed, "Done" if successful
    """
    with open(filename, "rb") as readfile:
        reader = PyPDF2.PdfFileReader(readfile)  # create writer and reader
        writer = PyPDF2.PdfFileWriter()
        if not reader.isEncrypted:  # we do not process encrypted files
            for page in range(reader.numPages):
                writer.addPage(reader.getPage(page))  # add pages to the writer
        else:
            print(f"{filename} is encrypted")
            return None
    with open(f"{filename.split('.')[0]}_encrypted.pdf", "wb") as writefile:  # open file fro writing with new name
        writer.encrypt(password)  # set encryption
        try:
            writer.write(writefile)
        except OSError as e:
            print(f"File write error {e}")
            return None
    with open(f"{pathlib.Path(filename).parent}\{pathlib.Path(filename).stem}_encrypted.pdf", "rb") as checkfile:
        result = PyPDF2.PdfFileReader(checkfile).decrypt(password)  # try to decrypt file before deleting original file
    if result != 0:  # 0 = decryption failed
        try:
            send2trash.send2trash(filename)
            print(f"file {filename} was deleted after encrypted file verification")
            return "Done"
        except OSError as e:
            print(f"Delete error: {e}, filename: {filename}")
    else:
        print("Encrypted file %s was not verified so original file %s was not deleted" % (f"{filename.split('.')[0]}_encrypted.pdf", filename))
        return None


def decrypt(filename, password):
    """
    :param filename: name of the .pdf file to decrypt
    :param password: password to try
    :return: None if failed, else "Done"
    """
    with open(filename, "rb") as readfile:
        reader = PyPDF2.PdfFileReader(readfile)
        writer = PyPDF2.PdfFileWriter()
        if not reader.isEncrypted:
            print(f"{filename} is not_encrypted")
            return None
        else:
            result = reader.decrypt(password)
            if result == 0:
                print(f"{filename} was not decrypted with password: {password}")
                return None
            else:
                for page in range(reader.numPages):
                    writer.addPage(reader.getPage(page))
                try:
                    with open(f"{filename.strip('_encrypted.pdf')}_decrypted.pdf", "wb") as writefile:
                        writer.write(writefile)
                except OSError as e:
                    print(f"File write error {e}")
                    return None
                return "Done"


password = sys.argv[1]  # password to use
option = sys.argv[2]  # mode to use
if option not in ["encrypt", "decrypt"]:
    sys.exit(f"Wrong option, option provided is {option}, supposed to be encrypt or decrypt")
folder_path = os.path.abspath(input("Please enter the path\n"))
if os.path.exists(folder_path):  # if path exists
    for folder, subfolders, files in os.walk(folder_path):  # walk through it
        pdfs = filter(lambda x: str(x).lower().endswith(".pdf"), files)  # we take only .pdf files
        os.chdir(folder)  # we follow the os.walk to ensure that .abspath will work
        for file in pdfs:
            filename = os.path.abspath(file)  # make absolute name to pass to function
            encrypt(filename, password) if option == "encrypt" else decrypt(filename, password)
    print("Done")
else:
    print(f"{folder_path} doesnt exist, exiting")
    sys.exit(f"{folder_path} not found")
