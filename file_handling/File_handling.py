from pathlib import Path
import os

def createfolder():
    name=input("tell your folder name : ")
    p=Path(name)
    p.mkdir()
    print(f"{name} named folder is created successfully")

def readfolderandfile():
    path=Path('')
    items=list(path.rglob('*'))
    # count=1
    # for i in items:
    #     print(f"{count} : {i}")
    #     count+=1
    for i ,v in enumerate(items):# ek sath me values and key dono print kar sakte hai)
        print(i+1,v)#with the help of  enumerate 

def updatefolder():
    readfolderandfile()
    name=input("enter name of the folder you want to update the name : ")
    path=Path(name)
    if path.exists():
        new_name=input("enter new name : ")
        new_path=Path(new_name)
        path.rename(new_path)
        print("renamed successfully")
    else:
        print("this folder is not found")
    
def deletefolder():
    readfolderandfile()
    name=input("enter the name you folder you want to delete : ")
    path=Path(name)
    if path.exists():
        path.rmdir()
        print("folder deleted")

        # c=input("are you sure you want to delete y/n ?")
        # if c=='y':
        #     path.rmdir()
        # elif c=='n':
        #     return 
        # else:
        #     print("wrong response")



print("press 1 for creating a folder")
print("press 2 for reading a folder")
print("press 3 for updating a folder")
print("press 4 for deleting a folder")

check=int(input("please tell your Response : "))

if check == 1:
    createfolder()
if check == 2:
    readfolderandfile()
if check == 3:
    updatefolder()
if check == 4:
    deletefolder()
# ```````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
##  this file handling project is ui function add with chatgpt code
# import os
# from pathlib import Path
# import tkinter as tk
# from tkinter import messagebox, filedialog, ttk

# # ---------------------------- File & Folder Operations ----------------------------

# def create_folder_ui():
#     f_name = folder_name_entry.get().strip()
#     if not f_name:
#         messagebox.showwarning("Warning", "Please enter folder name")
#         return
#     p = Path(f_name)
#     try:
#         p.mkdir()
#         messagebox.showinfo("Success", f"Folder '{f_name}' created successfully!")
#         refresh_folder_list()
#     except FileExistsError:
#         messagebox.showerror("Error", "Folder already exists!")

# def read_folder_ui():
#     refresh_folder_list()
#     messagebox.showinfo("Info", "Folder list refreshed!")

# def update_folder_ui():
#     selected = folder_listbox.selection()
#     if not selected:
#         messagebox.showwarning("Warning", "Select a folder to rename!")
#         return
#     old_name = folder_listbox.item(selected, 'text')
#     new_name = folder_name_entry.get().strip()
#     if not new_name:
#         messagebox.showwarning("Warning", "Enter new name first!")
#         return
#     old_path = Path(old_name)
#     new_path = Path(new_name)
#     if old_path.exists():
#         old_path.rename(new_path)
#         messagebox.showinfo("Success", f"Folder renamed to '{new_name}'")
#         refresh_folder_list()
#     else:
#         messagebox.showerror("Error", "Folder does not exist!")

# def delete_folder_ui():
#     selected = folder_listbox.selection()
#     if not selected:
#         messagebox.showwarning("Warning", "Select a folder to delete!")
#         return
#     name = folder_listbox.item(selected, 'text')
#     p = Path(name)
#     if p.exists():
#         try:
#             p.rmdir()
#             messagebox.showinfo("Deleted", f"Folder '{name}' deleted successfully!")
#             refresh_folder_list()
#         except:
#             messagebox.showerror("Error", "Folder is not empty!")
#     else:
#         messagebox.showerror("Error", "No such folder exists!")

# def create_file_ui():
#     f_name = file_name_entry.get().strip()
#     data = file_data_entry.get("1.0", tk.END).strip()
#     if not f_name:
#         messagebox.showwarning("Warning", "Enter file name!")
#         return
#     p = Path(f_name)
#     if not p.exists():
#         with open(p, 'w') as fs:
#             fs.write(data)
#         messagebox.showinfo("Success", f"File '{f_name}' created successfully!")
#         refresh_folder_list()
#     else:
#         messagebox.showerror("Error", "File already exists!")

