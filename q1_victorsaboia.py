createTransaction = lambda x: print(x)
createTransaction("**Create Transaction**");


###PARA LOGAR DEVE-SE UTILIZAR O NOME DO USUARIO, COMO MARCOS E DEPOIS DIGITAR SUA SENHA
###EX: USER:MARCOS SENHA: ATLANTICO1




##DICIONARIO DE USUARIO COM SALDO RESPECTIVO
contas_correntes = lambda: {
    'marcos': 240.0,
    'luiza': 354.0,
    'roberto': 987.0
}

##DICIONARIO DE USUARIO COM SENHA RESPECTIVA
senhas = lambda: {
    'marcos': 'atlantico1',
    'luiza': 'victor34',
    'roberto': 'rob345'
}

nome_usuario = input("Digite seu nome de usuário: ")
senha_usuario = input("Digite sua senha: ")

def aprovacao_banco():
    print("Solicitando aprovacao do banco.")

def cancela_transação_saldo_insuficiente():
    print("Saldo insuficiente. Transação cancelada.")
    
def fechar_transacao():
    print("Transação concluída com sucesso.")
    
################################CALCULO DE CREDITO(EMPRESTIMO)#################################################

somar_valor = lambda nome, valor_a_adicionar: (
    lambda contas: (
        lambda _: contas[nome]  # Retorna o novo saldo após a atualização
    )(contas.update({nome: contas.get(nome, 0.0) + valor_a_adicionar}))
)(contas_correntes()) 

def processar_pagamento(numero_cartao, valor, nome_usuario):
    print(f"Processando emprestimo para o cartão {numero_cartao} no valor de R${valor:.2f}")
    aprovacao_banco()
    conta_atualizada = somar_valor(nome_usuario, valor)
    print(f"Novo saldo de {nome_usuario.capitalize()}: R${conta_atualizada:.2f}")
    fechar_transacao()
    
def capturar_dados_pagamento(nome_usuario):
    numero_cartao = input("Digite o número do cartão de crédito: ")
    valor = float(input("Digite o valor que deseja de emprestimo: "))
    return numero_cartao, valor, nome_usuario


credit = lambda nome_usuario: processar_pagamento(*capturar_dados_pagamento(nome_usuario))



################################CALCULO DE SAQUE#################################################
processar_saque = lambda nome, valor_a_sacar: (
    contas_correntes[nome] - valor_a_sacar if contas_correntes.get(nome, 0) >= valor_a_sacar else "Saldo insuficiente"
)

diminuir_valor = lambda nome, valor_a_adicionar: (
    lambda contas: (
        lambda _: contas[nome]  # Retorna o novo saldo após a atualização
    )(contas.update({nome: contas.get(nome, 0.0) - valor_a_adicionar}))
)(contas_correntes()) 


def processar_saque(valor, nome_usuario):
    print(f"Processando saque para o {nome_usuario.capitalize()} no valor de R${valor:.2f}")

    conta_atualizada = lambda nome_usuario, valor: diminuir_valor(nome_usuario, valor) if contas_correntes().get(nome_usuario) >= valor else "Saldo insuficiente"
    resultado = conta_atualizada(nome_usuario, valor)
    
    imprimir_ou_atualizar = lambda resultado, nome_usuario: print(resultado) if isinstance(resultado, str) else print(f"Novo saldo de {nome_usuario.capitalize()}: R${resultado:.2f}")
    imprimir_ou_atualizar(resultado, nome_usuario)
    
def capturar_dados_saque(nome_usuario):
    valor = float(input("Digite o valor que sacar: "))
    return valor, nome_usuario


cash = lambda nome_usuario: processar_saque(*capturar_dados_saque(nome_usuario))


#############################CALCULO DE TRANSFERENCIA###################################################

def processar_transferencia(valor, nome_usuario, conta_corrente):
    print(f"Processando transferencia do {nome_usuario.capitalize()} para o {conta_corrente.capitalize()} no valor de R${valor:.2f}")

    conta_atualizada = lambda nome_usuario, valor: diminuir_valor(nome_usuario, valor) if contas_correntes().get(nome_usuario) >= valor else "Saldo insuficiente"
    resultado = conta_atualizada(nome_usuario, valor)
    
    imprimir_ou_atualizar = lambda resultado, nome_usuario: print(resultado) if isinstance(resultado, str) else print(f"Novo saldo de {nome_usuario.capitalize()}: R${resultado:.2f}")
    imprimir_ou_atualizar(resultado, nome_usuario)
    
    conta_atualizada = somar_valor(conta_corrente, valor)
    print(f"Novo saldo de {conta_corrente.capitalize()}: R${conta_atualizada:.2f}")






def capturar_dados_transferencia(nome_usuario):
    valor = float(input("Digite o valor que deseja transferir: "))
    conta_corrente = input("Digite o nome da conta corrente que deseja transferir: ")
    return valor, nome_usuario, conta_corrente


foundTransfer = lambda nome_usuario: processar_transferencia(*capturar_dados_transferencia(nome_usuario))



#################################################################################
menu_opcoes = {
    1: lambda valor: credit(nome_usuario),
    2: lambda valor: cash(valor),
    3: lambda valor: foundTransfer(valor)
}

escolha_menu = int(input("Selecione uma opção:\n1 - Credit\n2 - Cash\n3 - Found Transfer\nDigite o número da opção desejada: "))

inicia_operacao = lambda escolha, nome: (
    lambda operacao: operacao(nome) if escolha in menu_opcoes else print("Opção inválida.")
)(menu_opcoes.get(escolha))

autenticar_usuario = lambda nome, senha: (
    lambda senha_correta: inicia_operacao(escolha_menu, nome) if senha == senha_correta else (
        lambda resultado: print(resultado)
    )("Credenciais inválidas")
)(senhas().get(nome))

autenticar_usuario(nome_usuario, senha_usuario)


















#print("Escolha uma opção:")
#print("1 - Credito")
#print("2 - Debito")
#print("3 - Transferência de fundos")

#entrada = input("Digite o número da opção desejada: ")
#opcao = int(entrada)

#selecionar_opcao = lambda escolha: credit_process() if escolha == 1 else cash_process()
#selecionar_opcao(opcao)

