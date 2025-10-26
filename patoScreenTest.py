import customtkinter as ctk
from cssInicioScreen import *
from PIL import Image

# --- Aparência do programa ---
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# =================== CLASSE PATO CARD ===================
class PatoCard:
    
    def __init__(self, master, pato_name, pato_status, pato_image_path="pato.png"):
        self.master = master
        self.pato_name = pato_name
        self.pato_status = pato_status
        self.pato_image_path = pato_image_path
        
        # Criar o card
        self.frame = None
        self.create_card()
    
    def create_card(self):
        # Frame principal do pato
        self.frame = customtkinter.CTkFrame(
            master=self.master,
            fg_color="transparent",
            corner_radius=10,
            height=90
        )
        self.frame.pack(fill="x", pady=(0, 10))
        self.frame.pack_propagate(False)
        
        # Configuração do grid
        self.frame.grid_columnconfigure(0, weight=0)
        self.frame.grid_columnconfigure(1, weight=1)
        
        # Imagem do pato
        try:
            pato_image = customtkinter.CTkImage(
                dark_image=Image.open(self.pato_image_path),
                size=(100, 70)
            )
            pato_image_label = customtkinter.CTkLabel(
                master=self.frame,
                image=pato_image,
                text=""
            )
            pato_image_label.image = pato_image
            pato_image_label.grid(row=0, column=0, padx=(15, 15), pady=15, sticky="w")
        except Exception as e:
            print(f"Erro ao carregar imagem do pato: {e}")
        
        # Frame para os textos
        text_frame = customtkinter.CTkFrame(
            master=self.frame,
            fg_color="transparent"
        )
        text_frame.grid(row=0, column=1, sticky="w", padx=(0, 15), pady=15)
        
        # Título do pato
        title = customtkinter.CTkLabel(
            master=text_frame,
            text=self.pato_name,
            font=("Roboto", 16, "bold"),
            text_color="white",
            anchor="w"
        )
        title.pack(anchor="w")
        
        # Descrição/Status
        description = customtkinter.CTkLabel(
            master=text_frame,
            text=self.pato_status,
            font=("Roboto", 12),
            text_color="#B0C4DE",
            anchor="w"
        )
        description.pack(anchor="w", pady=(2, 0))
    
    def add_separator(self):
        line = customtkinter.CTkFrame(
            master=self.master,
            **LINES_STYLES
        )
        line.pack(padx=20, fill="x")
    
    def destroy(self):
        if self.frame:
            self.frame.destroy()


# --- Configuração Root ---
root = customtkinter.CTk()
root.geometry("401x820")
root.resizable(False, False)
root.configure(fg_color="#357E94")

radio_var = customtkinter.IntVar(value=0)

def login():
    print("Test")

# =================== HEADER FRAME ===================
headerFrame = customtkinter.CTkFrame(
    master=root,
    fg_color="#357E94",
    corner_radius=0,
    height=100
)
headerFrame.pack(fill="x", padx=0, pady=(30,0))
headerFrame.pack_propagate(False)

headerFrame.grid_columnconfigure(0, weight=1)
headerFrame.grid_columnconfigure(1, weight=1)
headerFrame.grid_columnconfigure(2, weight=1)

# ==================== HEADER IMAGENS ====================
try:
    # --- Menu imagem ---
    menu_image = customtkinter.CTkImage(
        dark_image=Image.open("menu.png"),    
        size=(35, 35)
    )
    menuImage_label = customtkinter.CTkLabel(
        master=headerFrame,
        image=menu_image,
        text=""
    )
    menuImage_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")
    
    # --- Logo imagem ---
    logo_image = customtkinter.CTkImage(
        light_image=Image.open("duck.png"),
        dark_image=Image.open("duck.png"),
        size=(70, 70)
    )
    logoImage_label = customtkinter.CTkLabel(
        master=headerFrame,
        image=logo_image,
        text=""
    )
    logoImage_label.grid(row=0, column=1, pady=20)
    
    # --- User imagem ---
    user_image = customtkinter.CTkImage(
        dark_image=Image.open("user.png"),
        size=(35, 35)
    )
    userImage_label = customtkinter.CTkLabel(
        master=headerFrame,
        image=user_image,
        text=""
    )
    userImage_label.grid(row=0, column=2, padx=20, pady=20, sticky="e")
    