# def read_file_ui():
#     f_name = file_name_entry.get().strip()
#     p = Path(f_name)
#     if p.exists() and p.is_file():
#         with open(f_name, 'r') as fs:
#             file_data_entry.delete("1.0", tk.END)
#             file_data_entry.insert(tk.END, fs.read())
#         messagebox.showinfo("Success", f"Content of '{f_name}' loaded!")
#     else:
#         messagebox.showerror("Error", "File not found!")

# def delete_file_ui():
#     f_name = file_name_entry.get().strip()
#     p = Path(f_name)
#     if p.exists():
#         os.remove(p)
#         messagebox.showinfo("Deleted", f"File '{f_name}' deleted successfully!")
#         refresh_folder_list()
#     else:
#         messagebox.showerror("Error", "No such file exists!")

# # ---------------------------- Helper Functions ----------------------------

# def refresh_folder_list():
#     for item in folder_listbox.get_children():
#         folder_listbox.delete(item)
#     p = Path("")
#     items = list(p.rglob('*'))
#     for v in items:
#         folder_listbox.insert("", "end", text=str(v))

# # ---------------------------- GUI Design ----------------------------

# root = tk.Tk()
# root.title("📂 File & Folder Manager")
# root.geometry("950x600")
# root.configure(bg="black")

# # Title Label
# title_label = tk.Label(root, text="File & Folder Management System",
#                        bg="black", fg="white", font=("Arial", 18, "bold"))
# title_label.pack(pady=10)

# # ---------------------------- Folder Operations ----------------------------
# folder_frame = tk.LabelFrame(root, text="Folder Operations", bg="black", fg="cyan", font=("Arial", 12, "bold"))
# folder_frame.pack(fill="x", padx=10, pady=5)

# tk.Label(folder_frame, text="Folder Name:", bg="black", fg="white").grid(row=0, column=0, padx=5, pady=5)
# folder_name_entry = tk.Entry(folder_frame, width=30)
# folder_name_entry.grid(row=0, column=1, padx=5, pady=5)

# tk.Button(folder_frame, text="Create", command=create_folder_ui, bg="#00bfff", fg="black").grid(row=0, column=2, padx=5)
# tk.Button(folder_frame, text="Read", command=read_folder_ui, bg="#00bfff", fg="black").grid(row=0, column=3, padx=5)
# tk.Button(folder_frame, text="Update", command=update_folder_ui, bg="#00bfff", fg="black").grid(row=0, column=4, padx=5)
# tk.Button(folder_frame, text="Delete", command=delete_folder_ui, bg="#ff6347", fg="black").grid(row=0, column=5, padx=5)

# # ---------------------------- File Operations ----------------------------
# file_frame = tk.LabelFrame(root, text="File Operations", bg="black", fg="cyan", font=("Arial", 12, "bold"))
# file_frame.pack(fill="x", padx=10, pady=5)

# tk.Label(file_frame, text="File Name:", bg="black", fg="white").grid(row=0, column=0, padx=5, pady=5)
# file_name_entry = tk.Entry(file_frame, width=30)
# file_name_entry.grid(row=0, column=1, padx=5, pady=5)

# tk.Button(file_frame, text="Create", command=create_file_ui, bg="#00bfff", fg="black").grid(row=0, column=2, padx=5)
# tk.Button(file_frame, text="Read", command=read_file_ui, bg="#00bfff", fg="black").grid(row=0, column=3, padx=5)
# tk.Button(file_frame, text="Delete", command=delete_file_ui, bg="#ff6347", fg="black").grid(row=0, column=4, padx=5)

# tk.Label(file_frame, text="File Data:", bg="black", fg="white").grid(row=1, column=0, padx=5, pady=5)
# file_data_entry = tk.Text(file_frame, width=70, height=6)
# file_data_entry.grid(row=1, column=1, columnspan=4, padx=5, pady=5)

# # ---------------------------- Folder List ----------------------------
# folder_list_frame = tk.LabelFrame(root, text="All Files & Folders", bg="black", fg="cyan", font=("Arial", 12, "bold"))
# folder_list_frame.pack(fill="both", expand=True, padx=10, pady=5)

# folder_listbox = ttk.Treeview(folder_list_frame)
# folder_listbox.pack(fill="both", expand=True)

# # ---------------------------- Start GUI ----------------------------
# refresh_folder_list()
# root.mainloop()

