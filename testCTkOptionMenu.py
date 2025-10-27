import customtkinter as ctk

ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.geometry("300x300")

def item_selecionado(item):
    print(f"Item selecionado: {item}")

# Frame scrollable
scrollable_frame = ctk.CTkScrollableFrame(app, width=250, height=200)
scrollable_frame.pack(pady=20)

# Itens como botões
itens = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5", 
         "Item 6", "Item 7", "Item 8", "Item 9", "Item 10"]

for item in itens:
    btn = ctk.CTkButton(
        scrollable_frame,
        text=item,
        width=200,
        height=30,
        command=lambda i=item: item_selecionado(i)
    )
    btn.pack(pady=5)

app.mainloop()