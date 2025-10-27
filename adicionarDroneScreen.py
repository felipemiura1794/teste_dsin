import customtkinter
from cssInicioScreen import *
from css import *
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
# ==================== SIDEBAR ====================
sidebar_window = None

class SidebarState:
    historico_aberto = False

def toggle_sidebar():
    global sidebar_window
    
    if sidebar_window and sidebar_window.winfo_exists():
        sidebar_window.destroy()
        sidebar_window = None
    else:
        sidebar_state = SidebarState()
        
        sidebar_window = customtkinter.CTkToplevel(root)
        sidebar_window.resizable(False, False)
        sidebar_window.configure(fg_color="#2A6A7D")
        sidebar_window.overrideredirect(True)
        sidebar_window.attributes("-topmost", True)
        
        window_width = 260
        window_height = 850
        
        root_x = root.winfo_x()
        root_y = root.winfo_y()
        sidebar_window.geometry(f"{window_width}x{window_height}+{root_x}+{root_y}")
        
        def update_sidebar_position():
            if sidebar_window and sidebar_window.winfo_exists():
                root_x = root.winfo_x()
                root_y = root.winfo_y()
                sidebar_window.geometry(f"{window_width}x{window_height}+{root_x}+{root_y}")
                sidebar_window.after(10, update_sidebar_position)
        
        update_sidebar_position()
        
        sidebar_frame = customtkinter.CTkFrame(
            master=sidebar_window,
            fg_color="#D9D9D9",
            corner_radius=0
        )
        sidebar_frame.pack(fill="both", expand=True)
        
        # ==================== CABEÇALHO DO USUÁRIO ====================
        user_header_frame = customtkinter.CTkFrame(
            master=sidebar_frame,
            fg_color="#357E94",
            corner_radius=0,
            height=80
        )
        user_header_frame.pack(fill="x", padx=0, pady=0)
        user_header_frame.pack_propagate(False)
        
        user_header_frame.grid_columnconfigure(0, weight=0)
        user_header_frame.grid_columnconfigure(1, weight=1)
        user_header_frame.grid_columnconfigure(2, weight=0)
        user_header_frame.grid_rowconfigure(0, weight=1)
        user_header_frame.grid_rowconfigure(1, weight=1)
        
        try:
            user_sidebar_image = customtkinter.CTkImage(
                dark_image=Image.open("user.png"),
                size=(40, 40)
            )
            user_sidebar_label = customtkinter.CTkLabel(
                master=user_header_frame,
                image=user_sidebar_image,
                text=""
            )
            user_sidebar_label.grid(row=0, column=0, rowspan=2, padx=(15, 10), pady=10, sticky="w")
            
            username_label = customtkinter.CTkLabel(
                master=user_header_frame,
                text="Nome do Usuário",
                font=("Arial", 14, "bold"),
                text_color="white",
                anchor="w"
            )
            username_label.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="w")
            
            email_label = customtkinter.CTkLabel(
                master=user_header_frame,
                text="usuario@gmail.com",
                font=("Arial", 12),
                text_color="#E8F4F8",
                anchor="w"
            )
            email_label.grid(row=1, column=1, padx=(0, 10), pady=(0, 10), sticky="w")
            
            menu_image_sidebar = customtkinter.CTkImage(
                dark_image=Image.open("menu.png"),
                size=(25, 25)
            )
            close_sidebar_btn = customtkinter.CTkButton(
                master=user_header_frame,
                image=menu_image_sidebar,
                text="",
                width=35,
                height=35,
                fg_color="transparent",
                hover_color="#2A6A7D",
                command=toggle_sidebar
            )
            close_sidebar_btn.grid(row=0, column=2, rowspan=2, padx=(0, 15), pady=10, sticky="e")
            
        except Exception as e:
            print(f"Erro ao carregar imagens da sidebar: {e}")
        
        # ==================== MENU PRINCIPAL ====================
        menu_frame = customtkinter.CTkFrame(
            master=sidebar_frame,
            fg_color="transparent"
        )
        menu_frame.pack(fill="both", expand=True, padx=0, pady=20)
        
        try:
            # Home
            home_frame = customtkinter.CTkFrame(
                master=menu_frame,
                fg_color="transparent",
                height=50
            )
            home_frame.pack(fill="x", padx=20, pady=(0, 30))
            home_frame.pack_propagate(False)
            
            home_frame.grid_columnconfigure(0, weight=0)
            home_frame.grid_columnconfigure(1, weight=1)
            
            home_icon = customtkinter.CTkImage(
                dark_image=Image.open("home.png"),
                size=(25, 25)
            )
            home_icon_label = customtkinter.CTkLabel(
                master=home_frame,
                image=home_icon,
                text=""
            )
            home_icon_label.grid(row=0, column=0, padx=(0, 15), sticky="w")
            
            home_text = customtkinter.CTkLabel(
                master=home_frame,
                text="Home",
                font=("Arial", 16, "bold"),
                text_color="#324054",
                anchor="w"
            )
            home_text.grid(row=0, column=1, sticky="w")
            
            # Patodex
            patodex_frame = customtkinter.CTkFrame(
                master=menu_frame,
                fg_color="transparent",
                height=50
            )
            patodex_frame.pack(fill="x", padx=20, pady=(0, 30))
            patodex_frame.pack_propagate(False)
            
            patodex_frame.grid_columnconfigure(0, weight=0)
            patodex_frame.grid_columnconfigure(1, weight=1)
            
            patodex_icon = customtkinter.CTkImage(
                dark_image=Image.open("patodexIco.png"),
                size=(25, 25)
            )
            patodex_icon_label = customtkinter.CTkLabel(
                master=patodex_frame,
                image=patodex_icon,
                text=""
            )
            patodex_icon_label.grid(row=0, column=0, padx=(0, 15), sticky="w")
            
            patodex_text = customtkinter.CTkLabel(
                master=patodex_frame,
                text="Patodex",
                font=("Arial", 16, "bold"),
                text_color="#324054",
                anchor="w"
            )
            patodex_text.grid(row=0, column=1, sticky="w")
            
            # Drones
            drones_frame = customtkinter.CTkFrame(
                master=menu_frame,
                fg_color="transparent",
                height=50
            )
            drones_frame.pack(fill="x", padx=20, pady=(0, 30))
            drones_frame.pack_propagate(False)
            
            drones_frame.grid_columnconfigure(0, weight=0)
            drones_frame.grid_columnconfigure(1, weight=1)
            
            drones_icon = customtkinter.CTkImage(
                dark_image=Image.open("droneIco.png"),
                size=(25, 25)
            )
            drones_icon_label = customtkinter.CTkLabel(
                master=drones_frame,
                image=drones_icon,
                text=""
            )
            drones_icon_label.grid(row=0, column=0, padx=(0, 15), sticky="w")
            
            drones_text = customtkinter.CTkLabel(
                master=drones_frame,
                text="Drones",
                font=("Arial", 16, "bold"),
                text_color="#324054",
                anchor="w"
            )
            drones_text.grid(row=0, column=1, sticky="w")

            # Logout
            logout_frame = customtkinter.CTkFrame(
                master=menu_frame,
                fg_color="transparent",
                height=50
            )
            logout_frame.pack(fill="x", padx=20, pady=(0, 30))
            logout_frame.pack_propagate(False)
            
            logout_frame.grid_columnconfigure(0, weight=0)
            logout_frame.grid_columnconfigure(1, weight=1)
            
            logout_icon = customtkinter.CTkImage(
                dark_image=Image.open("logout.png"),
                size=(25, 25)
            )
            logout_icon_label = customtkinter.CTkLabel(
                master=logout_frame,
                image=logout_icon,
                text=""
            )
            logout_icon_label.grid(row=0, column=0, padx=(0, 15), sticky="w")
            
            logout_text = customtkinter.CTkLabel(
                master=logout_frame,
                text="logout",
                font=("Arial", 16, "bold"),
                text_color="#324054",
                anchor="w"
            )
            logout_text.grid(row=0, column=1, sticky="w")

        except Exception as e:
            print(f"Erro ao carregar ícones do menu: {e}")

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
    # --- Menu imagem (agora com função) ---
    menu_image = customtkinter.CTkImage(
        dark_image=Image.open("menu.png"),    
        size=(35, 35)
    )
    menuImage_label = customtkinter.CTkLabel(
        master=headerFrame,
        image=menu_image,
        text="",
        cursor="hand2"
    )
    menuImage_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")
    menuImage_label.bind("<Button-1>", lambda e: toggle_sidebar())
    
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
frame = customtkinter.CTkScrollableFrame(
    master=root,
    fg_color="#357E94",
    corner_radius=0,
    scrollbar_button_color="#DCE7F6"
)
frame.pack(fill="both", expand=True, pady=0, padx=0)