# ````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
# from pathlib import Path
# import os

# def create_folder():
#     f_name=input("enter name : ")
#     p=Path(f_name)
#     p.mkdir()

# def read_folder():
#     p=Path("")
#     item=list(p.rglob('*'))
#     for i,v in enumerate(item):
#         print(i+1,v)

# def update_folder():
#     read_folder()
#     o_name=input("ente old name")  
#     p=Path(o_name)
#     if p.exists():
#         n_name=input("enter new name :")    
#         n_path=Path(n_name)
#         print(f"{o_name} is changed to {n_name}")
#     else:
#         print("no such folder exists")

# def delete_folder():
#     read_folder()
#     name=input("enter folder name to be deleted : ")
#     p=Path(name)
#     if p.exists():
#         p.rmdir()
#         print("folder deleted")
#     else:
#         print("no such folder exists")

# def create_file():
#     read_folder()
#     f_name=input("enter name : ")
#     p=Path(f_name)
#     if p.exists():
#         with open(f_name,'w') as fs:
#             data=input("enter data : ")
#             fs.write(data)
#             print("file created and data added successfully")
#     else:
#         print("file exists")

# def read_file():
#     f_name=input("enter file name to be readed : ")
#     p=Path(f_name)
#     if p.exists() and p.is_file():
#         with open(f_name,'r') as fs:
#             print(fs.read())
#     else:
#         print("no such file exists!")

# def update_file():
#     f_name=input("enter name of your file :")
#     p=Path(f_name)
#     if p.exists() and p.is_file():
#         print("press 1 for updating file name ")
#         print("press 2 for appending file data ")
#         print("press 3 for overwritting file data ")
#         choice=int(input("your choice : "))
#         if choice ==1:
#             n_name=input("enter new name : ")
#             n_path=Path(n_name)
#             p.rename(n_path)
#             print("name changed")
#         if choice ==2:
#             with open(f_name,'a') as fs:
#                 data=input("enter data : ")
#                 fs.write(" "+data)
#                 print("file created and data appended successfully")
#         if choice ==3:
#             with open(f_name,'w') as fs:
#                 data=input("enter data : ")
#                 fs.write(data)
#                 print("file created and data appended successfully")

# def delete_file():
#     read_file()
#     name=input("enter file name to be deleted : ")
#     p=Path(name)
#     if p.exists():
#         os.remove(p)
#         print("file deleted")
#     else:
#         print("no such file exists")

# def create_file_folder():
#     read_folder()
#     folder_name=input("enter folder name in which you want to create a file : ")
#     file_name=input("entter file name : ")
#     folder_path=Path(folder_name)
#     if folder_path.exists() and folder_path.is_dir():
#         file_path=folder_path/file_name
#         if not file_path.exists():
#             with open(file_path,'w') as fs:
#                 data=input("enter data : ")
#                 fs.write(data)
#                 print("file created and data appended successfully")
#         else:
#             print("file exists !")
#     else:
#         print("folder does not exist !")

# def delete_file_folder():
#     read_folder()
#     name=input("enter folder name : ")
#     file_name=input("enter file name : ")
#     p=Path(name)/file_name
#     if p.exists():
#         os.remove(p)
#         print("file deleted")
#     else:
#         print("no such file exists")

            

    
# while True:
#     print("press 0 to exit")
#     print("press 1 for creating a folder")
#     print("press 2 for reading a folder")
#     print("press 3 for updating a folder")
#     print("press 4 for deleting a folder")
#     print("press 5 for creating a file")
#     print("press 6 for reading a file")
#     print("press 7 for updating a folder")
#     print("press 8 for deleting a file")
#     print("press 9 for creating a file in a folder")
#     print("press 10 for deleting a file in a folder")

#     check=int(input("please tell your Response : "))


#     if check == 0:
#         break
#     if check == 1:
#         create_folder()
#     if check == 2:
#         read_folder()
#     if check == 3:
#         update_folder()
#     if check == 4:
#         delete_folder()
#     if check == 1:
#         create_file()
#     if check == 6:
#         read_file()
#     if check == 7:
#         update_file()
#     if check == 8:
#         delete_file()
#     if check == 9:
#         create_file_folder()
#     if check == 10:
#         delete_file_folder()

