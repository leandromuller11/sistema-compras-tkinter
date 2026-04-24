import tkinter as tk
from tkinter import ttk

# ==================== PRODUTOS ====================
produtos = {
    "Martelo": 20,
    "Alicate": 25,
    "Chave de Fenda": 15
}

carrinho = []

def adicionar_item():
    try:
        produto = combo_produto.get()
        quantidade = int(entry_quantidade.get().strip())

        if not produto or quantidade <= 0:
            return

        preco = produtos[produto]
        total_item = preco * quantidade

        carrinho.append(total_item)

        tree.insert("", "end", values=(produto, quantidade, f"R${total_item:.2f}"))
        atualizar_total()
        
        entry_quantidade.delete(0, tk.END)
    except:
        pass

def remover_item():
    selecionado = tree.selection()
    if selecionado:
        item = tree.item(selecionado)
        try:
            valor_texto = item["values"][2]
            valor = float(valor_texto.replace("R$", "").replace(",", "."))
            carrinho.remove(valor)
            tree.delete(selecionado)
            atualizar_total()
        except:
            pass

def atualizar_total():
    total_geral = sum(carrinho)
    label_total.config(text=f"Total: R${total_geral:.2f}")

# ==================== JANELA ====================
janela = tk.Tk()
janela.title("Sistema de Compras")
janela.geometry("520x500")        # Aumentei um pouco a largura
janela.configure(bg="#1e1e1e")

# ==================== ESTILO ====================
style = ttk.Style()
style.theme_use("default")

# Estilo dos botões com bordas arredondadas
style.configure("TButton", 
                font=("Segoe UI", 10),
                padding=(12, 6),
                background="#3a3a3a",
                foreground="white")

# Tentar deixar as bordas mais arredondadas (funciona melhor em alguns temas)
style.map("TButton",
          background=[("active", "#4a4a4a")],
          foreground=[("active", "white")])

# Estilo dos labels
style.configure("TLabel", background="#1e1e1e", foreground="white", font=("Segoe UI", 10))

# ==================== FRAME SUPERIOR CINZA ====================
frame_superior = tk.Frame(janela, bg="#2d2d2d", height=80)
frame_superior.pack(fill="x", padx=15, pady=(15, 8))
frame_superior.pack_propagate(False)

# Produto
tk.Label(frame_superior, text="Produto", bg="#2d2d2d", fg="white", 
         font=("Segoe UI", 10, "bold")).place(x=15, y=10)

combo_produto = ttk.Combobox(frame_superior, values=list(produtos.keys()), 
                             font=("Segoe UI", 10), state="readonly")
combo_produto.place(x=15, y=37, width=210)

# Quantidade
tk.Label(frame_superior, text="Quantidade", bg="#2d2d2d", fg="white", 
         font=("Segoe UI", 10, "bold")).place(x=245, y=10)

entry_quantidade = tk.Entry(frame_superior, 
                            bg="white", 
                            fg="black", 
                            insertbackground="black", 
                            font=("Segoe UI", 10),
                            width=12,
                            justify="center")
entry_quantidade.place(x=245, y=37)

# Botões com mais distância entre eles
btn_add = ttk.Button(frame_superior, text="Adicionar", command=adicionar_item, style="TButton")
btn_add.place(x=380, y=33, width=90)

btn_remove = ttk.Button(frame_superior, text="Remover", command=remover_item, style="TButton")
btn_remove.place(x=480, y=33, width=90)   # Aumentei a distância

# ==================== TABELA ====================
tree = ttk.Treeview(janela, columns=("Produto", "Qtd", "Total"), show="headings")
tree.heading("Produto", text="Produto")
tree.heading("Qtd", text="Qtd")
tree.heading("Total", text="Total")

style.configure("Treeview", background="#1e1e1e", foreground="white", fieldbackground="#1e1e1e")
style.configure("Treeview.Heading", background="#2d2d2d", foreground="white")

tree.pack(fill="both", expand=True, padx=15, pady=10)

# Total
label_total = ttk.Label(janela, text="Total: R$0.00", font=("Segoe UI", 12, "bold"))
label_total.pack(pady=10)

janela.mainloop()