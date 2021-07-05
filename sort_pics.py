from tkinter import *
import os
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime


root = Tk()
root.title('Sort Pictures')
root.geometry("500x150+300+200")
root.resizable(False, False)
root['bg'] = '#dae3df'


def choose_directory():
    dir_path = filedialog.askdirectory()
    enter_path.delete(0, END)
    enter_path.insert(0, dir_path)


def push_start():
    count_folders = 0
    count_files = 0
    cur_path = enter_path.get()
    if cur_path:
        for folder, subfolders, files in os.walk(cur_path):
            for file in files:
                path = os.path.join(folder, file)
                mtime = os.path.getmtime(path)
                date = datetime.fromtimestamp(mtime)
                date = date.strftime("%d.%m.%Y")
                date_folder = os.path.join(cur_path, date)
                if not os.path.exists(date_folder):
                    os.mkdir(date_folder)
                    count_folders += 1
                os.rename(path, os.path.join(date_folder, file))
                count_files += 1
        messagebox.showinfo('Success', f'Сортировка успешно выполнена\n\nСозданных папок: {count_folders}\n'
                                       f'Перемещённых файлов: {count_files}')
        enter_path.delete(0, END)
    else:
        messagebox.showwarning('Warning', 'Выберите папку с фото')


style_btn = ttk.Style()
style_btn.configure('My.TButton', font=("Arial", 15))

frame = Frame(root, bg="#a1aba6", bd=5)
frame.pack(pady=20, padx=10, fill=X)

enter_path = ttk.Entry(frame)
enter_path.pack(side=LEFT, ipady=2, expand=True, fill=X)

btn_dialog = ttk.Button(frame, text="Выбрать папку", command=choose_directory)
btn_dialog.pack(side=LEFT, padx=10)

btn_start = ttk.Button(root, text="Start", style="My.TButton", command=push_start)
btn_start.pack(fill=X, padx=10, pady=10)

root.mainloop()