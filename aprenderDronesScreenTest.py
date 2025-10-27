import customtkinter as ctk
from PIL import Image

# --- Aparência do programa ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

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
    menu_image = ctk.CTkImage(
        dark_image=Image.open("menu.png"),    
        size=(35, 35)
    )
    menuImage_label = ctk.CTkLabel(
        master=headerFrame,
        image=menu_image,
        text=""
    )
    menuImage_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")
    
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
    logoImage_label.grid(row=0, column=1, pady=20)
    
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
    userImage_label.grid(row=0, column=2, padx=20, pady=20, sticky="e")
    
except Exception as e:
    print(f"Erro ao carregar imagens: {e}")

# =================== FRAME MAIN ===================
frame = ctk.CTkFrame(
    master=root,
    fg_color="#357E94",
    corner_radius=0
)
frame.pack(fill="both", expand=True, padx=0, pady=(30,0))

# ==================== CONTEUDO MAIN ====================
# ----- Seção título -----
droneTitle = ctk.CTkLabel(
    master=frame,
    text="Aprenda sobre os drones",
    font=("Georgia", 24, "bold"),
    text_color="white"
)
droneTitle.pack(anchor="w", padx=25, pady=(0, 10))

# ==================== DRONES CONTAINER ====================
droneContainer = ctk.CTkScrollableFrame(
    master=frame,
    fg_color="transparent",
    scrollbar_button_color="#DCE7F6",    
)
droneContainer.pack(fill="both", padx=15, pady=(0, 10), expand=True)

# ==================== DRONES SOBRE ====================
# Lista de informações sobre drones
drones_info = [
    {
        "titulo": "Sobre os Drones",
        "descricao": "Os drones são a espinha dorsal do projeto: aparelhos construídos com tecnologia humana e alienígena para localizar, observar e (quando autorizados) capturar Patos Primordiais.\n\nEles operam em várias classes de missão e possuem sensores, protocolos de comunicação e regras de segurança integradas.\n\n "
    },
    {
        "titulo": "Sensores e Equipamentos",
        "descricao": "• GPS com precisão variável (4 cm a 30 m)\n• IMU / acelerômetros para estabilização e manobras\n• Microfones e sensores térmicos para detectar atividade muscular e calor\n• Câmeras de alta resolução com visão noturna\n• Sensores de movimento e proximidade\n• Sistemas de comunicação segura\n\n "
    },
    {
        "titulo": "Inteligência Artificial",
        "descricao": "Algoritmos de visão computacional que realizam:\n\n• Detecção de espécime em tempo real\n• Estimativa de altura/peso automática\n• Classificação de estado (desperto/transe/hibernação)\n• Reconhecimento de super-poderes por padrão visual\n• Análise de comportamento e padrões de movimento\n• Detecção de ameaças e avaliação de risco\n\n "
    },
    {
        "titulo": "Sistema de Operações",
        "descricao": "• Telemetria em tempo real para enviar dados ao servidor central\n• Conversão automática de unidades (ft, lb, yd → métrico)\n• Prioridade de integridade: rotas de fuga automáticas\n• Zonas de exclusão quando detecção de risco alto\n• Atualização automática da Patodex\n• Protocolos de segurança multi-camada\n\n "
    },
    {
        "titulo": "Entrega de Dados",
        "descricao": "Cada observação enviada inclui:\n\n• ID do drone e fabricante\n• Timestamp e localização com precisão\n• Medidas (unidade original + valor convertido)\n• Status comportamental e BPM se disponível\n• Mutações estimadas e detecção de super-poder\n• Classificação de risco e nome/descrição do poder\n• O servidor central normaliza e exibe no catálogo\n\n "
    }
]

