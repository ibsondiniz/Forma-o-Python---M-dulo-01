def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
    contato = {
        "contato": nome_contato,
        "telefone": telefone_contato,
        "email": email_contato,       
        "favorito": False}
    contatos.append(contato)
    print(f"Contato {nome_contato} foi adicionado com sucesso!")

def ver_contatos(contatos):
    print("\nLista de contatos: ")
    for indice, contato in enumerate(contatos, start=1):
        status = "★" if contato["favorito"] else " "
        nome_contato = contato["contato"]
        telefone_contato = contato["telefone"] if contato["telefone"] else " "
        email_contato = contato["email"] if contato["email"] else " "
        print(f"{indice}. [{status}] {nome_contato} - Telefone: {telefone_contato}, Email: {email_contato}")

def editar_dados_contato(contatos, indice_contato, novo_nome_contato=None, novo_telefone=None, novo_email=None):
    try:
        indice_contato_ajustado = int(indice_contato) - 1
        if 0 <= indice_contato_ajustado < len(contatos):
            if novo_nome_contato is not None:
                contatos[indice_contato_ajustado]["contato"] = novo_nome_contato
            if novo_telefone is not None:
                contatos[indice_contato_ajustado]["telefone"] = novo_telefone
            if novo_email is not None:
                contatos[indice_contato_ajustado]["email"] = novo_email
            print(f"Contato {indice_contato} atualizado com sucesso")
        else:
            print("Índice de contato inválido")
    except ValueError:
        print("Índice inválido. Certifique-se de que está digitando um número.")

def alternar_status(contatos, indice_contato):
    try:
        indice_contato_ajustado = int(indice_contato) - 1
        if 0 <= indice_contato_ajustado < len(contatos):
            contato = contatos[indice_contato_ajustado]
            contato["favorito"] = not contato["favorito"]
            status = "marcado como favorito" if contato["favorito"] else "desmarcado como favorito"
            print(f"Contato {indice_contato} foi {status}")
        else:
            print("Índice de contato inválido")
    except ValueError:
        print("Índice inválido. Certifique-se de que está digitando um número.")

def deletar_contato(contatos, indice_contato):
    try:
        indice_contato_ajustado = int(indice_contato) - 1
        if 0 <= indice_contato_ajustado < len(contatos):
            contatos.pop(indice_contato_ajustado)
            print(f"Contato {indice_contato} deletado com sucesso.")
        else:
            print("Índice de contato inválido")
    except ValueError:
        print("Índice inválido. Certifique-se de que está digitando um número.")
 
contatos = []
while True:
    print("\nMenu da agenda:")
    print("1. Adicionar contatos")
    print("2. Ver contatos")
    print("3. Editar dados dos contatos")
    print("4. Alterar Status")
    print("5. Deletar contatos")
    print("6 Sair")

    escolha = input("Digite a sua escolha: ")
    
    if escolha == "1":
        nome_contato = input("Digite o nome do contato que deseja adicionar: ")
        telefone_contato = input("Digite o telefone do contato (opcional): ")
        email_contato = input("Digite o email do contato (opcional): ")
        adicionar_contato(contatos, nome_contato, telefone_contato, email_contato)
    
    elif escolha == "2":
        ver_contatos(contatos)
    
    elif escolha == "3":
        ver_contatos(contatos)
        indice_contatos = input("Digite o número do contato que deseja atualizar: ")
        novo_nome = input("Digite o novo nome do contato(deixe em branco para não alterar): ")
        novo_telefone = input("Digite o novo telefone do contato(deixe em branco para não alterar): ")
        novo_email = input("Digite o novo email do contato(deixe em branco para não alterar): ")
        editar_dados_contato(contatos, indice_contatos, novo_nome if novo_nome else None, novo_telefone if novo_telefone else None, novo_email if novo_email else None)
    
    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja mudar o status: ")
        alternar_status(contatos, indice_contato)
        
    elif escolha == "5":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja deletar: ")
        deletar_contato(contatos, indice_contato)
        
    elif escolha == "6":
        break
    
print("Programa finalizado")