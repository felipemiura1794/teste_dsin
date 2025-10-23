# =============================================================================
# IMPORTAÇÕES
# =============================================================================
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk


# =============================================================================
# CONFIGURAÇÃO DO CUSTOMTKINTER
# =============================================================================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# =============================================================================
# CLASSE PRINCIPAL DO APLICATIVO
# =============================================================================
class App:
    def __init__(self):
        """
        Inicializa a aplicação e configura a janela principal.
        """
        self.configurar_janela()
        self.criar_canvas()
        self.carregar_imagens()
        self.criar_elementos()
    
    def configurar_janela(self):
        """
        Configura a janela principal com tamanho fixo e centralizada.
        """
        self.root = tk.Tk()
        self.root.title("DuckTracker - Bem Vindo")
        self.root.geometry("402x874")
        self.root.resizable(False, False)
    
    def criar_canvas(self):
        """
        Cria o canvas que servirá como base para todos os elementos visuais.
        """
        self.canvas = tk.Canvas(
            self.root, 
            width=402, 
            height=874, 
            highlightthickness=0, 
            bd=0
        )
        self.canvas.pack(fill="both", expand=True)
    
    def carregar_imagens(self):
        """
        Carrega e posiciona as imagens de fundo e logo.
        """
        try:
            # Imagem de fundo (gradiente)
            gradiente_fundo = Image.open("gradiente.png")  
            gradiente_fundo = gradiente_fundo.resize((1902, 1450), Image.Resampling.LANCZOS)
            self.imagem_fundo = ImageTk.PhotoImage(gradiente_fundo)
            
            # Logo do aplicativo
            imagem_logo = Image.open("duck.png") 
            imagem_logo = imagem_logo.resize((250, 250), Image.Resampling.LANCZOS)
            self.imagem_logo = ImageTk.PhotoImage(imagem_logo)
            
            # Posiciona as imagens no canvas
            self.canvas.create_image(-800, -290, image=self.imagem_fundo, anchor="nw")
            self.canvas.create_image(201, 180, image=self.imagem_logo)
            
        except Exception as e:
            print(f"Erro ao carregar imagens: {e}")
            # Fallback: cor sólida se as imagens não carregarem
            self.canvas.configure(bg='#3B8CA2')
    
    def criar_elementos(self):
        """
        Cria todos os elementos de interface (textos, botões, links).
        """
        self.criar_textos()
        self.criar_botoes()
        self.criar_link_cadastro()
    
    def criar_textos(self):
        """
        Cria os textos estáticos da tela inicial.
        """
        # Título principal
        self.canvas.create_text(
            201, 360, 
            text="Bem vindo(a)!", 
            font=("Alegreya", 28, "bold"),
            fill="white"
        )

        # Descrição do aplicativo
        self.canvas.create_text(
            201, 430, 
            text="Problemas com os patos primordiais? \n Nós temos a solução!", 
            font=("Alegreya Sans", 13, "normal"),
            fill="white",
            justify="center",
            width=380  # Limita a largura do texto
        )
    
    def criar_botoes(self):
        """
        Cria os botões  da interface.
        """
        botao_login_email = ctk.CTkButton(
            self.root, 
            text="Login com Email",
            command=self.ir_para_login,
            fg_color="#44959E",   
            bg_color="#153C4C",      
            hover_color="#3A7F88",   
            text_color="white",
            font=("Alegreya Sans", 20, "normal"),
            corner_radius=15,        
            width=300,
            height=60
        )
        
        # Posiciona o botão no canvas
        self.canvas.create_window(201, 620, window=botao_login_email)
    
    def criar_link_cadastro(self):
        """
        Cria o link 'Cadastre-se' com interação de clique.
        """
        # Container para os textos
        frame_cadastro = ctk.CTkFrame(self.root, fg_color="transparent")

        # Texto estático
        label_texto = tk.Label(
            frame_cadastro,
            text="Não tem uma conta? ",
            font=("Alegreya Sans", 12, "normal"),
            bg="#103241",
            fg="#FFFFFF",
        )
        label_texto.pack(side="left")
        
        # Link clicável
        label_link = tk.Label(
            frame_cadastro,
            text="Cadastre-se",
            font=("Alegreya Sans", 12, "bold"),
            bg="#103241",
            fg="#FFFFFF",
            cursor="hand2", 
        )
        label_link.pack(side="left")

        # Vincula o evento de clique à função
        label_link.bind("<Button-1>", lambda e: self.ir_para_cadastro())
        
        # Posiciona o container no canvas
        self.canvas.create_window(201, 680, window=frame_cadastro)

    # =========================================================================
    # FUNÇÕES DE NAVEGAÇÃO
    # =========================================================================
    
    def ir_para_cadastro(self):
        """
        Navega para a tela de cadastro.
        """

        
        print("Navegando para cadastro...")
        

    def ir_para_login(self):
        """
        Navega para a tela de login.
        """
        print("Navegando para login...")
        
        import sys
        import os
        
        # Adiciona o caminho absoluto para a pasta screens
        screens_path = os.path.join(os.path.dirname(__file__))
        if screens_path not in sys.path:
            sys.path.append(screens_path)
        
        # Agora importa
        from login_screen import setup
        
        # Limpa a tela atual
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.destroy()  # Oculta a janela atual
        
        # Chama a tela de login
        setup()


    
    def run(self):
        """
        Inicia o loop principal da aplicação.
        """
        self.root.mainloop()

# =============================================================================
# PONTO DE ENTRADA DA APLICAÇÃO
# =============================================================================
if __name__ == "__main__":
    app = App()
    app.run()