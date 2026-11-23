# Locadora de veículos - versão simples para a disciplina de Algoritmos.
# Os dados ficam em listas e são apagados quando o programa termina.


# Cadastra cada veículo com uma placa única e registra sua diária.
def cadastrar_veiculo(veiculos):
    print("\n--- Cadastro de veículo ---")

    # Repete a pergunta até a placa estar no formato correto e não estar cadastrada.
    while True:
        placa = input("Placa (LLLNNNN ou LLLNLNN): ").upper()

        placa_valida = False
        # Antes de verificar as posições, confirma que a placa tem sete caracteres.
        if len(placa) == 7:
            # Formato antigo: três letras seguidas por quatro números.
            if placa[0:3].isalpha() and placa[3:7].isdigit():
                placa_valida = True
            # Formato Mercosul: três letras, um número, uma letra e dois números.
            if (placa[0:3].isalpha() and placa[3].isdigit()
                    and placa[4].isalpha() and placa[5:7].isdigit()):
                placa_valida = True

        # Se nenhum dos formatos foi reconhecido, solicita outra placa.
        if placa_valida == False:
            print("Placa inválida. Use LLLNNNN ou LLLNLNN.")
        else:
            placa_repetida = False
            # Procura a placa informada entre os veículos já cadastrados.
            for veiculo in veiculos:
                if veiculo["placa"] == placa:
                    placa_repetida = True

            # Só aceita a placa se ela ainda não estiver na lista.
            if placa_repetida:
                print("Essa placa já está cadastrada. Digite outra placa.")
            else:
                break

    # Coleta os outros dados e cria o dicionário do veículo.
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    valor_diaria = float(input("Valor do aluguel por dia: R$ ").replace(",", "."))

    veiculo = {
        "codigo": len(veiculos) + 1,
        "placa": placa,
        "marca": marca,
        "modelo": modelo,
        "valor_diaria": valor_diaria,
        "locado": False,
    }
    veiculos.append(veiculo)
    print("Veículo cadastrado com sucesso.")


# Cadastra clientes ou colaboradores com nome e CPF.
def cadastrar_pessoa(lista, tipo):
    print("\n--- Cadastro de", tipo, "---")
    nome = input("Nome: ")

    # Pede outro CPF se tiver formato inválido ou já existir nesta lista.
    while True:
        cpf = input("CPF (somente números, 11 dígitos): ")
        # O CPF deve conter onze caracteres e todos precisam ser números.
        if len(cpf) != 11 or not cpf.isdigit():
            print("O CPF deve ter exatamente 11 números.")
        else:
            cpf_repetido = False
            # Percorre as pessoas já cadastradas procurando o mesmo CPF.
            for pessoa in lista:
                if pessoa["cpf"] == cpf:
                    cpf_repetido = True
            # Impede duplicidade; se for novo, encerra a repetição.
            if cpf_repetido:
                print("Esse CPF já está cadastrado.")
            else:
                break

    # Guarda código, nome e CPF em um dicionário dentro da lista escolhida.
    pessoa = {"codigo": len(lista) + 1, "nome": nome, "cpf": cpf}
    lista.append(pessoa)
    print(tipo, "cadastrado(a) com sucesso.")


# Listas que guardam temporariamente os dados durante a execução.
veiculos = []
clientes = []
colaboradores = []
locacoes = []

