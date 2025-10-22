import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("800x600")
root.title("Exemplo de Frames")

# Frame principal que ocupa toda a janela
main_frame = customtkinter.CTkFrame(master=root, fg_color="transparent")
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# ========== FRAME ESQUERDO - Texto informativo ==========
left_frame = customtkinter.CTkFrame(
    master=main_frame,
    fg_color="#2B2B2B",
    corner_radius=10
)
left_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

# Título do frame esquerdo
title_label = customtkinter.CTkLabel(
    master=left_frame,
    text="Bem-vindo ao Sistema",
    font=("Roboto", 28, "bold"),
    text_color="#4A9EBF"
)
title_label.pack(pady=(30, 10), padx=20)

# Parágrafo informativo
info_text = """
Este é um exemplo de como usar frames 
no CustomTkinter para organizar elementos.

Os frames funcionam como containers que 
agrupam widgets relacionados, facilitando 
o layout da interface.

Você pode criar quantos frames precisar 
e posicioná-los usando pack, grid ou place.
"""

paragraph_label = customtkinter.CTkLabel(
    master=left_frame,
    text=info_text,
    font=("Arial", 14),
    justify="left",
    wraplength=300
)
paragraph_label.pack(pady=20, padx=20)

# Botão de exemplo
example_button = customtkinter.CTkButton(
    master=left_frame,
    text="Saiba Mais",
    font=("Arial", 16),
    fg_color="#4A9EBF",
    hover_color="#357E94"
)
example_button.pack(pady=20, padx=20)


# ========== FRAME DIREITO - Login ==========
right_frame = customtkinter.CTkFrame(
    master=main_frame,
    fg_color="#357E94",
    corner_radius=10
)
right_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))

def login():
    username = entry1.get()
    password = entry2.get()
    print(f"Login: {username}")
    print(f"Senha: {'*' * len(password)}")

# Logo (tente carregar, senão mostra só o texto)
try:
    logo_image = customtkinter.CTkImage(
        light_image=Image.open("duck.png"),
        dark_image=Image.open("duck.png"),
        size=(80, 80)
    )
    image_label = customtkinter.CTkLabel(
        master=right_frame,
        image=logo_image,
        text=""
    )
    image_label.pack(pady=(30, 10))
except:
    pass

# Título Login
login_label = customtkinter.CTkLabel(
    master=right_frame,
    text="Login",
    font=("Roboto", 32, "bold")
)
login_label.pack(pady=(10, 5))

# Subtítulo
subtitle_label = customtkinter.CTkLabel(
    master=right_frame,
    text="Acesse seus registros de Drones,\nPatos e até da hora que você fez\num lanchinho!",
    font=("Arial", 12),
    justify="center"
)
subtitle_label.pack(pady=(0, 20))

# Entry Username
entry1 = customtkinter.CTkEntry(
    master=right_frame,
    placeholder_text="Email",
    fg_color="transparent",
    border_width=0,
    border_color="#FFFFFF",
    width=280,
    height=40,
    font=("Arial", 14)
)
entry1.pack(pady=12, padx=40)

# Linha divisória no entry 1
line1 = customtkinter.CTkFrame(
    master=right_frame,
    height=2,
    fg_color="#FFFFFF"
)
line1.pack(padx=40, fill="x")

# Entry Password
entry2 = customtkinter.CTkEntry(
    master=right_frame,
    placeholder_text="Senha",
    show="*",
    fg_color="transparent",
    border_width=0,
    width=280,
    height=40,
    font=("Arial", 14)
)
entry2.pack(pady=(20, 12), padx=40)

# Linha divisória no entry 2
line2 = customtkinter.CTkFrame(
    master=right_frame,
    height=2,
    fg_color="#FFFFFF"
)
line2.pack(padx=40, fill="x")

# Forgot Password
forgot_label = customtkinter.CTkLabel(
    master=right_frame,
    text="Forgot Password?",
    font=("Arial", 11),
    text_color="#E0E0E0",
    cursor="hand2"
)
forgot_label.pack(pady=(10, 20), anchor="e", padx=40)

# Botão Login
login_button = customtkinter.CTkButton(
    master=right_frame,
    text="LOGIN",
    command=login,
    font=("Arial", 16, "bold"),
    fg_color="#5FAFBF",
    hover_color="#4A9EBF",
    height=45,
    width=280,
    corner_radius=8
)
login_button.pack(pady=10, padx=40)

# Cadastro
signup_frame = customtkinter.CTkFrame(
    master=right_frame,
    fg_color="transparent"
)
signup_frame.pack(pady=15)

signup_label1 = customtkinter.CTkLabel(
    master=signup_frame,
    text="Não tem uma conta? ",
    font=("Arial", 12)
)
signup_label1.pack(side="left")

signup_label2 = customtkinter.CTkLabel(
    master=signup_frame,
    text="Cadastre-se",
    font=("Arial", 12, "bold"),
    text_color="#5FAFBF",
    cursor="hand2"
)
signup_label2.pack(side="left")

root.mainloop()