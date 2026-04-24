import tkinter as tk
from tkinter import ttk

# ==================== PRODUTOS ====================
produtos = {
    "Arroz 5kg": 28.90, "Feijão 1kg": 8.50, "Macarrão 500g": 4.20,
    "Açúcar 1kg": 4.80, "Sal 1kg": 2.50, "Óleo de Soja 900ml": 7.90,
    "Leite 1L": 5.50, "Café 500g": 16.90, "Pão de Forma": 8.00,
    "Manteiga 200g": 9.50, "Margarina 500g": 6.00,
    "Queijo Mussarela 1kg": 38.00, "Presunto 1kg": 32.00,
    "Frango 1kg": 12.90, "Carne Bovina 1kg": 39.90,
    "Ovos (30 unidades)": 18.00, "Banana 1kg": 5.00,
    "Maçã 1kg": 7.50, "Batata 1kg": 4.50, "Tomate 1kg": 6.00,
    "Cebola 1kg": 4.00, "Alho 100g": 3.50, "Cenoura 1kg": 3.80,
    "Alface": 2.50, "Refrigerante 2L": 9.00, "Suco 1L": 6.50,
    "Água 1.5L": 3.00, "Biscoito Recheado": 3.20,
    "Bolacha Água e Sal": 4.00, "Chocolate Barra": 6.00,
    "Sabão em Pó 1kg": 12.00, "Detergente": 2.80,
    "Esponja": 1.50, "Papel Higiênico 12 rolos": 18.00,
    "Shampoo": 12.90, "Condicionador": 13.90,
    "Creme Dental": 4.50, "Sabonete": 2.50,
    "Desodorante": 11.00, "Álcool 70%": 6.00
}

carrinho = []

# ==================== FUNÇÕES ====================
def buscar_produto():
    texto = entry_busca.get().lower().strip()
    filtrados = [p for p in produtos if texto in p.lower()]
    combo_produto["values"] = filtrados

    if filtrados:
        combo_produto.set(filtrados[0])

def adicionar_item():
    try:
        produto = combo_produto.get()
        quantidade = int(entry_quantidade.get())

        if not produto or quantidade <= 0:
            return

        preco = produtos[produto]
        total = preco * quantidade

        carrinho.append(total)

        tree.insert("", "end", values=(produto, quantidade, f"R${total:.2f}"))
        atualizar_total()

        entry_quantidade.delete(0, tk.END)
    except:
        pass

def remover_item():
    selecionado = tree.selection()
    if selecionado:
        item = tree.item(selecionado)
        valor = float(item["values"][2].replace("R$", ""))
        carrinho.remove(valor)
        tree.delete(selecionado)
        atualizar_total()

def atualizar_total():
    label_total.config(text=f"Total: R${sum(carrinho):.2f}")

# ==================== BOTÃO ARREDONDADO ====================
def criar_botao(parent, texto, comando, x, y):
    btn = tk.Label(parent,
                   text=texto,
                   bg="#3a3a3a",
                   fg="white",
                   font=("Segoe UI", 10, "bold"),
                   padx=15,
                   pady=6,
                   cursor="hand2")

    btn.place(x=x, y=y)

    # hover
    btn.bind("<Enter>", lambda e: btn.config(bg="#4a4a4a"))
    btn.bind("<Leave>", lambda e: btn.config(bg="#3a3a3a"))

    # clique
    btn.bind("<Button-1>", lambda e: comando())

    return btn

# ==================== JANELA ====================
janela = tk.Tk()
janela.title("Sistema de Compras PRO")
janela.geometry("550x550")
janela.configure(bg="#1e1e1e")

style = ttk.Style()
style.theme_use("default")

style.configure("TLabel", background="#1e1e1e", foreground="white", font=("Segoe UI", 10))

# ==================== FRAME ====================
frame = tk.Frame(janela, bg="#2d2d2d", height=100)
frame.pack(fill="x", padx=15, pady=10)
frame.pack_propagate(False)

# 🔍 Busca
tk.Label(frame, text="Buscar produto", bg="#2d2d2d", fg="white").place(x=10, y=5)

entry_busca = tk.Entry(frame)
entry_busca.place(x=10, y=25, width=180)
entry_busca.bind("<KeyRelease>", lambda e: buscar_produto())

# botão lupa
btn_buscar = tk.Button(frame, text="🔍", command=buscar_produto,
                       bg="#3a3a3a", fg="white")
btn_buscar.place(x=195, y=25, width=30)

# Produto
tk.Label(frame, text="Produto", bg="#2d2d2d", fg="white").place(x=240, y=5)

combo_produto = ttk.Combobox(frame, values=list(produtos.keys()))
combo_produto.place(x=240, y=25, width=200)

# Quantidade
tk.Label(frame, text="Qtd", bg="#2d2d2d", fg="white").place(x=450, y=5)

entry_quantidade = tk.Entry(frame, width=5)
entry_quantidade.place(x=450, y=25)

# Botões arredondados
criar_botao(frame, "Adicionar", adicionar_item, 10, 60)
criar_botao(frame, "Remover", remover_item, 120, 60)

# ==================== TABELA ====================
tree = ttk.Treeview(janela, columns=("Produto", "Qtd", "Total"), show="headings")
tree.heading("Produto", text="Produto")
tree.heading("Qtd", text="Qtd")
tree.heading("Total", text="Total")
tree.pack(fill="both", expand=True, padx=15, pady=10)

# Total
label_total = ttk.Label(janela, text="Total: R$0.00", font=("Segoe UI", 12, "bold"))
label_total.pack(pady=10)

janela.mainloop()