# Mantém o menu aberto até o usuário escolher sair.
while True:
    print("\n===== LOCADORA DE VEÍCULOS =====")
    print("1 - Cadastrar veículo")
    print("2 - Cadastrar cliente")
    print("3 - Cadastrar colaborador")
    print("4 - Listar veículos")
    print("5 - Fazer locação")
    print("6 - Registrar devolução")
    print("7 - Relatório")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    # Direciona a execução para a funcionalidade escolhida no menu.
    match opcao:
        case "1":
            # Cadastra um veículo.
            cadastrar_veiculo(veiculos)

        case "2":
            # Cadastra um cliente.
            cadastrar_pessoa(clientes, "cliente")

        case "3":
            # Cadastra um colaborador.
            cadastrar_pessoa(colaboradores, "colaborador")

        case "4":
            # Mostra a situação de cada veículo.
            print("\n--- Veículos disponíveis e locados ---")
            # Informa quando a lista ainda está vazia.
            if len(veiculos) == 0:
                print("Nenhum veículo cadastrado.")
            # Exibe os dados e determina se cada carro está livre ou locado.
            for veiculo in veiculos:
                situacao = "Locado"
                # Altera a situação exibida para carros que não estão alugados.
                if veiculo["locado"] == False:
                    situacao = "Disponível"
                print(
                    veiculo["codigo"], "-", veiculo["marca"], veiculo["modelo"],
                    "| Placa:", veiculo["placa"],
                    "| Diária: R$", format(veiculo["valor_diaria"], ".2f"),
                    "|", situacao
                )

        case "5":
            # Registra a locação, calcula valores e imprime o comprovante.
            # Uma locação precisa de veículo, cliente e colaborador cadastrados.
            if len(veiculos) == 0 or len(clientes) == 0 or len(colaboradores) == 0:
                print("Cadastre veículos, clientes e colaboradores antes da locação.")
            else:
                # Mostra os clientes para que o usuário escolha pelo código.
                print("\nClientes:")
                for cliente in clientes:
                    print(cliente["codigo"], "-", cliente["nome"], "| CPF:", cliente["cpf"])
                codigo_cliente = int(input("Código do cliente: "))

                # Procura na lista o cliente escolhido pelo usuário.
                cliente_escolhido = {}
                for cliente in clientes:
                    if cliente["codigo"] == codigo_cliente:
                        cliente_escolhido = cliente

                # Mostra os colaboradores para a escolha de quem atende a locação.
                print("\nColaboradores:")
                for colaborador in colaboradores:
                    print(colaborador["codigo"], "-", colaborador["nome"], "| CPF:", colaborador["cpf"])
                codigo_colaborador = int(input("Código do colaborador: "))

                # Procura na lista o colaborador escolhido pelo usuário.
                colaborador_escolhido = {}
                for colaborador in colaboradores:
                    if colaborador["codigo"] == codigo_colaborador:
                        colaborador_escolhido = colaborador

                # Não continua se algum dos cadastros escolhidos não existir.
                if len(cliente_escolhido) == 0:
                    print("Cliente não encontrado.")
                elif len(colaborador_escolhido) == 0:
                    print("Colaborador não encontrado.")
                else:
                    # Exibe somente os carros que podem ser alugados.
                    print("\nVeículos disponíveis:")
                    for veiculo in veiculos:
                        if veiculo["locado"] == False:
                            print(
                                veiculo["codigo"], "-", veiculo["marca"], veiculo["modelo"],
                                "| Placa:", veiculo["placa"],
                                "| Diária: R$", format(veiculo["valor_diaria"], ".2f")
                            )

                    codigo_veiculo = int(input("Código do veículo desejado: "))
                    # Procura o veículo correspondente ao código informado.
                    veiculo_escolhido = {}
                    for veiculo in veiculos:
                        if veiculo["codigo"] == codigo_veiculo:
                            veiculo_escolhido = veiculo

                    # Confere se o carro existe e se está livre antes de alugar.
                    if len(veiculo_escolhido) == 0:
                        print("Veículo não encontrado.")
                    elif veiculo_escolhido["locado"]:
                        print("Esse veículo já está locado.")
                    else:
                        dias = int(input("Quantidade de dias de locação: "))

                        # Impede locações com zero ou quantidade negativa de dias.
                        if dias < 1:
                            print("A quantidade de dias deve ser maior que zero.")
                        else:
                            # Calcula o aluguel e o seguro de 25% sobre o aluguel.
                            aluguel = veiculo_escolhido["valor_diaria"] * dias
                            seguro = aluguel * 0.25
                            desconto = 0

                            # Aplica somente a maior faixa de desconto correspondente.
                            if dias > 30:
                                desconto = aluguel * 0.20
                            elif dias > 15:
                                desconto = aluguel * 0.10
                            elif dias > 5:
                                desconto = aluguel * 0.05

                            # Desconta o aluguel e soma o seguro para obter o total.
                            total_final = aluguel - desconto + seguro
                            # Marca o veículo como ocupado até a devolução.
                            veiculo_escolhido["locado"] = True

                            # Registra os dados e valores da locação no histórico da execução.
                            locacao = {
                                "codigo": len(locacoes) + 1,
                                "cliente": cliente_escolhido["nome"],
                                "cliente_cpf": cliente_escolhido["cpf"],
                                "colaborador": colaborador_escolhido["nome"],
                                "colaborador_cpf": colaborador_escolhido["cpf"],
                                "veiculo_codigo": veiculo_escolhido["codigo"],
                                "dias": dias,
                                "aluguel": aluguel,
                                "seguro": seguro,
                                "desconto": desconto,
                                "total_final": total_final,
                            }
                            locacoes.append(locacao)

                            # Apresenta ao usuário os dados e o resumo financeiro da locação.
                            print("\n===== COMPROVANTE DE LOCAÇÃO =====")
                            print("Cliente:", locacao["cliente"])
                            print("CPF do cliente:", locacao["cliente_cpf"])
                            print("Colaborador:", locacao["colaborador"])
                            print("CPF do colaborador:", locacao["colaborador_cpf"])
                            print(
                                "Veículo:", veiculo_escolhido["marca"], veiculo_escolhido["modelo"],
                                "| Placa:", veiculo_escolhido["placa"]
                            )
                            print("Diária: R$", format(veiculo_escolhido["valor_diaria"], ".2f"))
                            print("Dias:", dias)
                            print("Valor total do aluguel: R$", format(aluguel, ".2f"))
                            print("Seguro (25%): R$", format(seguro, ".2f"))
                            print("Desconto: R$", format(desconto, ".2f"))
                            print("Valor final da locação: R$", format(total_final, ".2f"))

        case "6":
            # Libera um veículo que estava locado.
            locacoes_abertas = 0
            print("\n--- Veículos locados ---")
            # Lista os veículos que precisam ser devolvidos.
            for veiculo in veiculos:
                if veiculo["locado"]:
                    locacoes_abertas = locacoes_abertas + 1
                    print(veiculo["codigo"], "-", veiculo["modelo"], veiculo["placa"])

            # Só pede um código se existir algum carro locado.
            if locacoes_abertas == 0:
                print("Não há veículos locados.")
            else:
                codigo_veiculo = int(input("Código do veículo devolvido: "))
                veiculo_encontrado = False
                # Localiza o carro informado e muda seu estado para disponível.
                for veiculo in veiculos:
                    if veiculo["codigo"] == codigo_veiculo and veiculo["locado"]:
                        veiculo["locado"] = False
                        veiculo_encontrado = True

                # Mostra se a devolução foi registrada ou se o código não corresponde.
                if veiculo_encontrado:
                    print("Devolução registrada.")
                else:
                    print("Veículo locado não encontrado.")

        case "7":
            # Exibe veículos, clientes e os totais das locações.
            print("\n===== RELATÓRIO =====")
            print("Veículos disponíveis e locados:")
            # Informa se não há carros e exibe a situação de cada veículo cadastrado.
            if len(veiculos) == 0:
                print("Nenhum veículo cadastrado.")
            for veiculo in veiculos:
                situacao = "Locado"
                if veiculo["locado"] == False:
                    situacao = "Disponível"
                print(
                    veiculo["marca"], veiculo["modelo"],
                    "| Placa:", veiculo["placa"], "|", situacao
                )

            print("\nClientes cadastrados:")
            # Lista os clientes e seus CPFs.
            for cliente in clientes:
                print(cliente["codigo"], "-", cliente["nome"], "| CPF:", cliente["cpf"])

            # Soma os valores de todas as locações feitas nesta execução.
            total_alugueis = 0
            total_seguros = 0
            total_descontos = 0
            total_final = 0
            for locacao in locacoes:
                total_alugueis = total_alugueis + locacao["aluguel"]
                total_seguros = total_seguros + locacao["seguro"]
                total_descontos = total_descontos + locacao["desconto"]
                total_final = total_final + locacao["total_final"]

            print("\nValor total dos aluguéis: R$", format(total_alugueis, ".2f"))
            print("Valor total dos seguros: R$", format(total_seguros, ".2f"))
            print("Valor total dos descontos: R$", format(total_descontos, ".2f"))
            print("Valor final das locações: R$", format(total_final, ".2f"))

        case "0":
            # Encerra o programa; os dados estão somente na memória.
            print("Encerrando. Os dados serão apagados ao sair.")
            break

        case _:
            # Trata qualquer opção que não esteja prevista no menu.
            print("Opção inválida.")



