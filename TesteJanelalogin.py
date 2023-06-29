import customtkinter as ctk
import openpyxl

# Aparência da janela
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

janela = ctk.CTk()
janela.geometry("500x300")

frame = ctk.CTkFrame(janela)
frame.pack(padx=10, pady=10)

resultado_label = ctk.CTkLabel(janela)
resultado_label.pack(pady=10)

usuario_label = ctk.CTkLabel(frame, text="Nome de Usuário:")
usuario_label.pack()

usuario_entry = ctk.CTkEntry(frame)
usuario_entry.pack(pady=5)

senha_label = ctk.CTkLabel(frame, text="Senha:")
senha_label.pack()

senha_entry = ctk.CTkEntry(frame, show="*")
senha_entry.pack(pady=5)

def verificar_login(usuario, senha):
    # Carregar o arquivo Excel
    workbook = openpyxl.load_workbook('C:/Users/Administrador/Desktop/Projetohelton/cadastro_usuarios.xlsx')
    sheet = workbook.active

    # Percorrer as linhas do arquivo para verificar o login
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if row[0] == usuario and row[1] == senha:
            return True  # Login bem-sucedido

    return False  # Login incorreto

def fazer_login():
    usuario_input = usuario_entry.get()
    senha_input = senha_entry.get()

    if verificar_login(usuario_input, senha_input):
        resultado_label.configure(text="Login bem-sucedido! Acesso permitido.")
        
        nova_janela = ctk.CTk()
        nova_janela.geometry("400x300")

        # Adicione widgets e defina a lógica específica para a nova janela
        import JanelaPesquisa

        nova_janela.mainloop()
    else:
        resultado_label.configure(text="Usuário ou senha incorretos. Tente novamente.")

botao = ctk.CTkButton(janela, text="Login", command=fazer_login)
botao.pack(pady=10)

janela.mainloop()
