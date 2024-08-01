import tkinter as tk
from tkinter import *
from tkinter import filedialog
import customtkinter as ctk
import os
import re

# Set up environment
root = ctk.CTk()
root.title("Trav's Directory Printer")

# Window size and position
window_width = 600
window_height = 450

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

# root.iconbitmap("images/icon.ico")
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")


# Global Variables
cur_dir = os.getcwd()




# Functions

def open_dir():
	global cur_dir
	cur_dir = filedialog.askdirectory(initialdir=cur_dir)
	cur_dir = os.path.normpath(cur_dir)	
	get_file_list()


def get_file_list():
	global cur_dir
	file_list = []
	dir_list = []
	root.title(f"Directory Printer:  {cur_dir}")
	file_types_list = get_file_types()
	for file in os.listdir(cur_dir):
		file_path = os.path.join(cur_dir, file)
		if os.path.isfile(file_path):
            # Get the file extension
			_, ext = os.path.splitext(file)
			ext = ext[1:].lower()  # Remove the dot and convert to lowercase
            
			if not file_types_list or ext in file_types_list:
				file_list.append(file)
		
		if os.path.isdir(os.path.join(cur_dir, file)):
			dir = f"[{file}]"
			dir_list.append(dir)


	list_files(file_list, dir_list)




def list_files(file_list, dir_list):
	global cur_dir
	file_text.delete("1.0", ctk.END)

	list_files = "\n".join(file_list)
	list_dirs = "\n".join(dir_list)

	get_file_types()

	if include_path_status.get() == "on":
		file_text.insert(ctk.END, f"{cur_dir}\n\n")
	
	if include_directories_status.get() == "on":
		file_text.insert(ctk.END, list_dirs)
		file_text.insert(ctk.END, "\n\n")
	
	file_text.insert(ctk.END, list_files)

	
		
def save_txt():
	global cur_dir

	file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        title="Save As"
    )
    
	if file_path:
        # Write the content of the textbox to the selected file
		with open(file_path, 'w') as file:
			file.write(file_text.get("1.0", ctk.END))

def get_file_types():
	file_types_str = file_types.get()
	file_types_str = file_types_str.replace('.', '').replace('*', '')

	file_types_list = [file_type.strip() for file_type in re.split(r'[,\s]+', file_types_str) if file_type]

	return file_types_list





#################################################
#  GUI LAYOUT
#################################################

# Colors
ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green


background_color = "#525252"
background_textbox_color = "#ff9933"
text_color = "black"

btn_color = "#f0f0f0"
btn_text_color = "black"
btn_highlight_color = "#96d3e2"
btn_highlight_text_color = "black"


# Styling

cb_width = 20
cb_height = 20
cb_radius = 10
cb_border = 2

section_title = ("Helvetica", 14, "bold")


# ===  Layout  ===

# Columns
column0_container = ctk.CTkFrame(root, height=200, border_width=1)
column0_container.grid(column=0, row=0, padx=10, pady=10, sticky="nsew")

column1_container = ctk.CTkFrame(root, height=200, border_width=1)
column1_container.grid(column=1, row=0, padx=10, pady=10, sticky="nsew")

# Configure grid weights for the root to allow columns to resize
root.grid_columnconfigure(0, weight=1)
# root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

# Configure grid weights for column0_container to allow the text box to resize
column0_container.grid_columnconfigure(0, weight=1)
column0_container.grid_rowconfigure(0, weight=1)

# column1_container.grid_columnconfigure(0, weight=1)
# column1_container.grid_rowconfigure(0, weight=1)



# Text Box
file_text = ctk.CTkTextbox(column0_container)
file_text.grid(column=0, row=0, padx=10, pady=10, sticky="nsew")



# Options
options_container = ctk.CTkFrame(column1_container, height=250, border_width=1)
options_container.grid(column=0, row=0, padx=10, pady=10, sticky="nsew")

options_container.grid_columnconfigure(0, weight=1)
options_container.grid_rowconfigure(0, weight=1)

label = ctk.CTkLabel(options_container, text="Options", font=section_title)
label.grid(column=0, row=0, sticky="w", padx=5, pady=10)

include_path_status = ctk.StringVar(value="off")
include_path = ctk.CTkCheckBox(options_container, text="Include file path?", variable=include_path_status, onvalue="on", offvalue="off",
							   border_width=cb_border, checkbox_height=cb_height, checkbox_width=cb_width, corner_radius=cb_radius)
include_path.grid(column=0, row=5, padx=(15,5), pady=0, sticky=W)

include_directories_status = ctk.StringVar(value="off")
include_directories = ctk.CTkCheckBox(options_container, text="Include directories?", variable=include_directories_status, onvalue="on", offvalue="off",
									border_width=cb_border, checkbox_height=cb_height, checkbox_width=cb_width, corner_radius=cb_radius)
include_directories.grid(column=0, row=10, padx=(15,5), pady=(0,15), sticky=W)

file_types = ctk.CTkEntry(options_container, placeholder_text="All Files Types")
file_types.grid (column=0, row=2, padx=(15,5), pady=(0,15), sticky=W)



# Buttons
btn_container = ctk.CTkFrame(column1_container)
btn_container.grid(column=0, row=1, pady=5)

open_dir_btn = ctk.CTkButton(btn_container, text="Open Directory", command=open_dir)
open_dir_btn.grid(column=0, row=0,pady=5)

refresh_btn = ctk.CTkButton(btn_container, text="Refresh", command=get_file_list)
refresh_btn.grid(column=0, row=1, pady=5)

save_txt_btn = ctk.CTkButton(btn_container, text="Save txt File", command=save_txt)
save_txt_btn.grid(column=0, row=2, pady=5)




root.mainloop()