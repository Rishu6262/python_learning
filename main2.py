import streamlit as st
from pathlib import Path
import os

st.set_page_config(page_title="📁 File & Folder Manager", layout="centered")
st.title("📁 File & Folder Manager")
st.markdown("---")

# Show all files and folders
def show_directory():
    st.subheader("📂 Current Directory Structure")
    p = Path("")
    items = list(p.rglob("*"))
    for i, item in enumerate(items, 1):
        st.text(f"{i}. {item}")

# --- Folder Functions ---
def create_folder_ui():
    folder_name = st.text_input("Enter folder name to create:")
    if st.button("Create Folder"):
        p = Path(folder_name)
        if not p.exists():
            p.mkdir()
            st.success(f"Folder '{folder_name}' created!")
        else:
            st.warning("Folder already exists!")

def update_folder_ui():
    show_directory()
    old_name = st.text_input("Enter current folder name:")
    new_name = st.text_input("Enter new folder name:")
    if st.button("Rename Folder"):
        p = Path(old_name)
        if p.exists() and p.is_dir():
            p.rename(new_name)
            st.success(f"Folder renamed to '{new_name}'")
        else:
            st.error("Folder not found!")

def delete_folder_ui():
    show_directory()
    folder_name = st.text_input("Enter folder name to delete:")
    if st.button("Delete Folder"):
        p = Path(folder_name)
        if p.exists() and p.is_dir():
            try:
                p.rmdir()
                st.success("Folder deleted!")
            except:
                st.error("Folder is not empty!")
        else:
            st.error("Folder not found!")

# --- File Functions ---
def create_file_ui():
    show_directory()
    file_name = st.text_input("Enter file name:")
    content = st.text_area("Enter content for the file:")
    if st.button("Create File"):
        p = Path(file_name)
        if not p.exists():
            with open(p, "w") as f:
                f.write(content)
            st.success("File created and content added!")
        else:
            st.warning("File already exists!")

def read_file_ui():
    file_name = st.text_input("Enter file name to read:")
    if st.button("Read File"):
        p = Path(file_name)
        if p.exists() and p.is_file():
            with open(p, "r") as f:
                st.code(f.read())
        else:
            st.error("File not found!")

def update_file_ui():
    file_name = st.text_input("Enter file name to update:")
    choice = st.radio("Choose operation", ["Rename", "Append Data", "Overwrite Data"])
    if choice == "Rename":
        new_name = st.text_input("Enter new file name:")
        if st.button("Rename File"):
            p = Path(file_name)
            if p.exists():
                p.rename(new_name)
                st.success("File renamed successfully")
            else:
                st.error("File not found!")
    elif choice == "Append Data":
        data = st.text_area("Enter data to append:")
        if st.button("Append"):
            with open(file_name, "a") as f:
                f.write(" " + data)
            st.success("Data appended!")
    elif choice == "Overwrite Data":
        data = st.text_area("Enter data to overwrite:")
        if st.button("Overwrite"):
            with open(file_name, "w") as f:
                f.write(data)
            st.success("File overwritten!")

def delete_file_ui():
    show_directory()
    file_name = st.text_input("Enter file name to delete:")
    if st.button("Delete File"):
        p = Path(file_name)
        if p.exists() and p.is_file():
            os.remove(p)
            st.success("File deleted!")
        else:
            st.error("File not found!")

# --- File Inside Folder ---
def create_file_in_folder_ui():
    show_directory()
    folder_name = st.text_input("Enter folder name:")
    file_name = st.text_input("Enter file name:")
    data = st.text_area("Enter data:")
    if st.button("Create File in Folder"):
        folder_path = Path(folder_name)
        if folder_path.exists() and folder_path.is_dir():
            file_path = folder_path / file_name
            if not file_path.exists():
                with open(file_path, 'w') as f:
                    f.write(data)
                st.success("File created inside folder!")
            else:
                st.warning("File already exists in folder!")
        else:
            st.error("Folder does not exist!")

def delete_file_in_folder_ui():
    show_directory()
    folder_name = st.text_input("Enter folder name:")
    file_name = st.text_input("Enter file name inside folder to delete:")
    if st.button("Delete File from Folder"):
        file_path = Path(folder_name) / file_name
        if file_path.exists():
            os.remove(file_path)
            st.success("File deleted!")
        else:
            st.error("File not found!")

# --- Sidebar Navigation ---
menu = [
    "📁 Create Folder",
    "🔍 Read Directory",
    "✏️ Rename Folder",
    "🗑️ Delete Folder",
    "📄 Create File",
    "📖 Read File",
    "📝 Update File",
    "🗑️ Delete File",
    "📂 Create File in Folder",
    "❌ Delete File from Folder"
]

choice = st.sidebar.selectbox("Select Action", menu)

if choice == "📁 Create Folder":
    create_folder_ui()
elif choice == "🔍 Read Directory":
    show_directory()
elif choice == "✏️ Rename Folder":
    update_folder_ui()
elif choice == "🗑️ Delete Folder":
    delete_folder_ui()
elif choice == "📄 Create File":
    create_file_ui()
elif choice == "📖 Read File":
    read_file_ui()
elif choice == "📝 Update File":
    update_file_ui()
elif choice == "🗑️ Delete File":
    delete_file_ui()
elif choice == "📂 Create File in Folder":
    create_file_in_folder_ui()
elif choice == "❌ Delete File from Folder":
    delete_file_in_folder_ui()