# Função para calcular altura necessária baseada no texto
def calcular_altura_texto(texto, largura_max=300, altura_linha=15):
    """Calcula a altura necessária baseada no comprimento do texto"""
    palavras = texto.split()
    linhas = []
    linha_atual = []
    
    for palavra in palavras:
        linha_atual.append(palavra)
        linha_texto = ' '.join(linha_atual)
        # Estimativa simples baseada em caracteres por linha
        if len(linha_texto) > 45:  # Aproximadamente 45 caracteres por linha
            linhas.append(' '.join(linha_atual[:-1]))
            linha_atual = [palavra]
    
    if linha_atual:
        linhas.append(' '.join(linha_atual))
    
    altura_minima = 120  # Altura mínima do card
    altura_calculada = len(linhas) * altura_linha + 80  # 80px para título e margens
    
    return max(altura_minima, altura_calculada)

# Criar cards para cada pato
for pato in drones_info:
    altura_card = calcular_altura_texto(pato["descricao"])
    
    # Container com cantos arredondados
    patoCard = ctk.CTkFrame(
        master=droneContainer,
        fg_color="#5BA4B8",
        corner_radius=25,
        height=altura_card
    )
    patoCard.pack(fill="x", pady=(0, 15))
    patoCard.pack_propagate(False)
    
    # Padding interno
    patoCard_inner = ctk.CTkFrame(
        master=patoCard,
        fg_color="transparent"
    )
    patoCard_inner.pack(fill="both", expand=True, padx=15, pady=15)
    
    # Título do pato
    patoTitulo = ctk.CTkLabel(
        master=patoCard_inner,
        text=pato["titulo"],
        font=("Georgia", 18, "bold"),
        text_color="white",
        anchor="w"
    )
    patoTitulo.pack(anchor="w", pady=(0, 10))
    
    # Descrição do pato
    patoDescricao = ctk.CTkLabel(
        master=patoCard_inner,
        text=pato["descricao"],
        font=("Arial", 12),
        text_color="#E8F4F8",
        anchor="nw",
        justify="left",
        wraplength=310
    )
    patoDescricao.pack(anchor="w", fill="both", expand=True)

# ==================== BOTÃO PRÓXIMO E VOLTAR ====================
botoes_frame = ctk.CTkFrame(
    master=droneContainer,
    fg_color="transparent"
)
botoes_frame.pack(anchor = "e", pady=(20, 10))

botaovoltar = ctk.CTkButton(
    master=botoes_frame,
    text="< Voltar",
    font=("Arial", 14, "bold"),
    fg_color="#5BA4B8",
    hover_color="#4A8FA0",
    text_color="white",
    width=120,
    height=35,
    corner_radius=20
)
botaovoltar.pack(side="left", padx=(0, 53))

botaoProximo = ctk.CTkButton(
    master=botoes_frame,
    text="Próximo >",
    font=("Arial", 14, "bold"),
    fg_color="#5BA4B8",
    hover_color="#4A8FA0",
    text_color="white",
    width=120,
    height=35,
    corner_radius=20
)
botaoProximo.pack(side="right", padx=20)
# =================== FOOTER (Pode ser usado em todas as paginas) ===================
footerFrame = ctk.CTkFrame(
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
    patodexMenu_image = ctk.CTkImage(
        dark_image=Image.open("patodexVetor.png"),    
        size=(40, 40)
    )
    patodexMenu_image_label = ctk.CTkLabel(
        master=footerFrame,
        image=patodexMenu_image,
        text=""
    )
    patodexMenu_image_label.grid(row=0, column=0, padx=20, pady=30, sticky="")
    
    # --- Drones imagem ---
    droneMenu_image = ctk.CTkImage(
        dark_image=Image.open("droneVetor.png"),
        size=(40, 40)
    )
    droneMenu_image_label = ctk.CTkLabel(
        master=footerFrame,
        image=droneMenu_image, 
        text=""
    )
    droneMenu_image_label.grid(row=0, column=1, pady=30, sticky="")
    
    # --- Usuário imagem ---
    user2_image = ctk.CTkImage(
        dark_image=Image.open("userVetor.png"),
        size=(40, 40)
    )
    user2Image_label = ctk.CTkLabel(
        master=footerFrame,
        image=user2_image,
        text=""
    )
    user2Image_label.grid(row=0, column=2, padx=20, pady=30, sticky="")
    
except Exception as e:
    print(f"Erro ao carregar imagens do footer: {e}")

root.mainloop()