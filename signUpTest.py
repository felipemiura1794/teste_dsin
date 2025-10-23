import customtkinter 
from css import *
from PIL import Image
# --- Imports ---

# --- Program appearance ---
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x810")
root.resizable(False, False)
radio_var = customtkinter.IntVar(value=0)

def login():
    print("Test")

# =================== MAIN FRAME ===================
# --- Main frame ---
frame = customtkinter.CTkFrame(
    master=root,
    fg_color = "#357E94",
    corner_radius = 0
    )
frame.pack(pady = 20, padx = 60, fill = "both", expand = True)
frame.pack_propagate(False)

# ==================== LOGO IMAGE ====================
try:
    logo_image = customtkinter.CTkImage(
        light_image = Image.open("duck.png"),
        dark_image = Image.open("duck.png"),
        size = (60, 60)
    )

    image_label = customtkinter.CTkLabel(
        master = frame,
        image = logo_image,
        text = "",
    )
    image_label.pack(pady = (50, 10), anchor = "w", padx = 20)

except:
    pass

# ==================== LOGIN SECTION ====================
# --- Login label ---
label = customtkinter.CTkLabel(
    master = frame,
    text = "Cadastre-se", 
    font = ("Georgia", 27),
    text_color = "#FFFFFF"
    )
label.pack(pady = (30, 15), anchor = "w", padx = 50)

# --- Description ---
subtitle = customtkinter.CTkLabel(
    master = frame,
    text = "Te garanto que esse é o melhor (e, \n por enquanto, único) sistema de \n controle de patos que você vai encontrar!",
    **DESCRIPTION_STYLE
)
subtitle.pack(pady = (10, 15), padx = 30)

# --- Input "Username" ---
entry1 = customtkinter.CTkEntry( 
    master = frame, 
    placeholder_text = "Email",
    **ENTRY_STYLE
    )
entry1.pack(pady = (12, 5), padx = 40)

# --- Username line ---
line1 = customtkinter.CTkFrame(
    master = frame,
    **LINES_STYLES
)
line1.pack(padx = 40,  fill = "x")

# --- Input "Email" ---
entry2 = customtkinter.CTkEntry( 
    master = frame, 
    placeholder_text = "Nome",
    **ENTRY_STYLE
    )
entry2.pack(pady = (12, 5), padx = 40)

# --- Email line ---
line2 = customtkinter.CTkFrame(
    master = frame,
    **LINES_STYLES
)
line2.pack(padx = 40,  fill = "x")

# --- Input "Password" ---
entry3 = customtkinter.CTkEntry( 
    master = frame, 
    placeholder_text = "Senha", 
    show = "*",
    **ENTRY_STYLE
    )
entry3.pack(pady = (20, 5), padx = 40)

# --- Password line ---
line3 = customtkinter.CTkFrame(
    master = frame,
    **LINES_STYLES
)
line3.pack(padx = 40,  fill = "x")

# ==================== BOTÕES RADIO E BOTÃO CADASTRAR ====================
# --- Frame dos radios ---
radioFrame = customtkinter.CTkFrame(
    master = frame,
    fg_color = "transparent",    
)
radioFrame.pack(pady=20, padx=25, fill="x")

# --- Primeiro botão radio ---
coderCB = customtkinter.CTkRadioButton(
    master = radioFrame,
    **RADIO_BUTTON_STYLE,
    text = "Coder", 
    variable=radio_var,
    value = 1
)
coderCB.grid(row = 1, column = 0, padx = (25, 0), pady = (0, 20), sticky = "w")

# --- Segundo botão radio ---
dsinmerCB = customtkinter.CTkRadioButton(
    master = radioFrame,
    **RADIO_BUTTON_STYLE,
    text = "DSINmer",
    variable=radio_var,  
    value = 2
)
dsinmerCB.grid(row = 1, column = 1,padx = (0, 15), pady = (0, 20), sticky = "w")

# --- Terceiro botão radio ---
patoCB = customtkinter.CTkRadioButton(
    master = radioFrame,    
    **RADIO_BUTTON_STYLE,
    text = "Pato",
    variable=radio_var,
    value = 3
)
patoCB.grid(row = 1, column = 2, pady = (0, 20), sticky = "w")

# --- Botão login ---
log_button = customtkinter.CTkButton (
    master = frame, 
    text = "Cadastrar",
    **LOG_BUTTON_STYLE
    )
log_button.pack(pady = (12, 0), padx = 10)

# ============== JÁ TEM UMA CONTA ==============
# --- Frame já possui conta ---
signup_frame = customtkinter.CTkFrame(
    master = frame,
    fg_color="transparent"
)
signup_frame.pack(pady=(10, 0))

# --- Já tem uma conta 1 ---
na_account1 = customtkinter.CTkLabel(
    master = signup_frame,
    text = "Já tem uma conta?",
    font=("Arial", 16)    
    ) 
na_account1.pack(side = "left")

# --- Já tem uma conta 2 ---
na_account2 = customtkinter.CTkLabel(
    master = signup_frame,
    text = " Faça Login",
    font=("Arial", 16),
    text_color = "#FFFFFF",
    cursor = "hand2"           
    ) 
na_account2.pack(side = "right")
root.mainloop()
