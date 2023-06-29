import customtkinter


# Aparência da janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x300")

def cadastrar():
    nova_janela = customtkinter.CTk()
    nova_janela.geometry("400x300")
    
    import testeCadastroUsuario


    nova_janela.mainloop()


def fazer_login():
    nova_janela = customtkinter.CTk()
    nova_janela.geometry("400x300")

    # Adicione widgets e defina a lógica específica para a nova janela
    import TesteJanelalogin 
    import JanelaPesquisa
    

    nova_janela.mainloop()

def sair():
    print("Opção: Sair")
    janela.destroy()

botao_cadastrar = customtkinter.CTkButton(janela, text="Cadastrar", command=cadastrar)
botao_cadastrar.pack(pady=10)

botao_login = customtkinter.CTkButton(janela, text="Fazer Login", command=fazer_login)
botao_login.pack(pady=10)

botao_sair = customtkinter.CTkButton(janela, text="Sair", command=sair)
botao_sair.pack(pady=10)

janela.mainloop()
input("Pressione <enter> para encerrar!")