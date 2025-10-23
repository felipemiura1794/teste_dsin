import customtkinter
from cssInicioScreen import *
from PIL import Image

# --- Aparência do programa ---
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

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
frame.pack(fill="both", expand=True, padx=0, pady=0)

# ==================== CONTEUDO MAIN ====================

# --- Bem vindo label ---
mainTitle = customtkinter.CTkLabel(
    master=frame,
    text="Bem vindo(a) de volta!",
    **TITLE_LABEL_STYLE
)
mainTitle.pack(pady=(20, 5))

# --- Descrição ---
description = customtkinter.CTkLabel(
    master=frame,
    text="O que está procurando hoje?",
    **DESCRIPTION_LABEL_STYLE
)
description.pack(pady=(0, 20))

# ==================== BOTÕES PRINCIPAIS ====================

# ----- Frame para os 4 botões principais -----
buttonsFrame = customtkinter.CTkFrame(
    master=frame,
    fg_color="#357E94",
    corner_radius=0,
    height=120
)
buttonsFrame.pack(fill="x", padx=40, pady=(0, 20))
buttonsFrame.pack_propagate(False)

buttonsFrame.grid_columnconfigure(0, weight=1)
buttonsFrame.grid_columnconfigure(1, weight=1)
buttonsFrame.grid_columnconfigure(2, weight=1)
buttonsFrame.grid_columnconfigure(3, weight=1)

# ==================== BOTÕES IMAGENS ====================

try:
    # --- Patodex ---
    patodex_image = customtkinter.CTkImage(
        dark_image=Image.open("patodex.png"),    
        size=(60, 60)
    )
    patodex_button = customtkinter.CTkButton(
        master = buttonsFrame,
        image = patodex_image,        
        text="Patodex",
        **BUTTONS_STYLE 
    )
    patodex_button.grid(row=0, column=0, padx=3, pady=10)
    
    # --- Drones ---
    drone_image = customtkinter.CTkImage(
        dark_image=Image.open("drones.png"),
        size=(60, 60)
    )
    drone_button = customtkinter.CTkButton(
        master = buttonsFrame,
        image = drone_image,        
        text="Drones",
        **BUTTONS_STYLE 
    )
    drone_button.grid(row=0, column=1, padx=3, pady=10)
    
    # --- Aprender ---
    aprender_image = customtkinter.CTkImage(
        dark_image=Image.open("aprender.png"),
        size=(60, 60)
    )
    aprender_button = customtkinter.CTkButton(
        master = buttonsFrame,
        image = aprender_image,        
        text="Aprender",
        **BUTTONS_STYLE 
    )
    aprender_button.grid(row=0, column=2, padx=3, pady=10)

    # --- Suporte ---
    suporte_image = customtkinter.CTkImage(
        dark_image=Image.open("suporte.png"),
        size=(60, 60)
    )
    suporte_button = customtkinter.CTkButton(
        master = buttonsFrame,
        image = suporte_image,        
        text="Suporte",
        **BUTTONS_STYLE 
    )
    suporte_button.grid(row=0, column=3, padx=3, pady=10) 

except Exception as e:
    print(f"Erro ao carregar imagens dos botões: {e}")

# =================== DRONE SEÇÃO ===================
# ----- Seção título -----
droneTitle = customtkinter.CTkLabel(
    master=frame,
    text="Mais acessados:",
    font=("Georgia", 24, "bold"),
    text_color="white"
)
droneTitle.pack(anchor="w", padx=25, pady=(0, 10))

# ----- Drone container -----
droneContainer = customtkinter.CTkFrame(
    master = frame,
    fg_color = "transparent",
)
droneContainer.pack(fill = "x", padx = 25, pady = (0, 10))

