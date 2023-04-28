#MegaFocusDev

import os

print(f"Current directory: {os.getcwd()}")
# ask the user for a file extension type
extension = input("Enter file extension (e.g. .txt): ")

# ask the user whether to delete only in current directory or in subdirectories as well
while True:
    reply = input("Do you want to delete files only in the current directory or in subdirectories as well? (c/s): ")
    if reply.lower() == "c":
        delete_in_subdirs = False
        break
    elif reply.lower() == "s":
        delete_in_subdirs = True
        break
    else:
        print("Invalid input. Please enter c or s.")

# ask for confirmation before deleting files
reply = input(f"Do you really want to delete all files with extension {extension}? (y/n): ")
if reply.lower() == "n":
    print("Deletion cancelled.")
else:
    # get the current working directory
    cwd = os.getcwd()

    # loop through all files and directories in the directory
    for root, dirs, files in os.walk(cwd):
        # determine whether to delete files in this directory or not
        if delete_in_subdirs or os.path.samefile(root, cwd):
            for filename in files:
                # check if the file has the extension given by the user
                if filename.endswith(extension):
                    # delete the file without asking for confirmation
                    try:
                        os.remove(os.path.join(root, filename))
                        print(filename, "deleted.")
                    except Exception as e:
                        print("Error:", e)