# ==================== CONTEUDO MAIN ====================

# --- Login label ---
label = customtkinter.CTkLabel(
    master = frame,
    text = "Cadastre um novo drone", 
    font = ("Georgia", 27),
    text_color = "#FFFFFF"      
    )
label.pack(pady = (30, 15), anchor = "w", padx = 40)

# --- Input "Imagem do Drone" ---
entry_imagem = customtkinter.CTkEntry(
    master = frame,
    placeholder_text = "Caminho da imagem do drone",
    **ENTRY_STYLE
)
entry_imagem.pack(pady = (12, 5), padx = 40)
# --- Imagem line ---
line_imagem = customtkinter.CTkFrame(
    master = frame,
    **LINES_STYLES
)
line_imagem.pack(padx = 40, fill = "x")

# --- Input "Número de Série" ---
entry_serial = customtkinter.CTkEntry(
    master = frame,
    placeholder_text = "Número de série",
    **ENTRY_STYLE
)
entry_serial.pack(pady = (12, 5), padx = 40)
# --- Serial line ---
line_serial = customtkinter.CTkFrame(
    master = frame,
    **LINES_STYLES
)
line_serial.pack(padx = 40, fill = "x")

# --- Radio Button "Status" ---
label_status = customtkinter.CTkLabel(
    master = frame,
    text = "Status:",
    font = ("Arial", 12)
)
label_status.pack(pady = (12, 5), padx = 40, anchor = "w")

