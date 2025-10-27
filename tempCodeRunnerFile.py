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
    placeholder_text = "Nível atual da bateria (%)",
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
    placeholder_text = "Taxa de consumo de bateria (%/h)",
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
    placeholder_text = "Nível atual de combustível (L)",
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
    placeholder_text = "Taxa de consumo de combustível (L/h)",
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
    placeholder_text = "Nível de integridade (%)",
    **ENTRY_STYLE
)
entry_integridade.pack(pady = (12, 5), padx = 40)
# --- Integridade line ---
line_integridade = customtkinter.CTkFrame(
    master = frame,
    **LINES_STYLES
)
line_integridade.pack(padx = 40, fill = "x")