from tkinter import *
from tkinter import filedialog, simpledialog
import os


def get_file(textvar: StringVar):
    """Opens file browser and sets the path of the file chosen to the inputted textvariable"""
    path = filedialog.askopenfilename()
    textvar.set(path)


def create_bat(exe_path, py_path):
    """Prompts user for name and desired location of new bat file, then creates a bat file from the exe/py paths"""
    name_of_file = simpledialog.askstring("File needs name", prompt="What is the name of the batch file:")
    new_file_location = filedialog.askdirectory()
    new_txt_file_path = f'{new_file_location}/{name_of_file}.txt'
    new_bat_file_path = f'{new_file_location}/{name_of_file}.bat'

    with open(new_txt_file_path, mode='w') as notepad:
        notepad.write(f'"{exe_path}" "{py_path}"\npause')

    os.rename(new_txt_file_path, new_bat_file_path)
    os.startfile(new_file_location)

    print('Batch file created, opening location')

    # save location of exe path to autofill next time program is launched
    with open('python_exe_path', mode='w') as file:
        file.write(exe_path)


root = Tk()
root.title("Batch File Creator - Python")
root.geometry("")  # allows window to dynamically resize to fit the contents of labels
root.config(padx=90, pady=50)

python_exe_strvar = StringVar(root, value="path for python.exe")
py_file_strvar = StringVar(root, value="path for py file")

python_exe_label = Label(root, textvariable=python_exe_strvar, bg='white')
py_file_label = Label(root, textvariable=py_file_strvar, bg='white',)

# use lambdas to pass args through button command
python_exe_button = Button(root, text='Browse', command=lambda: get_file(textvar=python_exe_strvar))
py_file_button = Button(root, text='Browse', command=lambda: get_file(textvar=py_file_strvar))
make_bat = Button(root, text="Make Batch file", command=lambda: create_bat(exe_path=python_exe_strvar.get(),
                                                                           py_path=py_file_strvar.get()))

python_exe_label.grid(row=0, column=0)
py_file_label.grid(row=0, column=2)
python_exe_button.grid(row=1, column=0, pady=15)
py_file_button.grid(row=1, column=2, pady=15)
make_bat.grid(row=2, column=1)

# if program has been run before, autofill the location of python.exe
try:
    with open('python_exe_path', mode='r') as file:
        path = file.read()
        python_exe_strvar.set(path)
except FileNotFoundError:
    # program hasn't been run before
    # location of exe gets saved when making batch file
    pass

root.mainloop()
