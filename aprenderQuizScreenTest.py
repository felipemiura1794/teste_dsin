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
# ==================== QUIZ CONTAINER ====================
quizContainer = ctk.CTkScrollableFrame(
    master=frame,
    fg_color="transparent",
    scrollbar_button_color="#DCE7F6",    
)
quizContainer.pack(fill="both", padx=10, pady=(0, 10), expand=True)

def calcular_altura_texto(texto, largura_max=300, altura_linha=15):
    linhas = texto.split('\n')
    altura_minima = 120
    

    total_linhas = 0
    for linha in linhas:
        if len(linha) > 45:
            total_linhas += max(1, len(linha) // 45)
        else:
            total_linhas += 1
    
    altura_calculada = total_linhas * altura_linha + 60
    
    return max(altura_minima, altura_calculada)

# ==================== INTRODUÇÃO DO QUIZ ====================
introCard = ctk.CTkFrame(
    master=quizContainer,
    fg_color="#5BA4B8",
    corner_radius=25,
    height=160
)
introCard.pack(fill="x", pady=(0, 20))
introCard.pack_propagate(False)

# Padding interno
introCard_inner = ctk.CTkFrame(
    master=introCard,
    fg_color="transparent"
)
introCard_inner.pack(fill="both", expand=True, padx=15, pady=15)

# Texto de introdução
introTexto = ctk.CTkLabel(
    master=introCard_inner,
    text="Agora que você leu (né?) como funciona os Patos Primordiais, os drones e o controle, você fará um pequeno quiz de 6 perguntas para testar seus conhecimentos.\n\nEste trabalho é extremamente importante para a segurança da Terra.\n\nEstá pronto? Então comece!",
    font=("Arial", 14),
    text_color="white",
    anchor="nw",
    justify="left",
    wraplength=320
)
introTexto.pack(anchor="w", fill="both", expand=True)

# ==================== QUIZ INTERATIVO ====================
quizTitle = ctk.CTkLabel(
    master=quizContainer,
    text="Quiz - DuckTracker",
    font=("Georgia", 24, "bold"),
    text_color="white"
)
quizTitle.pack(anchor="c", padx=25, pady=(0, 15))

# Lista de perguntas do quiz
perguntas_quiz = [
    {
        "categoria": "Patos Primordiais",
        "pergunta": "Qual é a principal característica que diferencia um Pato Primordial de um pato comum?",
        "opcoes": [
            "A) Tamanho maior e cores mais vibrantes",
            "B) Morfologias, poderes e níveis de mutação únicos", 
            "C) Capacidade de falar e se comunicar"
        ],
        "resposta_correta": 1
    },
    {
        "categoria": "Patos Primordiais", 
        "pergunta": "Qual estado comportamental apresenta o MAIOR risco durante a abordagem?",
        "opcoes": [
            "A) Hibernação - mínimo movimento",
            "B) Transe - reduzido mas sensível", 
            "C) Desperto - ativo e potencialmente agressivo"
        ],
        "resposta_correta": 2
    },
    {
        "categoria": "Drones",
        "pergunta": "Qual tecnologia NÃO faz parte dos sensores dos drones?",
        "opcoes": [
            "A) GPS de alta precisão (4cm a 30m)",
            "B) Sensores e scanner de dados",
            "C) Scanner de pensamento"
        ],
        "resposta_correta": 2
    },
    {
        "categoria": "Drones",
        "pergunta": "O que o algoritmo de visão computacional dos drones é capaz de fazer?",
        "opcoes": [
            "A) Apenas detectar a presença de patos",
            "B) Detecção, estimativa de tamanho, classificação de estado e reconhecimento de super-poderes",
            "C) Controlar remotamente o comportamento dos patos"
        ],
        "resposta_correta": 1
    },
    {
        "categoria": "Controle",
        "pergunta": "O que acontece quando o drone atinge o raio de proximidade de um Pato Primordial?",
        "opcoes": [
            "A) Automaticamente inicia a captura",
            "B) A interface propõe 'Entrar na Tela de Captura'",
            "C) O drone retorna automaticamente à base"
        ],
        "resposta_correta": 1
    },
    {
        "categoria": "Controle", 
        "pergunta": "Qual fator NÃO influencia no cálculo de dificuldade de captura?",
        "opcoes": [
            "A) Cor da plumagem do pato",
            "B) Estado comportamental (Desperto/Transe/Hibernação)",
            "C) BPM e quantidade de mutações"
        ],
        "resposta_correta": 0
    }
]

# Cards quiz
for i, pergunta in enumerate(perguntas_quiz):
    # Card container
    quizCard = ctk.CTkFrame(
        master=quizContainer,
        fg_color="#5BA4B8",
        corner_radius=25,
        height=200
    )
    quizCard.pack(fill="x", pady=(0, 15))
    quizCard.pack_propagate(False)
    
    # Padding interno
    quizCard_inner = ctk.CTkFrame(
        master=quizCard,
        fg_color="transparent"
    )
    quizCard_inner.pack(fill="both", expand=True, padx=15, pady=15)
    
    # Categoria
    categoriaLabel = ctk.CTkLabel(
        master=quizCard_inner,
        text=pergunta["categoria"],
        font=("Arial", 12, "bold"),
        text_color="#E8F4F8",
        anchor="w"
    )
    categoriaLabel.pack(anchor="w", pady=(0, 5))
    
    # Pergunta
    perguntaLabel = ctk.CTkLabel(
        master=quizCard_inner,
        text=pergunta["pergunta"],
        font=("Arial", 14, "bold"),
        text_color="white",
        anchor="w",
        justify="left",
        wraplength=320
    )
    perguntaLabel.pack(anchor="w", pady=(0, 8))
    
    # Variável para armazenar a resposta selecionada
    resposta_var = ctk.IntVar(value=-1)
    
    # Opções de resposta (radio buttons)
    for j, opcao in enumerate(pergunta["opcoes"]):
        radio_btn = ctk.CTkRadioButton(
            master=quizCard_inner,
            text=opcao,
            variable=resposta_var,
            value=j,
            font=("Arial", 12),
            text_color="#E8F4F8",
            fg_color="#FFFFFF",
            hover_color = "#ACACAC",
            border_color = "#FFFFFF",  
        )
        radio_btn.pack(anchor="w", pady=1)

# Botão resultado
resultadoProximo_frame = ctk.CTkFrame(
    master=quizContainer,
    fg_color="transparent"
)
resultadoProximo_frame.pack(fill="x", pady=(20, 10))

resultadoProximo_frame = ctk.CTkButton(
    master=resultadoProximo_frame,
    text="Resultado >",
    font=("Arial", 14, "bold"),
    fg_color="#5BA4B8",
    hover_color="#4A8FA0",
    text_color="white",
    width=120,
    height=35,
    corner_radius=20
)
resultadoProximo_frame.pack(side="right", padx=20)
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