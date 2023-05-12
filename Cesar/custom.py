from tkinter import *
import tkinter as tk
import cesar
import os
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.scrolledtext import ScrolledText
import customtkinter
import pyperclip
import cryptopicture

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

ces = cesar.Cesar()
crypto_picture = cryptopicture.Picture()
window = customtkinter.CTk()
window.title("Cryptography")  
window.geometry("1100x600")

font=customtkinter.CTkFont(size=15, weight="bold")

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "")
logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CP.png")), size=(26, 26))
cesar_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "cesar.png")), size=(26, 26))

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

navigation_frame = customtkinter.CTkFrame(window, corner_radius=0)
navigation_frame.grid(row=0, column=0, sticky="nsew")
navigation_frame.grid_rowconfigure(4, weight=10)

navigation_frame_label = customtkinter.CTkLabel(navigation_frame, text="  Cryptography", compound="left", font=customtkinter.CTkFont(size=15, weight="bold"), image=logo_image)
navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

home_frame = customtkinter.CTkFrame(window, corner_radius=0, fg_color="transparent")
home_frame.grid_columnconfigure(0, weight=1)
second_frame = customtkinter.CTkFrame(window, corner_radius=0, fg_color="transparent")
third_frame = customtkinter.CTkFrame(window, corner_radius=0, fg_color="transparent")


def home_button_event():
    select_frame_by_name("home")

def frame_2_button_event():
    select_frame_by_name("frame_2")

def frame_3_button_event():
    select_frame_by_name("frame_3")


home_button = customtkinter.CTkButton(navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Cesar",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w", command=home_button_event, image=cesar_image)
home_button.grid(row=1, column=0, sticky="ew")

frame_2_button = customtkinter.CTkButton(navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Encrypt in picture",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=frame_2_button_event)
frame_2_button.grid(row=2, column=0, sticky="ew")

frame_3_button = customtkinter.CTkButton(navigation_frame, corner_radius=0, height=40, border_spacing=10, text="SSH",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=frame_3_button_event)
frame_3_button.grid(row=3, column=0, sticky="ew")

def encrypting():
    textbox2.delete("0.0", "end")
    txt = textbox1.get("1.0", END)
    enc = ces.encryption(txt)
    textbox2.insert("0.0", enc)

def open_picture():
    picture = customtkinter.filedialog.askopenfilename()
    picture_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, picture)), size=(600, 300))
    picture_label = customtkinter.CTkLabel(tabview.tab("Encrypt"), image=picture_image, text="")
    picture_label.grid()
    picture_entry.grid(sticky="nsew")
    return picture


def encrypt_picture():
    enc = picture_entry.get()
    crypto_picture.stega_encrypt(open_picture(), enc)

def decrypting():
    textbox2.delete("0.0", "end")
    txt = textbox1.get("1.0", END)
    enc = ces.decryption(txt)
    textbox2.insert("0.0", enc)

def copy_to_clipboard1():
    txt = textbox1.get("1.0", END)
    pyperclip.copy(txt)

def copy_to_clipboard2():
    txt = textbox2.get("1.0", END)
    pyperclip.copy(txt)

def paste_to_clipboard():
    textbox1.delete("0.0", "end")
    # q = window.clipboard_get()
    textbox1.insert("0.0", pyperclip.paste())

def clear_to_clipboard():
    textbox1.delete("0.0", "end")
    textbox2.delete("0.0", "end")

def select_frame_by_name(name):
    # set button color for selected button
    home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
    frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
    frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

    if name == "home":
        home_frame.grid(row=0, column=1, sticky="n")
    else:
        home_frame.grid_forget()
    if name == "frame_2":
        second_frame.grid(row=0, column=1, sticky="nsew")
    else:
        second_frame.grid_forget()
    if name == "frame_3":
        third_frame.grid(row=0, column=1, sticky="nsew")
    else:
        third_frame.grid_forget()

select_frame_by_name("home")

