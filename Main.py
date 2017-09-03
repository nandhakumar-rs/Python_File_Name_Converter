# import os package to access the path
# import tkinter package to develope windows application
import os
from tkinter import *
# creating an instance windows for tkinter class
window = Tk()


def convert_file_name(direc):
    """ This function will rename the filename to
    perfect python filename convention format"""
    stri = ""
    for i in os.listdir(direc):
        if check_file_path(direc, i):
            name = i.split(os.extsep, 1)[0]
            ext = i.split(os.extsep, 1)[1]
            if ext == "py" or ext == "py.md":
                for j in name:
                    if j == " " or (ord(j) > 32 and ord(j) < 48):
                        stri += "_"
                    else:
                        stri += j.lower()
                nstr = stri[0].upper()
                nstr+=stri[1:] +  "." + ext
                os.chdir(direc)
                os.rename(direc + '/' + i, nstr)
                stri = ""
        else:
            convert_file_name(direc + '/' + i)


# def prompt_user(direc):
#     qn = input("Do you want to rename the files?")
#     if qn == "yes":
#         convert_name(direc)
#         print("Successfully files renamed")
#     else:
#         print("Thank you")

def check_file_path(path, file):
    """ To check whether the current item is file or folder
    and returns true if it is file else false"""
    if os.path.isfile(path + "/" + file):
        return True
    return False


# def change_file_name(direc):
#     stri = ""
#     for i in os.listdir(direc):
#         if check_file_path(direc, i):
#             name = i.split(os.extsep, 1)[0]
#             ext = i.split(os.extsep, 1)[1]
#             if ext == "py" or ext == "py.md":
#                 for j in name:
#                     if j == " " or (ord(j) > 32 and ord(j) < 48):
#                         stri += "_"
#                     else:
#                         stri += j.lower()
#                 stri += "." + ext
#                 stri = ""
#         else:
#             change_file_name(direc + '/' + i)


def get_url():
    """ This function will get the path from the user
    where the python file must be investigated """
    url = string.get()
    os.chdir(url)
    # change_file_name(url)
    convert_file_name(url)


string = StringVar()
lable = Label(window, text="Enter the URL to rename your files with extension .py and .py.md")
lable.grid(row=0, column=0)
entry = Entry(window, textvariable=string, width=75)
entry.grid(row=1, column=0)
rename = Button(window, text="Rename", command=get_url)
rename.grid(row=1, column=1)
# Tkinter window loop ends here
window.mainloop()