try:
    # ----- Drone 1 -----
    drone1_frame = customtkinter.CTkFrame(
        master = droneContainer,
        fg_color = "transparent",
        corner_radius = 10,
        height = 90
    )
    drone1_frame.pack(fill="x", pady=(0, 10))
    drone1_frame.pack_propagate(False)

    # ----- configuração grid -----
    drone1_frame.grid_columnconfigure(0, weight=0)
    drone1_frame.grid_columnconfigure(1, weight=1)

    # ----- Drone imagem -----
    drone1_image = customtkinter.CTkImage(
        dark_image = Image.open("droneImagem.png"),
        size = (70, 70)
    )
    drone1_image_label = customtkinter.CTkLabel(
        master=drone1_frame,
        image=drone1_image,
        text=""        
    )
    drone1_image_label.grid(row=0, column=0, padx=(15, 15), pady=15, sticky="w")
    
    # ----- Frame para os textos -----
    drone1_text_frame = customtkinter.CTkFrame(
        master=drone1_frame,
        fg_color="transparent"
    )
    drone1_text_frame.grid(row=0, column=1, sticky="w", padx=(0, 15), pady=15)
    
    # ----- Título do drone ----- 
    drone1_title = customtkinter.CTkLabel(
        master=drone1_text_frame,
        text="Drone 1.",
        font=("Roboto", 16, "bold"),
        text_color="white",
        anchor="w"
    )
    drone1_title.pack(anchor="w")
    
    # ----- Descrição -----
    drone1_desc = customtkinter.CTkLabel(
        master=drone1_text_frame,
        text="Nenhum movimento suspeito detectado!",
        font=("Roboto", 12),
        text_color="#B0C4DE",
        anchor="w"
    )
    drone1_desc.pack(anchor="w", pady=(2, 0))
    
    # =================== SEPARAÇÃO LINHA ===================
    line = customtkinter.CTkFrame(
        master = droneContainer,
        **LINES_STYLES
    )
    line.pack(padx = 20,  fill = "x")

    # ----- DRONE 2 -----
    drone2_frame = customtkinter.CTkFrame(
        master = droneContainer,
        fg_color="transparent",
        corner_radius=10,
        height=90
    )
    drone2_frame.pack(fill="x", pady=(0, 10))
    drone2_frame.pack_propagate(False)
    
    drone2_frame.grid_columnconfigure(0, weight=0)
    drone2_frame.grid_columnconfigure(1, weight=1)
    
    # ----- Imagem drone 2 -----
    drone2_img_label = customtkinter.CTkLabel(
        master=drone2_frame,
        image=drone1_image,
        text=""
    )
    drone2_img_label.grid(row=0, column=0, padx=(15, 15), pady=15, sticky="w")
    
    # ----- Textos drone 2 -----
    drone2_text_frame = customtkinter.CTkFrame(
        master=drone2_frame,
        fg_color="transparent"
    )
    drone2_text_frame.grid(row=0, column=1, sticky="w", padx=(0, 15), pady=15)
    
    drone2_title = customtkinter.CTkLabel(
        master=drone2_text_frame,
        text="Drone 2.",
        font=("Roboto", 16, "bold"),
        text_color="white",
        anchor="w"
    )
    drone2_title.pack(anchor="w")
    
    drone2_desc = customtkinter.CTkLabel(
        master=drone2_text_frame,
        text="Necessita de reparos!",
        font=("Roboto", 12),
        text_color="#B0C4DE",
        anchor="w"
    )
    drone2_desc.pack(anchor="w", pady=(2, 0))
    
except Exception as e:
    print(f"Erro ao carregar seção de drones: {e}")

# =================== FOOTER (Pode ser usado em todas as paginas) ===================
# ----- Footer Frame
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
    
    # --- Drones imagem ---
    droneMenu_image = customtkinter.CTkImage(
        dark_image=Image.open("droneVetor.png"),
        size=(40, 40)
    )
    droneMenu_image_label = customtkinter.CTkLabel(
        master=footerFrame,
        image=droneMenu_image, 
        text=""
    )
    droneMenu_image_label.grid(row=0, column=1, pady=30, sticky="")
    
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