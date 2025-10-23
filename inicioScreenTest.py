import customtkinter 
from cssInicioScreen import *
from PIL import Image
# --- imports ---

# --- Program appearance ---
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# --- Root configuration ---
root = customtkinter.CTk()
root.geometry("500x810")
root.resizable(False, False)
radio_var = customtkinter.IntVar(value=0)

def login():
    print("Test")

# =================== FRAMES ===================
# --- Main frame ---
frame = customtkinter.CTkFrame(
    master=root,
    fg_color = "#357E94",
    corner_radius = 0
    )
frame.pack(pady = 20, padx = 60, fill = "both", expand = True)
frame.pack_propagate(False)    

#headerFrame = customtkinter.CTkFrame(
#    master = root,
#    fg_color = "#357E94",
#    "corner_radius = 0
#)
#headerFrame.pack()
#headerFrame.pack_propagate(False)

#droneFrame = customtkinter.CTkFrame (
#    master = root,
#    fg_color = "#357E94",
#    corner_radius = 0
#)
#droneFrame.pack()
#droneFrame.pack_propagate(False)

# ==================== IMAGES ====================
try:
    # =================== image and label ===================
 
    # --- Menu image ---
    menu_image = customtkinter.CTkImage(
        dark_image = Image.open("menu.png"),     
        size = (35, 35)
    )

    # --- Menu image label ---
    menuImage_label = customtkinter.CTkLabel(
        master = frame,
        image = menu_image,
        text = ""
    )
    menuImage_label.grid(row = 1, column = 0, padx = (40, 0), pady = (0, 20), sticky = "w") 
 
    # --- Logo image ---
    logo_image = customtkinter.CTkImage(
        light_image = Image.open("duck.png"),
        dark_image = Image.open("duck.png"),
        size = (60, 60)
    )

    # --- Logo image label ---
    logoImage_label = customtkinter.CTkLabel(
        master = frame,
        image = logo_image,
        text = ""
    )
    logoImage_label.grid(row = 1, column = 1, padx = (40, 0), pady = (0, 20), sticky = "w")

    # --- User image ---
    user_image = customtkinter.CTkImage(
        dark_image = Image.open("user.png"),
        size = (35, 35)
    )

    # --- User image label ---
    userImage_label = customtkinter.CTkLabel(
        master = frame,
        image = user_image,
        text = ""

    ) 
    userImage_label.grid(row = 1, column = 2, padx = (40, 0), pady = (0, 20), sticky = "w")

except:
    pass

# ==================== MAIN FRAME ====================
# --- Bem vindo label ---
mainTitle = customtkinter.CTkLabel(
    master = frame,
    text = "Bem vindo(a) de volta!",
    **TITLE_LABEL_STYLE
)
mainTitle.pack()

# --- Descrição ---
description = customtkinter.CTkLabel(
    master = frame,
    text = "O que está procurando hoje?",
    **DESCRIPTION_LABEL_STYLE
)
description.pack()

#PATODEX, DRONES, APRENDER, SUPORTEn (imagens, nomes e grid)


# --- Drones title ---
droneTitle = customtkinter.CTkLabel(
    master = frame,
    text = "Mais acessados:"
)
droneTitle.pack()

#frame dos mais acessados

# =================== FOOTER (usado em todas as paginas) ===================

# 3 imagens, patodex, drones e usuario (sem texto)


root.mainloop()









