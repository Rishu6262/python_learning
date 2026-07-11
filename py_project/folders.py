from pathlib import Path
import os

def create_folder():
    f_name=input("enter name : ")
    p=Path(f_name)
    p.mkdir()

def read_folder():
    p=Path("")
    item=list(p.rglob('*'))
    for i,v in enumerate(item):
        print(i+1,v)

def update_folder():
    read_folder()
    o_name=input("ente old name")  
    p=Path(o_name)
    if p.exists():
        n_name=input("enter new name :")    
        n_path=Path(n_name)
        print(f"{o_name} is changed to {n_name}")
    else:
        print("no such folder exists")

def delete_folder():
    read_folder()
    name=input("enter folder name to be deleted : ")
    p=Path(name)
    if p.exists():
        p.rmdir()
        print("folder deleted")
    else:
        print("no such folder exists")

def create_file():
    read_folder()
    f_name=input("enter name : ")
    p=Path(f_name)
    if p.exists():
        with open(f_name,'w') as fs:
            data=input("enter data : ")
            fs.write(data)
            print("file created and data added successfully")
    else:
        print("file exists")

def read_file():
    f_name=input("enter file name to be readed : ")
    p=Path(f_name)
    if p.exists() and p.is_file():
        with open(f_name,'r') as fs:
            print(fs.read())
    else:
        print("no such file exists!")

def update_file():
    f_name=input("enter name of your file :")
    p=Path(f_name)
    if p.exists() and p.is_file():
        print("press 1 for updating file name ")
        print("press 2 for appending file data ")
        print("press 3 for overwritting file data ")
        choice=int(input("your choice : "))
        if choice ==1:
            n_name=input("enter new name : ")
            n_path=Path(n_name)
            p.rename(n_path)
            print("name changed")
        if choice ==2:
            with open(f_name,'a') as fs:
                data=input("enter data : ")
                fs.write(" "+data)
                print("file created and data appended successfully")
        if choice ==3:
            with open(f_name,'w') as fs:
                data=input("enter data : ")
                fs.write(data)
                print("file created and data appended successfully")

def delete_file():
    read_file()
    name=input("enter file name to be deleted : ")
    p=Path(name)
    if p.exists():
        os.remove(p)
        print("file deleted")
    else:
        print("no such file exists")

def create_file_folder():
    read_folder()
    folder_name=input("enter folder name in which you want to create a file : ")
    file_name=input("entter file name : ")
    folder_path=Path(folder_name)
    if folder_path.exists() and folder_path.is_dir():
        file_path=folder_path/file_name
        if not file_path.exists():
            with open(file_path,'w') as fs:
                data=input("enter data : ")
                fs.write(data)
                print("file created and data appended successfully")
        else:
            print("file exists !")
    else:
        print("folder does not exist !")

def delete_file_folder():
    read_folder()
    name=input("enter folder name : ")
    file_name=input("enter file name : ")
    p=Path(name)/file_name
    if p.exists():
        os.remove(p)
        print("file deleted")
    else:
        print("no such file exists")

            

    
while True:
    print("press 0 to exit")
    print("press 1 for creating a folder")
    print("press 2 for reading a folder")
    print("press 3 for updating a folder")
    print("press 4 for deleting a folder")
    print("press 5 for creating a file")
    print("press 6 for reading a file")
    print("press 7 for updating a folder")
    print("press 8 for deleting a file")
    print("press 9 for creating a file in a folder")
    print("press 10 for deleting a file in a folder")

    check=int(input("please tell your Response : "))


    if check == 0:
        break
    if check == 1:
        create_folder()
    if check == 2:
        read_folder()
    if check == 3:
        update_folder()
    if check == 4:
        delete_folder()
    if check == 1:
        create_file()
    if check == 6:
        read_file()
    if check == 7:
        update_file()
    if check == 8:
        delete_file()
    if check == 9:
        create_file_folder()
    if check == 10:
        delete_file_folder()