def change_appearance_mode_event(new_appearance_mode):
    customtkinter.set_appearance_mode(new_appearance_mode)

textbox1 = customtkinter.CTkTextbox(home_frame, width=1500, height=220)
textbox1.grid(padx=(20, 20), pady=(10, 0))

label1 = customtkinter.CTkLabel(home_frame, compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
label1.grid(row=1, column=0, padx=20, sticky="w")

encr = customtkinter.CTkButton(label1, text="Encrypt", width=150, height=50, corner_radius=20, command=encrypting)
encr.grid(row=0, column=0, padx=(0, 20), pady=(10, 0))

decr = customtkinter.CTkButton(label1, text="Decipher", fg_color="#800000", hover_color="#A52A2A", width=150, height=50, corner_radius=20, command=decrypting)
decr.grid(row=0, column=1, padx=(0, 20), pady=(10, 0))

label1_5 = customtkinter.CTkLabel(home_frame, text="", compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
label1_5.grid(row=1, column=0, padx=20, sticky="e")

copy1 = customtkinter.CTkButton(label1_5, text="Copy", width=50, fg_color="#2F4F4F", hover_color="#696969", height=30, corner_radius=0, command=copy_to_clipboard1)
copy1.grid(row=0, column=2, padx=(0, 0), pady=(0, 0))

paste1 = customtkinter.CTkButton(label1_5, text="Paste", fg_color="#2F4F4F", hover_color="#696969", width=50, height=30, corner_radius=0, command=paste_to_clipboard)
paste1.grid(row=0, column=3, padx=(0, 0), pady=(0, 0))

textbox2 = customtkinter.CTkTextbox(home_frame, width=1500, height=250)
textbox2.grid(padx=(20, 20), pady=(10, 0))

label2 = customtkinter.CTkLabel(home_frame, text="", compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
label2.grid(row=3, column=0, padx=20, sticky="e")

copy2 = customtkinter.CTkButton(label2, text="Copy", width=50, fg_color="#2F4F4F", hover_color="#696969", height=30, corner_radius=0, command=copy_to_clipboard2)
copy2.grid(row=0, column=0, padx=(0, 0), pady=(10, 0))

clear = customtkinter.CTkButton(label2, text="Clear", width=50, fg_color="#800000", hover_color="#696969", height=30, corner_radius=0, command=clear_to_clipboard)
clear.grid(row=0, column=1, padx=(0, 0), pady=(10, 0))

tabview = customtkinter.CTkTabview(second_frame, width=875, height=850)
tabview.pack(fill=X, padx=(20, 20), pady=(10, 20))
tabview.add("Encrypt")
tabview.add("Decrypt")
tabview.tab("Encrypt").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
tabview.tab("Decrypt").grid_columnconfigure(0, weight=1)

open_pic = customtkinter.CTkButton(tabview.tab("Encrypt"), text="Open File", fg_color="#2F4F4F", hover_color="#696969", width=50, height=30, corner_radius=0, command=open_picture)
open_pic.grid(row=0, column=0, padx=(10, 0), pady=(0, 0), sticky="n")

picture_label = customtkinter.CTkLabel(tabview.tab("Encrypt"), text="")
picture_entry = customtkinter.CTkEntry(tabview.tab("Encrypt"), placeholder_text="Encrypt word or sentinces")

enc = customtkinter.CTkButton(tabview.tab("Encrypt"), text="Encrypt", fg_color="#2F4F4F", hover_color="#696969", width=50, height=30, corner_radius=0, command=encrypt_picture)
enc.grid(row=0, column=1, padx=(10, 0), pady=(0, 0), sticky="s")

# optionmenu_1 = customtkinter.CTkOptionMenu(navigation_frame, dynamic_resizing=False,
#                                                         values=["Dark", "Light"], command=change_appearance_mode_event)

# optionmenu_1.grid(row=5, column=0, padx=20, pady=(20, 10))

window.mainloop()