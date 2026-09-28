import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("630x750")


def login(): 
    print("Test")


frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

#LOGO
logo_image = ctk.CTkImage(
    light_image=Image.open("assets/images/logo.png"),
    dark_image=Image.open("assets/images/logo.png"),
    size=(140, 32)
)

logo_label = ctk.CTkLabel(
    master=frame,
    image=logo_image,
    text=""
)
logo_label.pack(pady=(25, 5))

#LOGIN SYSTEM LABEL
label = ctk.CTkLabel(
    master=frame, text="Login System", 
    font=("Roboto", 40)
)
label.pack(pady=12, padx=10)

#USERNAME
entry1 = ctk.CTkEntry(
    master=frame, 
    placeholder_text="Username"
)
entry1.pack(pady=12, padx=10)

#PASSWORD
entry2 = ctk.CTkEntry(
    master=frame, 
    placeholder_text="Password", 
    show="*"
)
entry2.pack(pady=12, padx=10)

#REMEMBER ME CHECKBOX
checkbox = ctk.CTkCheckBox(
    master=frame, 
    text="Remember Me"
)
checkbox.pack(pady=12, padx=10)

#LOGIN BUTTON
button = ctk.CTkButton(
    master=frame, 
    text="Login", 
    command=login
)
button.pack(pady=1, padx=10)



root.mainloop()
