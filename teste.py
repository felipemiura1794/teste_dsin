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

# ==================== IMAGE ====================
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

# ==================== LOGIN ====================
# --- Login label ---
label = customtkinter.CTkLabel(
    master = frame,
    text = "login", 
    font = ("Georgia", 30),
    text_color = "#FFFFFF"
    )
label.pack(pady = (30, 15), anchor = "w", padx = 55)

# --- Description ---
subtitle = customtkinter.CTkLabel(
    master = frame,
    text = "Acesse seus registros de Drones,\nPatos e até da hora que você fez\num lanchinho!",
    **DESCRIPTION_STYLE
)
subtitle.pack(pady = (10, 15), anchor = "w", padx = 20)

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

# --- Input "Password" ---
entry2 = customtkinter.CTkEntry( 
    master = frame, 
    placeholder_text = "Senha", 
    show = "*",
    **ENTRY_STYLE
    )
entry2.pack(pady = (20, 5), padx = 40)

# --- Password line ---
line2 = customtkinter.CTkFrame(
    master = frame,
    **LINES_STYLES
)
line2.pack(padx = 40,  fill = "x")

# --- Forgot Password ---
fg_password = customtkinter.CTkLabel(
    master = frame,
    text = "Esqueceu a senha?",
    **FG_PASSWORD_STYLE
)
fg_password.pack(pady = (10, 20), anchor = "e", padx = 40)

# --- Button login ---
log_button = customtkinter.CTkButton (
    master = frame, 
    text = "login",
    **LOG_BUTTON_STYLE
    )
log_button.pack(pady = 12, padx = 10)

# ============== Footer ==============
# --- Sign up frame ---
signup_frame = customtkinter.CTkFrame(
    master = frame,
    fg_color="transparent"
)
signup_frame.pack(pady=15)

# --- Not have account 1 ---
na_account1 = customtkinter.CTkLabel(
    master = signup_frame,
    text = "Não tem uma conta?",
    font=("Arial", 16)    
    ) 
na_account1.pack(side = "left")

# --- Not have account 2 ---
na_account2 = customtkinter.CTkLabel(
    master = signup_frame,
    text = " Cadastre-se",
    font=("Arial", 16, "bold"),
    text_color = "#FFFFFF",
    ) 
na_account2.pack(side = "right")

root.mainloop()
