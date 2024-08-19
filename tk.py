import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog, PhotoImage

root = tk.Tk()
root.title("Фасовщик счетов на оплату")
root.geometry("400x200")
root.resizable(0, 0)

def open_file():
    file_path = tk.filedialog.askopenfilename(filetypes=[("ZIP", "*.zip")])
    print(file_path)
def open_folder():
    folder_path = tk.filedialog.askdirectory()
    print(folder_path)

frame = tk.Frame(root)
frame.pack(expand=True)

folder_img = tk.PhotoImage(file="folder_icon.png").subsample(5)
zip_img = tk.PhotoImage(file="zip_icon.png").subsample(5)

folder_button = tk.Button(frame, image=folder_img, command=open_folder, text="Папка с файлами", compound="top")
zip_button = tk.Button(frame, image=zip_img, command=open_file, text="Zip архив", compound="top")

folder_button.pack(in_=frame, side="left")
zip_button.pack(in_=frame, side="left")

root.mainloop()