status_var = customtkinter.StringVar(value = "Ativo")

radio_ativo = customtkinter.CTkRadioButton(
    master = frame,
    text = "Ativo",
    variable = status_var,
    value = "Ativo"
)
radio_ativo.pack(pady = 2, padx = 60, anchor = "w")

radio_inativo = customtkinter.CTkRadioButton(
    master = frame,
    text = "Inativo",
    variable = status_var,
    value = "Inativo"
)
radio_inativo.pack(pady = 2, padx = 60, anchor = "w")

radio_missao = customtkinter.CTkRadioButton(
    master = frame,
    text = "Em missão",
    variable = status_var,
    value = "Em missão"
)
radio_missao.pack(pady = 2, padx = 60, anchor = "w")

# --- Status line ---
line_status = customtkinter.CTkFrame(
    master = frame,
    **LINES_STYLES
)
line_status.pack(padx = 40, fill = "x", pady = (5, 0))

# --- Input "Marca" ---
entry_marca = customtkinter.CTkEntry(
    master = frame,
    placeholder_text = "Marca",
    **ENTRY_STYLE
)
entry_marca.pack(pady = (12, 5), padx = 40)
# --- Marca line ---
line_marca = customtkinter.CTkFrame(
    master = frame,
    **LINES_STYLES
)
line_marca.pack(padx = 40, fill = "x")

# --- Input "Fabricante" ---
entry_fabricante = customtkinter.CTkEntry(
    master = frame,
    placeholder_text = "Fabricante",
    **ENTRY_STYLE
)
entry_fabricante.pack(pady = (12, 5), padx = 40)
# --- Fabricante line ---
line_fabricante = customtkinter.CTkFrame(
    master = frame,
    **LINES_STYLES
)
line_fabricante.pack(padx = 40, fill = "x")

# --- Input "País de Origem" ---
entry_pais = customtkinter.CTkEntry(
    master = frame,
    placeholder_text = "País de origem",
    **ENTRY_STYLE
)
entry_pais.pack(pady = (12, 5), padx = 40)
# --- País line ---
line_pais = customtkinter.CTkFrame(
    master = frame,
    **LINES_STYLES
)
line_pais.pack(padx = 40, fill = "x")

# --- Input "Nível Atual da Bateria" ---
entry_bateria = customtkinter.CTkEntry(
    master = frame,
    placeholder_text = "Nível atual da bateria",
    **ENTRY_STYLE
)
entry_bateria.pack(pady = (12, 5), padx = 40)
# --- Bateria line ---
line_bateria = customtkinter.CTkFrame(
    master = frame,
    **LINES_STYLES
)
line_bateria.pack(padx = 40, fill = "x")

# --- Input "Taxa de Consumo de Bateria" ---
entry_taxa_bateria = customtkinter.CTkEntry(
    master = frame,
    placeholder_text = "Taxa de consumo de bateria",
    **ENTRY_STYLE
)
entry_taxa_bateria.pack(pady = (12, 5), padx = 40)
# --- Taxa Bateria line ---
line_taxa_bateria = customtkinter.CTkFrame(
    master = frame,
    **LINES_STYLES
)
line_taxa_bateria.pack(padx = 40, fill = "x")

# --- Input "Nível Atual de Combustível" ---
entry_combustivel = customtkinter.CTkEntry(
    master = frame,
    placeholder_text = "Nível atual de combustível",
    **ENTRY_STYLE
)
entry_combustivel.pack(pady = (12, 5), padx = 40)
# --- Combustível line ---
line_combustivel = customtkinter.CTkFrame(
    master = frame,
    **LINES_STYLES
)
line_combustivel.pack(padx = 40, fill = "x")

# --- Input "Taxa de Consumo de Combustível" ---
entry_taxa_combustivel = customtkinter.CTkEntry(
    master = frame,
    placeholder_text = "Taxa de consumo de combustível",
    **ENTRY_STYLE
)
entry_taxa_combustivel.pack(pady = (12, 5), padx = 40)
# --- Taxa Combustível line ---
line_taxa_combustivel = customtkinter.CTkFrame(
    master = frame,
    **LINES_STYLES
)
line_taxa_combustivel.pack(padx = 40, fill = "x")

# --- Input "Nível de Integridade" ---
entry_integridade = customtkinter.CTkEntry(
    master = frame,
    placeholder_text = "Nível de integridade",
    **ENTRY_STYLE
)
entry_integridade.pack(pady = (12, 5), padx = 40)
# --- Integridade line ---
line_integridade = customtkinter.CTkFrame(
    master = frame,
    **LINES_STYLES
)
line_integridade.pack(padx = 40, fill = "x")

btn_cadastrar = customtkinter.CTkButton(
    master = frame,
    text = "Cadastrar Drone",
    font = ("Arial", 16, "bold"),
    fg_color = "#2A6A7D",
    hover_color = "#1E4F5F",
    corner_radius = 8,
    height = 45
)
btn_cadastrar.pack(pady = (30, 40), padx = 40, fill = "x")

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