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
    text="Aprenda sobre os patos",
    font=("Georgia", 24, "bold"),
    text_color="white"
)
droneTitle.pack(anchor="w", padx=25, pady=(0, 10))

# ==================== PATOS CONTAINER ====================
patoContainer = ctk.CTkScrollableFrame(
    master=frame,
    fg_color="transparent",
    scrollbar_button_color="#DCE7F6",    
)
patoContainer.pack(fill="both", padx=15, pady=(0, 10), expand=True)

# ==================== PATOS SOBRE ====================
# Lista de informações sobre patos baseada no texto fornecido
patos_info = [
    {
        "titulo": "1. Visão Geral",
        "descricao": "Os Patos Primordiais são espécimes únicos, similares a patos em alguns traços, mas com morfologias, poderes e níveis de mutação que os tornam alvos de altíssimo interesse científico (e, frequentemente, perigosos).\n\nNossos drones com tecnologia alienígena vasculham o planeta apenas com sensores óticos (câmeras) e registram dados padronizados que alimentam o catálogo central.\n\nA partir dessas informações, avaliamos valor científico, custo operacional e risco para decidir se enviamos equipes de captura.\n\n "
    },
    {
        "titulo": "2. Anatomia & Comportamento",
        "descricao": "• TAMANHO: Varia do porte de um pato comum até vários metros de altura\n\n• PESO: Amplo espectro — animais leves a colossos maciços\n\n• ESTADOS COMPORTAMENTAIS:\n   - Hibernação: Mínimo movimento; abordagem de baixo risco\n   - Transe: Reduzido, mas sensível; drones medem batimentos cardíacos (bpm)\n   - Desperto: Ativo e potencialmente agressivo; pode ter super-poder detectável\n\n• TRANSMISSÃO: Padrões (luminosidade ocular, tremores musculares, som) preveem mudança de estado\n\n "
    },
    {
        "titulo": "3. Características Especiais",
        "descricao": "Os Patos Primordiais possuem características únicas que os distinguem dos patos comuns:\n\n• Morfologias variadas e adaptadas a diferentes ambientes\n• Níveis de mutação que conferem habilidades especiais\n• Sensibilidade a diferentes estímulos ambientais\n• Comportamentos complexos que requerem estudo aprofundado\n• Capacidade de alterar estados de consciência rapidamente\n• Resistência física além do comum para sua classe\n\n "
    },
    {
        "titulo": "4. Procedimentos de Observação",
        "descricao": "A observação dos Patos Primordiais segue protocolos rigorosos:\n\n• Uso exclusivo de drones com sensores óticos para evitar contato direto\n• Monitoramento contínuo dos estados comportamentais\n• Análise de padrões de luminosidade ocular e atividade muscular\n• Avaliação de risco baseada em múltiplos parâmetros\n• Registro detalhado de todas as interações ambientais\n• Protocolos de segurança para equipes de captura\n\n "
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
for pato in patos_info:
    altura_card = calcular_altura_texto(pato["descricao"])
    
    # Container com cantos arredondados
    patoCard = ctk.CTkFrame(
        master=patoContainer,
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

# ==================== SEÇÃO DE COMPARAÇÃO ====================
# Título da seção
comparacaoTitle = ctk.CTkLabel(
    master=patoContainer,
    text="Como diferenciar um Pato \n Primordial de um Pato Comum",
    font=("Georgia", 18, "bold"),
    text_color="white"
)
comparacaoTitle.pack(anchor="w", pady=(20, 15), padx = (27, 0))

# Container da grid 2x2
gridContainer = ctk.CTkFrame(
    master=patoContainer,
    fg_color="transparent"
)
gridContainer.pack(fill="x", pady=(0, 20))

# Configurar grid 2x2
gridContainer.grid_columnconfigure(0, weight=1)
gridContainer.grid_columnconfigure(1, weight=1)
gridContainer.grid_rowconfigure(0, weight=1)
gridContainer.grid_rowconfigure(1, weight=1)

# Linha 1 - Fotos
try:
    # Pato comum (esquerda)
    patoComum_image = ctk.CTkImage(
        dark_image=Image.open("patoFoto.jpeg"),
        size=(120, 120)
    )
    patoComum_label = ctk.CTkLabel(
        master=gridContainer,
        image=patoComum_image,
        text=""
    )
    patoComum_label.grid(row=0, column=0, padx=10, pady=5)
    
    # Pato primordial (direita)
    patoPrimordial_image = ctk.CTkImage(
        dark_image=Image.open("patoPrimordialFoto.jpg"),
        size=(120, 120)
    )
    patoPrimordial_label = ctk.CTkLabel(
        master=gridContainer,
        image=patoPrimordial_image,
        text=""
    )
    patoPrimordial_label.grid(row=0, column=1, padx=10, pady=5)

except Exception as e:
    print(f"Erro ao carregar imagens de comparação: {e}")
    
    # Placeholder se as imagens não existirem
    placeholderComum = ctk.CTkLabel(
        master=gridContainer,
        text="🦆",
        font=("Arial", 50),
        text_color="white"
    )
    placeholderComum.grid(row=0, column=0, padx=10, pady=5)
    
    placeholderPrimordial = ctk.CTkLabel(
        master=gridContainer,
        text="🔥🦆",
        font=("Arial", 50),
        text_color="white"
    )
    placeholderPrimordial.grid(row=0, column=1, padx=10, pady=5)

# Linha 2 - Textos
# Pato comum (esquerda)
textoComum = ctk.CTkLabel(
    master=gridContainer,
    text="Pato Comum",
    font=("Georgia", 16, "bold"),
    text_color="white"
)
textoComum.grid(row=1, column=0, padx=10, pady=5)

# Pato primordial (direita)
textoPrimordial = ctk.CTkLabel(
    master=gridContainer,
    text="Pato Primordial",
    font=("Georgia", 16, "bold"),
    text_color="#FF6B6B"  # Cor diferente para destacar
)
textoPrimordial.grid(row=1, column=1, padx=10, pady=5)

# ==================== BOTÃO PRÓXIMO ====================
botaoProximo_frame = ctk.CTkFrame(
    master=patoContainer,
    fg_color="transparent"
)
botaoProximo_frame.pack(fill="x", pady=(20, 10))

botaoProximo = ctk.CTkButton(
    master=botaoProximo_frame,
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