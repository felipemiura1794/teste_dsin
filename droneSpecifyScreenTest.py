import customtkinter as ctk
from cssInicioScreen import *
from PIL import Image

# --- Aparência do programa ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# =================== CLASSE DRONE CARD ===================
class DroneCard:
    
    def __init__(self, master, drone_name, drone_status, drone_image_path="droneImagem.png"):
        self.master = master
        self.drone_name = drone_name
        self.drone_status = drone_status
        self.drone_image_path = drone_image_path
        
        # Criar o card
        self.frame = None
        self.create_card()
    
    def create_card(self):
        # Frame principal do drone
        self.frame = ctk.CTkFrame(
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
        
        # Imagem do drone
        try:
            drone_image = ctk.CTkImage(
                dark_image=Image.open(self.drone_image_path),
                size=(70, 70)
            )
            drone_image_label = ctk.CTkLabel(
                master=self.frame,
                image=drone_image,
                text=""
            )
            drone_image_label.image = drone_image
            drone_image_label.grid(row=0, column=0, padx=(15, 15), pady=15, sticky="w")
        except Exception as e:
            print(f"Erro ao carregar imagem do drone: {e}")
        
        # Frame para os textos
        text_frame = ctk.CTkFrame(
            master=self.frame,
            fg_color="transparent"
        )
        text_frame.grid(row=0, column=1, sticky="w", padx=(0, 15), pady=15)
        
        # Título do drone
        title = ctk.CTkLabel(
            master=text_frame,
            text=self.drone_name,
            font=("Roboto", 16, "bold"),
            text_color="white",
            anchor="w"
        )
        title.pack(anchor="w")
        
        # Descrição/Status
        description = ctk.CTkLabel(
            master=text_frame,
            text=self.drone_status,
            font=("Roboto", 12),
            text_color="#B0C4DE",
            anchor="w"
        )
        description.pack(anchor="w", pady=(2, 0))
    
    def add_separator(self):
        line = ctk.CTkFrame(
            master=self.master,
            **LINES_STYLES
        )
        line.pack(padx=20, fill="x")
    
    def destroy(self):
        if self.frame:
            self.frame.destroy()

# =================== CLASSE PARA AS BARRAS ===================
class StatusBar:
    def __init__(self, master, image_path, text, position):
        self.master = master
        self.image_path = image_path
        self.text = text
        self.position = position
        self.create_bar()
    
    def create_bar(self):
        try:
            # Container para a barra (para manter o posicionamento relativo)
            bar_container = ctk.CTkFrame(
                master=self.master,
                fg_color="transparent",
                height=37
            )
            bar_container.pack(anchor="e", pady=(10 if self.position == "first" else 5))
            
            # Imagem da barra
            bar_image = ctk.CTkImage(
                dark_image=Image.open(self.image_path),
                size=(150, 37)
            )
            bar_label = ctk.CTkLabel(
                master=bar_container,
                text="",
                image=bar_image,
                fg_color="transparent"
            )
            bar_label.pack()
            
            # Texto sobre a barra usando place para posicionamento absoluto
            text_label = ctk.CTkLabel(
                master=bar_label,
                text=self.text,
                font=("Roboto", 12, "bold"),
                text_color="white",
                fg_color="transparent",
                bg_color="#44959E"
            )
            # Ajusta posição: "Muito danificado" mais à direita, demais centralizados
            if "danificado" in self.text.lower():
                text_label.place(relx=0.58, rely=0.5, anchor="center")
            else:
                text_label.place(relx=0.5, rely=0.5, anchor="center")
            
        except Exception as e:
            print(f"Erro ao carregar imagem da barra {self.text}: {e}")

# --- Configuração Root ---
root = ctk.CTk()
root.geometry("401x820")
root.resizable(False, False)
root.configure(fg_color="#357E94")

radio_var = ctk.IntVar(value=0)

def login():
    print("Test")

# =================== HEADER FRAME ===================
headerFrame = ctk.CTkFrame(
    master=root,
    fg_color="transparent",
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
    menu_image = ctk.CTkImage(
        dark_image=Image.open("menu.png"),    
        size=(35, 35)
    )
    menuImage_label = ctk.CTkLabel(
        master=headerFrame,
        image=menu_image,
        text=""
    )
    menuImage_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")
    
    # --- Logo imagem ---
    logo_image = ctk.CTkImage(
        light_image=Image.open("duck.png"),
        dark_image=Image.open("duck.png"),
        size=(70, 70)
    )
    logoImage_label = ctk.CTkLabel(
        master=headerFrame,
        image=logo_image,
        text=""
    )
    logoImage_label.grid(row=0, column=1, pady=(20, 0))
    
    # --- User imagem ---
    user_image = ctk.CTkImage(
        dark_image=Image.open("user.png"),
        size=(35, 35)
    )
    userImage_label = ctk.CTkLabel(
        master=headerFrame,
        image=user_image,
        text=""
    )
    userImage_label.grid(row=0, column=2, padx=20, pady=(20, 0), sticky="e")
    
except Exception as e:
    print(f"Erro ao carregar imagens: {e}")

# =================== FRAME MAIN ===================
frame = ctk.CTkFrame(
    master=root,
    fg_color="transparent",
    corner_radius=0
)
frame.pack(fill="both", expand=True, padx=0, pady=(30,0))

# =================== BOTÃO FECHAR ===================
try:
    exitImage = ctk.CTkImage(
        dark_image=Image.open("xVetor.png"),
        size=(50, 50)
    )
    exitImage_label = ctk.CTkLabel(
        master=frame,
        text="",
        image=exitImage,
        fg_color="transparent"
    )
    exitImage_label.pack(anchor="w", padx=(30, 0))

except Exception as e:
    print(f"Erro ao carregar imagem X: {e}")

# =================== CONTAINER PARA AS BARRAS ===================
bars_container = ctk.CTkFrame(
    master=frame,
    fg_color="transparent",
    height=150
)
bars_container.pack(fill="x", pady=(20, 0))
bars_container.pack_propagate(False)

# =================== BARRAS DE STATUS ===================
bars_data = [
    {"image": "vetor.png", "text": "Restam 5h", "position": "first"},
    {"image": "vetor1.png", "text": "Restam 5h", "position": "middle"},
    {"image": "vetor2.png", "text": "Muito danificado", "position": "last"}
]

for bar_info in bars_data:
    StatusBar(bars_container, bar_info["image"], bar_info["text"], bar_info["position"])

# =================== NOME DRONE ===================
label = ctk.CTkLabel(
    master=frame,
    text="Drone 1", #coloca aqui o nome do drone que puxa do banco de dados depois e tals :P
    font=("Georgia", 26),
    text_color="#FFFFFF"
)
label.pack(pady=(30, 15), anchor="w", padx=40)

# =================== DESCRIÇÃO ===================
subtitle = ctk.CTkLabel(
    master=frame,
    text="AQUI VAI OS COISO DO DRONE",
    text_color = "#CFCFCF",
    font = ("Georgia",16,),
    justify="left"
)
subtitle.pack(anchor="w", padx=40, pady=(0))

# =================== FOOTER FRAME ===================
footerFrame = ctk.CTkFrame(
    master=root,
    fg_color="transparent"
)
footerFrame.pack(fill="both", expand=True, padx=40, pady=(20, 30))

# Configurar grid 2x2
footerFrame.grid_columnconfigure(0, weight=1)
footerFrame.grid_columnconfigure(1, weight=1)
footerFrame.grid_rowconfigure(0, weight=1)
footerFrame.grid_rowconfigure(1, weight=1)

# =================== CAIXAS DE INFORMAÇÕES ===================
# Caixa 1: Fabricante
box1 = ctk.CTkFrame(
    master=footerFrame,
    fg_color="#44959E",
    corner_radius=10,
    width=150,
    height=70
)
box1.grid(row=0, column=0, padx=(0, 5), pady=(0, 5), sticky="nsew")
box1.grid_propagate(False)

icon_label1 = ctk.CTkLabel(
    master=box1,
    text="🏭",
    font=("Roboto", 14),
    text_color="white"
)
icon_label1.pack(anchor="w", padx=10, pady=(8, 0))

title_label1 = ctk.CTkLabel(
    master=box1,
    text="Fabricante",
    font=("Roboto", 12, "bold"),
    text_color="white",
    anchor="w"
)
title_label1.pack(anchor="w", padx=10)

info_label1 = ctk.CTkLabel(
    master=box1,
    text="DJI",
    font=("Roboto", 10),
    text_color="#E0E0E0",
    anchor="w",
    justify="left"
)
info_label1.pack(anchor="w", padx=10, pady=(0, 8))

# Caixa 2: Ataque
box2 = ctk.CTkFrame(
    master=footerFrame,
    fg_color="#44959E",
    corner_radius=10,
    width=150,
    height=70
)
box2.grid(row=0, column=1, padx=(5, 0), pady=(0, 5), sticky="nsew")
box2.grid_propagate(False)

icon_label2 = ctk.CTkLabel(
    master=box2,
    text="⚔️",
    font=("Roboto", 14),
    text_color="white"
)
icon_label2.pack(anchor="w", padx=10, pady=(8, 0))

title_label2 = ctk.CTkLabel(
    master=box2,
    text="Ataque",
    font=("Roboto", 12, "bold"),
    text_color="white",
    anchor="w"
)
title_label2.pack(anchor="w", padx=10)

info_label2 = ctk.CTkLabel(
    master=box2,
    text="Laser",
    font=("Roboto", 10),
    text_color="#E0E0E0",
    anchor="w",
    justify="left"
)
info_label2.pack(anchor="w", padx=10, pady=(0, 8))

# Caixa 3: Velocidade
box3 = ctk.CTkFrame(
    master=footerFrame,
    fg_color="#44959E",
    corner_radius=10,
    width=150,
    height=70
)
box3.grid(row=1, column=0, padx=(0, 5), pady=(5, 0), sticky="nsew")
box3.grid_propagate(False)

icon_label3 = ctk.CTkLabel(
    master=box3,
    text="⚡",
    font=("Roboto", 14),
    text_color="white"
)
icon_label3.pack(anchor="w", padx=10, pady=(8, 0))

title_label3 = ctk.CTkLabel(
    master=box3,
    text="Velocidade",
    font=("Roboto", 12, "bold"),
    text_color="white",
    anchor="w"
)
title_label3.pack(anchor="w", padx=10)

info_label3 = ctk.CTkLabel(
    master=box3,
    text="33 m/s",
    font=("Roboto", 10),
    text_color="#E0E0E0",
    anchor="w",
    justify="left"
)
info_label3.pack(anchor="w", padx=10, pady=(0, 8))

# Caixa 4: Precisão
box4 = ctk.CTkFrame(
    master=footerFrame,
    fg_color="#44959E",
    corner_radius=10,
    width=150,
    height=70
)
box4.grid(row=1, column=1, padx=(5, 0), pady=(5, 0), sticky="nsew")
box4.grid_propagate(False)

icon_label4 = ctk.CTkLabel(
    master=box4,
    text="🎯",
    font=("Roboto", 14),
    text_color="white"
)
icon_label4.pack(anchor="w", padx=10, pady=(8, 0))

title_label4 = ctk.CTkLabel(
    master=box4,
    text="Precisão",
    font=("Roboto", 12, "bold"),
    text_color="white",
    anchor="w"
)
title_label4.pack(anchor="w", padx=10)

info_label4 = ctk.CTkLabel(
    master=box4,
    text="± 1.5 cm",
    font=("Roboto", 10),
    text_color="#E0E0E0",
    anchor="w",
    justify="left"
)
info_label4.pack(anchor="w", padx=10, pady=(0, 8))

# =================== BOTÃO DE CONTROLE ===================
try:
    # Frame do botão
    control_button_frame = ctk.CTkFrame(
        master=root,
        fg_color="transparent"
    )
    control_button_frame.pack(fill="x", padx=40, pady=(10, 30))
    
    # Botão de controle
    control_button = ctk.CTkButton(
        master=control_button_frame,
        text="CONTROLE",
        font=("Roboto", 18, "bold"),
        text_color="white",
        fg_color="#44959E",
        hover_color="#3A8089",
        corner_radius=15,
        height=60
    )
    control_button.pack(fill="x")
    
    try:
        camera_icon = ctk.CTkImage(
            dark_image=Image.open("camera.png"),
            size=(30, 30)
        )
        control_button.configure(image=camera_icon, compound="right")
    except:
        control_button.configure(text="CONTROLE  📷")
        
except Exception as e:
    print(f"Erro ao criar botão de controle: {e}")

root.mainloop()