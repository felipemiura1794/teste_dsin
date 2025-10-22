import customtkinter 
from css import *
from PIL import Image
# --- Imports ---

# --- Program appearance ---
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x874")

def login():
    print("Test")

# =================== MAIN FRAME ===================
# --- Main frame ---
frame = customtkinter.CTkFrame(
    master=root,
    fg_color = "#000000",
    corner_radius = 0
    )
frame.pack(pady = 20, padx = 60, fill = "both", expand = True)

# ==================== TEXTO TELA ====================
# --- Login label ---
label = customtkinter.CTkLabel(
    master = frame,
    text = "BOTOES DE \nTESTE ATAQUE", 
    font = ("Georgia", 27),
    text_color = "#FFFFFF"
    )
label.pack(pady = (30, 15), padx = 55)

# --- Description ---
subtitle = customtkinter.CTkLabel(
    master = frame,
    text = "O que você deseja fazer?",
    **DESCRIPTION_STYLE
)
subtitle.pack(pady = (10, 15), padx = 20)

# ============== BOTOES TELA TESTE ==============
# --- Funções ---

def atacar():
    add_message("vc atacou !!")
    
def defender():
    add_message("vc defendeu !!")
    
def nada():
    add_message("vc nao fez nada !!!!!!!!!!!!!!!!!!!!!")

def add_message(text):
    output_box.insert("end", text + "\n")
    output_box.see("end")

# --- Buttons Frame ---
signup_frame = customtkinter.CTkFrame(
    master = frame,
    fg_color="transparent"
)
signup_frame.pack(pady=30)

# --- Output box ---
output_box = customtkinter.CTkTextbox(
    master=frame,
    width=380,
    height=200,
    font=("Arial", 12),
    fg_color="#1A1A1A",
    text_color="#FFFFFF"
)
output_box.pack(pady=20, padx=20)

# --- button 1 ---
button1 = customtkinter.CTkButton(
    master = signup_frame,
    text = "Atacar",
    command = atacar,
    font=("Arial", 12),
    width = 120
    )
button1.grid(row=0, column=0, padx=5, pady=20)

# --- button 2 ---
button2 = customtkinter.CTkButton(
    master = signup_frame,
    text = "Defender",
    command = defender,
    font=("Arial", 12),
    width = 120
    )
button2.grid(row=0, column=1, padx=5, pady=20)

# --- button 3 ---
button3 = customtkinter.CTkButton(
    master = signup_frame,
    text = "Nada",
    command = nada,
    font=("Arial", 12),
    width = 120
    )
button3.grid(row=0, column=2, padx=5, pady=20)

root.mainloop()
