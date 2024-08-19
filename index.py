import ftfy
import os
import zipfile
import shutil
import re
import sys
import tkinter as tk
from tkinter import filedialog

def process_zip(zip_path):
    zip_name = os.path.basename(zip_path).split('.')[0]

    if zipfile.is_zipfile(zip_path):
        script_path = os.path.dirname(os.path.realpath(sys.argv[0]))
        temp_dir = script_path + "/temp_unzip_files"

        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        os.mkdir(temp_dir)

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            for file_info in zip_ref.infolist():
                file_info.filename = ftfy.fix_text(file_info.filename)
                zip_ref.extract(file_info, temp_dir)

            if os.path.exists(temp_dir + '/' + zip_name):
                file_list = os.listdir(temp_dir + '/' + zip_name)
                file_list = [f for f in file_list if not f.startswith('.')]
            else:
                file_list = os.listdir(temp_dir)
                file_list = [f for f in file_list if not f.startswith('.')]
                file_list = [f for f in file_list if not f.startswith('__')]
                file_list = [f for f in file_list if not f.startswith('_')]

            for file in file_list:
                folder_for_file = re.sub(r'.*для ', '', file)
                folder_for_file = re.sub(r'\.pdf', '', folder_for_file)

                if not os.path.exists(script_path + '/' + folder_for_file):
                    os.mkdir(script_path + '/' + folder_for_file)

                if not os.path.exists(script_path + '/' + folder_for_file + '/' + file):
                    if os.path.exists(temp_dir + '/' + zip_name + '/'):
                        shutil.move(temp_dir + '/' + zip_name + '/' + file, script_path + '/' + folder_for_file + '/' + file)
                    else:
                        shutil.move(temp_dir + '/' + file, script_path + '/' + folder_for_file + '/' + file)
                else:
                    print("Этот файл уже существует:", file)

            shutil.rmtree(temp_dir)
            print("Обработано файлов:", len(file_list))
    else:
        print("Нужен файл архива с расширением .zip")

def process_folder(folder_path):
    script_path = os.path.dirname(os.path.realpath(sys.argv[0]))
    file_list = os.listdir(folder_path)
    file_list = [f for f in file_list if not f.startswith('.')]
    file_list = [f for f in file_list if not f.startswith('__')]
    file_list = [f for f in file_list if not f.startswith('_')]

    for file in file_list:
        folder_for_file = re.sub(r'.*для ', '', file)
        folder_for_file = re.sub(r'\.pdf', '', folder_for_file)

        if not os.path.exists(script_path + '/' + folder_for_file):
            os.mkdir(script_path + '/' + folder_for_file)

        if not os.path.exists(script_path + '/' + folder_for_file + '/' + file):
            shutil.move(folder_path + '/' + file, script_path + '/' + folder_for_file + '/' + file)
        else:
            print("Этот файл уже существует:", file)

    print("Обработано файлов:", len(file_list))

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("ZIP", "*.zip")])
    if file_path:
        process_zip(file_path)

def open_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        process_folder(folder_path)

if __name__ == "__main__":
    print('Запуск TRAKTOR 1.0 Автор: @coloritada. Несанкционированное копиирование файлов запрещено. 2024 ©')
    print('Рабочая директория: ', os.path.dirname(os.path.realpath(sys.argv[0])))

    root = tk.Tk()
    root.title("Фасовщик счетов на оплату")
    root.geometry("400x200")
    root.resizable(0, 0)

    frame = tk.Frame(root)
    frame.pack(expand=True)

    folder_button = tk.Button(frame, text="Папка с файлами", command=open_folder)
    zip_button = tk.Button(frame, text="Zip архив", command=open_file)

    folder_button.pack(in_=frame, side="left")
    zip_button.pack(in_=frame, side="left")

    root.mainloop()