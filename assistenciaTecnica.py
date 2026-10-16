import os
import time


chamados = []
proximo_id = 1
SENHA_ADMIN = "admin123"

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausa():
    input("\nPressione Enter para voltar ao menu...")

def menu(perfil):
    print("=" * 52)
    print(f"=== Assistência Técnica - Menu {perfil.capitalize()} ===")
    print("=" * 52)
    if perfil == "cliente":
        print(" 1 - Abrir chamado")
        print(" 2 - Consultar chamado")
        print(" 3 - Fazer Logout (Mudar de Perfil)")
    else:
        print(" 1 - Listar todos os chamados")
        print(" 2 - Alterar status de um chamado")
        print(" 3 - Filtrar chamados por status")
        print(" 4 - Fazer Logout (Mudar de Perfil)")
    print("=" * 52)

def abrir_chamado():
    global proximo_id
    limpar_tela()
    print("=== ABRIR CHAMADO ===\n")
    while True:
        tipo = input("Tipo de equipamento (pc/notebook): ").lower().strip()
        if tipo in ["pc", "notebook"]:
            break
        print("Opção inválida! Digite apenas pc ou notebook.")
        
    numero_pc = input("Número do PC / Patrimônio: ").strip()
    local = input("Local: ").strip()
    descricao = input("Descrição do Problema: ").strip()
    
    chamado = {
        "id": proximo_id,
        "tipo": tipo,
        "numero_pc": numero_pc,
        "local": local,
        "descricao": descricao,
        "status": "Aberto"
    }
    chamados.append(chamado)
    print(f"\nChamado nº {proximo_id} aberto com sucesso!")
    proximo_id += 1
    pausa()

def consultar_chamado():
    limpar_tela()
    print("=== CONSULTAR CHAMADO ===\n")
    if not chamados:
        print("Nenhum chamado registrado no sistema.")
        pausa()
        return
        
    try:
        id_busca = int(input("Digite o número do chamado: "))
    except ValueError:
        print("Número inválido!")
        pausa()
        return
        
    for c in chamados:
        if c["id"] == id_busca:
            print("\n--- Detalhes do Chamado ---")
            print(f"ID: {c['id']}")
            print(f"Equipamento: {c['tipo'].upper()}")
            print(f"Número/Patrimônio: {c['numero_pc']}")
            print(f"Local: {c['local']}")
            print(f"Descrição: {c['descricao']}")
            print(f"Status: {c['status']}")
            pausa()
            return
            
    print(f"Chamado nº {id_busca} não foi encontrado.")
    pausa()

def listar_chamados():
    limpar_tela()
    print("=== LISTAR TODOS OS CHAMADOS ===\n")
    if not chamados:
        print("Nenhum chamado registrado até o momento.")
    else:
        print(f"{'ID':<5} | {'Equipamento':<12} | {'Local':<15} | {'Status':<15}")
        print("-" * 52)
        for c in chamados:
            print(f"{c['id']:<5} | {c['tipo'].upper():<12} | {c['local']:<15} | {c['status']:<15}")
    pausa()

def alterar_status():
    limpar_tela()
    print("=== ALTERAR STATUS DO CHAMADO ===\n")
    if not chamados:
        print("Nenhum chamado registrado no sistema.")
        pausa()
        return
        
    try:
        id_busca = int(input("Digite o número do chamado que deseja alterar: "))
    except ValueError:
        print("Número inválido!")
        pausa()
        return
        
    for c in chamados:
        if c["id"] == id_busca:
            print(f"\nChamado encontrado! Status atual: {c['status']}")
            print("\nEscolha o novo status:")
            print("1 - Aberto")
            print("2 - Em Atendimento")
            print("3 - Concluído")
            opcao_status = input("Opção (1-3): ").strip()
            
            if opcao_status == "1":
                c["status"] = "Aberto"
            elif opcao_status == "2":
                c["status"] = "Em Atendimento"
            elif opcao_status == "3":
                c["status"] = "Concluído"
            else:
                print("Opção inválida! O status não foi alterado.")
                pausa()
                return
                
            print(f"\nStatus do chamado nº {id_busca} updated para {c['status']} com sucesso!")
            pausa()
            return
            
    print(f"Chamado nº {id_busca} não foi encontrado.")
    pausa()

def filtrar_chamados():
    limpar_tela()
    print("=== FILTRAR CHAMADOS POR STATUS ===\n")
    if not chamados:
        print("Nenhum chamado registrado no sistema.")
        pausa()
        return
        
    print("Escolha o status que deseja filtrar:")
    print("1 - Aberto")
    print("2 - Em Atendimento")
    print("3 - Concluído")
    opcao = input("Opção (1-3): ").strip()
    
    if opcao == "1":
        status_busca = "Aberto"
    elif opcao == "2":
        status_busca = "Em Atendimento"
    elif opcao == "3":
        status_busca = "Concluído"
    else:
        print("Opção inválida!")
        pausa()
        return
        
    limpar_tela()
    print(f"=== CHAMADOS COM STATUS: {status_busca.upper()} ===\n")
    encontrados = [c for c in chamados if c["status"] == status_busca]
    
    if not encontrados:
        print(f"Nenhum chamado encontrado com o status {status_busca}.")
    else:
        print(f"{'ID':<5} | {'Equipamento':<12} | {'Local':<15} | {'Status':<15}")
        print("-" * 52)
        for c in encontrados:
            print(f"{c['id']:<5} | {c['tipo'].upper():<12} | {c['local']:<15} | {c['status']:<15}")
    pausa()



while True:  
    limpar_tela()
    print("=" * 52)
    print("=== BEM-VINDO AO SISTEMA DE CHAMADOS ===")
    print("=" * 52)

    while True:
        perfil = input("Escolha o perfil (1 - Cliente / 2 - Administrador / 3 - Fechar Programa): ").strip()
        if perfil == "1":
            perfil_usuario = "cliente"
            break
        elif perfil == "2":
            senha_digitada = input("Digite a senha de administrador: ").strip()
            if senha_digitada == SENHA_ADMIN:
                perfil_usuario = "admin"
                print("\nAcesso concedido!")
                time.sleep(1)
                break
            else:
                limpar_tela()
                print("Senha incorreta! Tente novamente.\n")
        elif perfil == "3":
            limpar_tela()
            print("Encerrando o programa definitivamente... Até logo!")
            time.sleep(1)
            exit()  
        else:
            print("Opção inválida! Digite 1, 2 ou 3.")

    
    logout = False
    while not logout:
        limpar_tela()
        menu(perfil_usuario)
        opcao = input("Escolha uma opção: ").strip()
        
        if perfil_usuario == "cliente":
            if opcao == "1":
                abrir_chamado()
            elif opcao == "2":
                consultar_chamado()
            elif opcao == "3":
                print("\nFazendo logout...")
                time.sleep(1)
                logout = True  
            else:
                print("Opção inválida! Tente novamente.")
                time.sleep(1.5)
                
        elif perfil_usuario == "admin":
            if opcao == "1":
                listar_chamados()
            elif opcao == "2":
                alterar_status()
            elif opcao == "3":
                filtrar_chamados()
            elif opcao == "4":
                print("\nFazendo logout...")
                time.sleep(1)
                logout = True  
            else:
                print("Opção inválida! Tente novamente.")
                time.sleep(1.5)
