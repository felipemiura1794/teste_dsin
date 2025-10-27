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

# Função para calcular altura necessária baseada no texto
def calcular_altura_texto(texto, largura_max=300, altura_linha=15):
    """Calcula a altura necessária baseada no comprimento do texto"""
    linhas = texto.split('\n')
    altura_minima = 120  # Altura mínima do card
    
    # Calcula quantas linhas de texto temos
    total_linhas = 0
    for linha in linhas:
        # Estimativa: cada linha com mais de 45 caracteres pode quebrar
        if len(linha) > 45:
            total_linhas += max(1, len(linha) // 45)
        else:
            total_linhas += 1
    
    altura_calculada = total_linhas * altura_linha + 60  # 60px para título e margens
    
    return max(altura_minima, altura_calculada)

# ==================== PATOS SOBRE ====================
# Lista de informações sobre controle de drones (conteúdo ORIGINAL completo)
controles_info = [
    {
        "titulo": "Controle de Drones - Visão Geral",
        "descricao": "Esta aba explica a interface principal que o usuário verá ao pilotar um drone e ao tentar capturar um Pato Primordial. A experiência foi pensada para ser intuitiva e eficiente para operações de campo.\n\n "
    },
    {
        "titulo": "Tela Principal",
        "descricao": "• MAPA INTERATIVO: Mostra sua posição, locais e ícones de avistamentos de Patos Primordiais\n\n• RADAR: Indicador que mostra a distância até o pato mais próximo e sua direção relativa ao drone\n\n• BARRA DE TELEMETRIA: Exibe bateria (%), combustível/energia restante, integridade estrutural do drone (%)\n\n "
    },
    {
        "titulo": "Sistema de Aproximação",
        "descricao": "Ao atingir um raio de proximidade, a interface automaticamente propõe 'Entrar na Tela de Captura'.\n\nAo confirmar, você é direcionado para a tela onde todos os dados do pato estão organizados para análise e ação.\n\n "
    },
    {
        "titulo": "Tela de Captura - Ficha Técnica",
        "descricao": "• Nome/ID do registro e drone que coletou\n• Localização (cidade, país + coordenadas) e precisão\n• Altura (cm) e Peso (g) - com unidade original e conversão\n• Status: Desperto / Transe / Hibernação Profunda\n• BPM (se disponível) e Mutações (índice)\n• Super-poder detectado: nome, descrição e classificação\n• Indicador de Dificuldade de Captura\n\n "
    },
    {
        "titulo": "Sugestões Táticas",
        "descricao": "A interface recomenda ações automaticamente baseadas no motor de regras táticas:\n\n• 'Atacar de cima'\n• 'Usar rede eletromagnética'\n• 'Manter distância e observar'\n• 'Aguardar momento oportuno'\n• 'Chamar reforços'\n\n "
    },
    {
        "titulo": "Ações Disponíveis",
        "descricao": "• APROXIMAR / RECUAR - Controla distância do alvo\n\n• INICIAR CAPTURA - Prepara sistemas de captura\n\n• SIMULAR TÁTICA - Roda simulação rápida de sucesso/fracasso\n\n• ABORTAR - Volta ao mapa principal\n\n• CAPTURAR / NEUTRALIZAR - Executa ação de captura\n\n• ARMAZENAR NA PATODEX - Salva dados após captura bem-sucedida\n\n "
    },
    {
        "titulo": "Cálculo de Dificuldade",
        "descricao": "O sistema calcula dificuldade baseado em:\n\n• Estado (Desperto > Transe > Hibernação)\n• Tamanho + peso (alvos grandes = mais difícil)\n• BPM alto → chance de despertar\n• Quantidade de mutações\n• Classificação do super-poder\n• Precisão GPS disponível\n\nCLASSIFICAÇÃO:\nFácil • Médio • Difícil • Impossível/Abortar\n\n "
    },
    {
        "titulo": "Sistema Patodex",
        "descricao": "Ao armazenar, o registro entra na sua Patodex com:\n\n• Ficha completa do espécime\n• Dados de captura e localização\n• Mídia coletada durante a operação\n• Carimbo temporal da captura\n\nFILTROS DISPONÍVEIS:\nPrioridade, classificação de poder, região e data\n\n "
    }
]

# Criar cards para cada pato
for pato in controles_info:
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