import customtkinter as ctk
from cssInicioScreen import *
from PIL import Image

# --- Aparência do programa ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

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
            # Container para a barra
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
            
            text_label = ctk.CTkLabel(
                master=bar_label,
                text=self.text,
                font=("Roboto", 12, "bold"),
                text_color="white",
                fg_color="transparent",
                bg_color="#44959E"
            )
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
    {"image": "vetor4.png", "text": "Perigo fatal!", "position": "first"},
]

for bar_info in bars_data:
    StatusBar(bars_container, bar_info["image"], bar_info["text"], bar_info["position"])

# =================== NOME PATO ===================
pato_label = ctk.CTkLabel(
    master=frame,
    text="PATO 1",
    font=("Georgia", 26),
    text_color="#FFFFFF"
)
pato_label.pack(pady=(30, 15), anchor="w", padx=40)

# =================== DESCRIÇÃO ===================
pato_subtitle = ctk.CTkLabel(
    master=frame,
    text="*descrição pato",
    text_color = "#CFCFCF",
    font = ("Georgia",16,),
    justify="left"
)
pato_subtitle.pack(anchor="w", padx=40, pady=(0))

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
# Caixa 1: Altura
pato_box1 = ctk.CTkFrame(
    master=footerFrame,
    fg_color="#44959E",
    corner_radius=10
)
pato_box1.grid(row=0, column=0, padx=(0, 5), pady=(0, 5), sticky="nsew")

pato_icon_label1 = ctk.CTkLabel(
    master=pato_box1,
    text="🏭",
    font=("Roboto", 14),
    text_color="white"
)
pato_icon_label1.pack(anchor="w", padx=10, pady=(8, 0))

pato_title_label1 = ctk.CTkLabel(
    master=pato_box1,
    text="Altura",
    font=("Roboto", 12, "bold"),
    text_color="white",
    anchor="w",
    wraplength=130
)
pato_title_label1.pack(anchor="w", padx=10, fill="x")

pato_info_label1 = ctk.CTkLabel(
    master=pato_box1,
    text="100 centímetros",
    font=("Roboto", 10),
    text_color="#E0E0E0",
    anchor="w",
    justify="left",
    wraplength=130
)
pato_info_label1.pack(anchor="w", padx=10, pady=(0, 8), fill="x")

# Caixa 2: Batimentos Cardiacos
pato_box2 = ctk.CTkFrame(
    master=footerFrame,
    fg_color="#44959E",
    corner_radius=10
)
pato_box2.grid(row=0, column=1, padx=(5, 0), pady=(0, 5), sticky="nsew")

pato_icon_label2 = ctk.CTkLabel(
    master=pato_box2,
    text="⚔️",
    font=("Roboto", 14),
    text_color="white"
)
pato_icon_label2.pack(anchor="w", padx=10, pady=(8, 0))

pato_title_label2 = ctk.CTkLabel(
    master=pato_box2,
    text="Batimentos Cardiacos",
    font=("Roboto", 12, "bold"),
    text_color="white",
    anchor="w",
    wraplength=130
)
pato_title_label2.pack(anchor="w", padx=10, fill="x")

pato_info_label2 = ctk.CTkLabel(
    master=pato_box2,
    text="94 BPM",
    font=("Roboto", 10),
    text_color="#E0E0E0",
    anchor="w",
    justify="left",
    wraplength=130
)
pato_info_label2.pack(anchor="w", padx=10, pady=(0, 8), fill="x")

# Caixa 3: Velocidade
pato_box3 = ctk.CTkFrame(
    master=footerFrame,
    fg_color="#44959E",
    corner_radius=10
)
pato_box3.grid(row=1, column=0, padx=(0, 5), pady=(5, 0), sticky="nsew")

pato_icon_label3 = ctk.CTkLabel(
    master=pato_box3,
    text="⚡",
    font=("Roboto", 14),
    text_color="white"
)
pato_icon_label3.pack(anchor="w", padx=10, pady=(8, 0))

pato_title_label3 = ctk.CTkLabel(
    master=pato_box3,
    text="Velocidade",
    font=("Roboto", 12, "bold"),
    text_color="white",
    anchor="w",
    wraplength=130
)
pato_title_label3.pack(anchor="w", padx=10, fill="x")

pato_info_label3 = ctk.CTkLabel(
    master=pato_box3,
    text="33 m/s",
    font=("Roboto", 10),
    text_color="#E0E0E0",
    anchor="w",
    justify="left",
    wraplength=130
)
pato_info_label3.pack(anchor="w", padx=10, pady=(0, 8), fill="x")

# Caixa 4: Peso
pato_box4 = ctk.CTkFrame(
    master=footerFrame,
    fg_color="#44959E",
    corner_radius=10
)
pato_box4.grid(row=1, column=1, padx=(5, 0), pady=(5, 0), sticky="nsew")

pato_icon_label4 = ctk.CTkLabel(
    master=pato_box4,
    text="🎯",
    font=("Roboto", 14),
    text_color="white"
)
pato_icon_label4.pack(anchor="w", padx=10, pady=(8, 0))

pato_title_label4 = ctk.CTkLabel(
    master=pato_box4,
    text="Peso",
    font=("Roboto", 12, "bold"),
    text_color="white",
    anchor="w",
    wraplength=130
)
pato_title_label4.pack(anchor="w", padx=10, fill="x")

pato_info_label4 = ctk.CTkLabel(
    master=pato_box4,
    text="30 quilos",
    font=("Roboto", 10),
    text_color="#E0E0E0",
    anchor="w",
    justify="left",
    wraplength=130
)
pato_info_label4.pack(anchor="w", padx=10, pady=(0, 8), fill="x")

# =================== BOTÕES DE CONTROLE ===================
try:
    # Frame dos botões
    control_buttons_frame = ctk.CTkFrame(
        master=root,
        fg_color="transparent"
    )
    control_buttons_frame.pack(fill="x", padx=40, pady=(10, 30))
    
    # Configurar grid com 3 colunas
    control_buttons_frame.grid_columnconfigure(0, weight=1)
    control_buttons_frame.grid_columnconfigure(1, weight=1)
    control_buttons_frame.grid_columnconfigure(2, weight=1)
    
    # Botão 1: Sobre
    sobre_button = ctk.CTkButton(
        master=control_buttons_frame,
        text="SOBRE",
        font=("Roboto", 14, "bold"),
        text_color="white",
        fg_color="#44959E",
        hover_color="#3A8089",
        corner_radius=15,
        height=50
    )
    sobre_button.grid(row=0, column=0, padx=(0, 5), sticky="ew")
    
    # Botão 2: Status
    status_button = ctk.CTkButton(
        master=control_buttons_frame,
        text="STATUS",
        font=("Roboto", 14, "bold"),
        text_color="white",
        fg_color="#44959E",
        hover_color="#3A8089",
        corner_radius=15,
        height=50
    )
    status_button.grid(row=0, column=1, padx=5, sticky="ew")
    
    # Botão 3: Ataque
    ataque_button = ctk.CTkButton(
        master=control_buttons_frame,
        text="ATAQUE",
        font=("Roboto", 14, "bold"),
        text_color="white",
        fg_color="#44959E",
        hover_color="#3A8089",
        corner_radius=15,
        height=50
    )
    ataque_button.grid(row=0, column=2, padx=(5, 0), sticky="ew")
    
except Exception as e:
    print(f"Erro ao criar botões de controle: {e}")

root.mainloop()