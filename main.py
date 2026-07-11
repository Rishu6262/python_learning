from pathlib import Path
import os
#CRUD

def create_folder():
    folder_name = input("enter your folder name: ")
    p = Path(folder_name)
    p.mkdir()


def read_folder():
    p = Path("")
    items = list(p.rglob('*'))
    for i , v in enumerate(items):
        print(i+1,v)


def update_folder():
    read_folder()
    old_name = input("Enter folder name to be changed: ")
    p = Path(old_name)
    if p.exists():
        new_name = input("enter new name for your folder: ")
        new_path = Path(new_name)
        p.rename(new_path)
        print(f"{old_name} is changed to {new_name}")
    else:
        print("No such foler exists")

def delete_folder():
    read_folder()
    name = input("Enter folder name to be deleted: ")
    p = Path(name)
    if p.exists():
        p.rmdir()
        print("Folder Deleted")





#FILE - CRUD
def create_file():
    read_folder()
    file_name = input("Enter your file name: ")
    p = Path(file_name)
    if not p.exists():
        with open(file_name,'w') as fs:
            data = input("Enter your data: ")
            fs.write(data)
            print("File created and data added successfully")
    else:
        print("File already exists!")

def read_file():
    file_name = input("Enter file name to be readed: ")
    p = Path(file_name)
    if p.exists() and p.is_file():
        with open(file_name,'r') as fs:
            print(fs.read())
    else:
        print("No such file exists!")


def update_file():
    file_name = input("Enter your file name to be updated: ")
    p = Path(file_name)
    if p.exists() and p.is_file():
        print("Press 1 for Updating file name")
        print("Press 2 for Appending data")
        print("Print 3 for Overwriting data")
        choice = int(input("Your Choice: "))

        if choice ==1:
            new_name = input("Enter new name: ")
            new_path = Path(new_name)
            p.rename(new_path)
            print("File name changed...")
        
        if choice == 2:
            with open(file_name,"a") as fs:
                data = input("Enter data to be appende: ")
                fs.write(" "+data)
                print("Data appended successfully...")
        if choice == 3:
            with open(file_name,"w") as fs:
                data = input("Enter data to be Overwrite: ")
                fs.write(data)
                print("Data Overwriteded successfully...")  




def delete_file():
    read_folder()
    file_name = input("Enter file name to be deleted: ")
    p = Path(file_name)
    if p.exists() and p.is_file():
        os.remove(p)
        print("File deleted successfully")
    else:
        print("File not exists!")

def createfile_folder():
    read_folder()
    folder_name = input("Enter the name of folder: ")
    file_name = input("Enter file name")

    folder_path = Path(folder_name)
    if folder_path.exists() and folder_path.is_dir():
        file_path = folder_path/file_name
        if not file_path.exists():
            with open(file_path,'w') as fs:
                data = input("Enter your data: ")
                fs.write(data)
                print("File created successfully")
        else:
            print("File already exists!")
    else:
        print("folder does not exists")



def deletefile_folder():
    read_folder()
    folder_name = input("Enter the name of folder: ")
    file_name = input("Enter file name")

    file_path = Path(folder_name)/file_name
    if file_path.exists() and file_path.is_file():
        os.remove(file_path)
        print("File deleted successfully")
    else:
        print("No such file exists!")




while True:
    print("Press 1 for creating folder: ")
    print("Press 2 for reading folder: ")
    print("Press 3 for Updating folder name: ")
    print("Press 4 for deleteing folder: ")
    print("Press 5  for Creating file: ")
    print("Press 6  for Reading file: ")
    print("Press 7  for Updating file: ")
    print("Press 8 for deleting  file: ")
    print("Press 9 for creating a file inside a folder: ")
    print("Press 10 for deleting a file from folder:")
    print("Press 0 for Exiting.")
    choice = int(input(("Your choice: ")))

    if choice == 1:
        create_folder()

    if choice == 2:
        read_folder()

    if choice == 3:
        update_folder()

    if choice == 4:
        delete_folder()
    
    if choice == 5:
        create_file()
    
    if choice == 6:
        read_file()

    if choice == 7:
        update_file()
    
    if choice == 8:
        delete_file()
    
    if choice == 9:
        createfile_folder()

    if choice == 10:
        deletefile_folder()

    if choice == 0:
        print("Exiting...")
        break

















