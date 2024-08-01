import tkinter as tk
from tkinter import *
import customtkinter as ctk



# Set up environment
root = ctk.CTk()
root.title("Trav's Directory Printer")
# root.iconbitmap("images/icon.ico")
root.geometry("600x450")



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
options_container = ctk.CTkFrame(column1_container)
options_container.grid(column=0, row=0, padx=10, pady=10 )

# label = ctk.CTkLabel(options_container, text="Options")
# label.grid(column=0, row=0)

# Buttons
btn_container = ctk.CTkFrame(column1_container)
btn_container.grid(column=0, row=1, pady=5)

open_dir_btn = ctk.CTkButton(btn_container, text="Open Directory")
open_dir_btn.grid(column=0, row=0,pady=5)

refresh_btn = ctk.CTkButton(btn_container, text="Refresh")
refresh_btn.grid(column=0, row=1, pady=5)

save_txt_btn = ctk.CTkButton(btn_container, text="Save txt File")
save_txt_btn.grid(column=0, row=2, pady=5)




root.mainloop()