except Exception as e:
    print(f"Erro ao carregar imagens: {e}")

# =================== FRAME MAIN ===================
frame = customtkinter.CTkFrame(
    master=root,
    fg_color="#357E94",
    corner_radius=0
)
frame.pack(fill="both", expand=True, padx=0, pady=(30,0))

# ==================== CONTEUDO MAIN ====================
# ----- Seção título -----
patoTitle = customtkinter.CTkLabel(
    master=frame,
    text="Patos capturados:",
    font=("Georgia", 24, "bold"),
    text_color="white"
)
patoTitle.pack(anchor="w", padx=25, pady=(0, 10))

# ==================== PATOS CONTAINER ====================
patoContainer = customtkinter.CTkScrollableFrame(
    master=frame,
    fg_color="transparent",
    scrollbar_button_color="#DCE7F6",    
)
patoContainer.pack(fill="both", padx=25, pady=(0, 10), expand = True)

# ==================== PATOS ====================
patos_list = []

# Criando patos usando a classe
pato1 = PatoCard(
    master=patoContainer,
    pato_name="Pato 1.",
    pato_status="Nenhum movimento suspeito detectado!"
)
patos_list.append(pato1)
pato1.add_separator()

pato2 = PatoCard(
    master=patoContainer,
    pato_name="Pato 2.",
    pato_status="Necessita de reparos!"
)
patos_list.append(pato2)
pato2.add_separator()

pato3 = PatoCard(
    master=patoContainer,
    pato_name="Pato 3.",
    pato_status="Em patrulha na área norte!"
)
patos_list.append(pato3)
pato3.add_separator()

pato4 = PatoCard(
    master=patoContainer,
    pato_name="Pato 4.",
    pato_status="Bateria baixa - retornando à base!"
)
patos_list.append(pato4)
# =================== ADICIONAR PATO ===================

button_add_image = customtkinter.CTkImage(
    dark_image=Image.open("add.png"),
    size = (60,60)
)

button_add = customtkinter.CTkButton(
    master = frame,
    image = button_add_image,
    text = "",
    fg_color = "transparent"    
)
button_add.pack ()

# =================== FOOTER (Pode ser usado em todas as paginas) ===================
footerFrame = customtkinter.CTkFrame(
    master=root,
    fg_color="#357E94",
    corner_radius=0,
    height=100
)
footerFrame.pack(side="bottom", fill="x", padx=0, pady=0)
footerFrame.pack_propagate(False)

footerFrame.grid_columnconfigure(0, weight=1)
footerFrame.grid_columnconfigure(1, weight=1)
footerFrame.grid_columnconfigure(2, weight=1)

try:
    # --- Patodex imagem ---
    patodexMenu_image = customtkinter.CTkImage(
        dark_image=Image.open("patodexVetor.png"),    
        size=(40, 40)
    )
    patodexMenu_image_label = customtkinter.CTkLabel(
        master=footerFrame,
        image=patodexMenu_image,
        text=""
    )
    patodexMenu_image_label.grid(row=0, column=0, padx=20, pady=30, sticky="")
    
    # --- Patos imagem ---
    patoMenu_image = customtkinter.CTkImage(
        dark_image=Image.open("droneVetor.png"),
        size=(40, 40)
    )
    patoMenu_image_label = customtkinter.CTkLabel(
        master=footerFrame,
        image=patoMenu_image, 
        text=""
    )
    patoMenu_image_label.grid(row=0, column=1, pady=30, sticky="")
    
    # --- Usuário imagem ---
    user2_image = customtkinter.CTkImage(
        dark_image=Image.open("userVetor.png"),
        size=(40, 40)
    )
    user2Image_label = customtkinter.CTkLabel(
        master=footerFrame,
        image=user2_image,
        text=""
    )
    user2Image_label.grid(row=0, column=2, padx=20, pady=30, sticky="")
    
except Exception as e:
    print(f"Erro ao carregar imagens do footer: {e}")

root.mainloop()