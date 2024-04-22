import unittest
import random

contas_correntes = lambda: {
    'marcos': 240.0,
    'luiza': 354.0,
    'roberto': 987.0
}

# Ajuste da função somar_valor para usar o dicionário contas_correntes diretamente
somar_valor = lambda nome, valor_a_adicionar: (
    lambda contas: (
        lambda _: contas[nome]  # Retorna o novo saldo após a atualização
    )(contas.update({nome: contas.get(nome, 0.0) + valor_a_adicionar}))
)(contas_correntes()) 

diminuir_valor = lambda nome, valor_a_adicionar: (
    lambda contas: (
        lambda _: contas[nome]  # Retorna o novo saldo após a atualização
    )(contas.update({nome: contas.get(nome, 0.0) - valor_a_adicionar}))
)(contas_correntes()) 

# Atualizando processar_pagamento para ser mais adequado para testes
def processar_pagamento(valor, nome_usuario):
    conta_atualizada = somar_valor(nome_usuario, valor)
    return f"R${conta_atualizada:.1f}"

def processar_saque(valor, nome_usuario):
    conta_atualizada = lambda nome_usuario, valor: diminuir_valor(nome_usuario, valor) if contas_correntes().get(nome_usuario) >= valor else "Saldo insuficiente"
    resultado = conta_atualizada(nome_usuario, valor)
    
    imprimir_ou_atualizar = lambda resultado, nome_usuario: resultado if isinstance(resultado, str) else f"R${resultado:.1f}"
    return imprimir_ou_atualizar(resultado, nome_usuario)

    
class TestBankOperations(unittest.TestCase):
    def test_emprestimo_bem_sucedido(self):
        resultado = processar_pagamento(100, 'luiza')
        self.assertEqual("R$454.0", resultado) 
    
    def test_saque_saldo_insuficiente(self):
        # Assume que Luiza tem $354.0, tentar sacar mais do que isso
        resultado = processar_saque(500, 'luiza')
        self.assertEqual("Saldo insuficiente", resultado)
        
    def test_saque_saldo(self):
        # Assume que Luiza tem $354.0, tentar sacar mais do que isso
        resultado = processar_saque(100, 'luiza')
        self.assertEqual("R$254.0", resultado) 
    
    def test_stress_multiple_operations(self):
        # Valores iniciais para referência
        initial_balances = {
            'marcos': 240.0,
            'luiza': 354.0,
            'roberto': 987.0
        }
        
        # Número de operações por usuário
        num_operations = 10000
        
        # Simular operações
        for _ in range(num_operations):
            for user in ['marcos', 'luiza', 'roberto']:
                amount = random.uniform(1, 100)  # valores aleatórios entre $1 e $100
                somar_valor(user, amount)

        # Verificar os saldos finais após todas as operações
        for user in ['marcos', 'luiza', 'roberto']:
            expected_final_balance = initial_balances[user]  # Calcula o saldo esperado
            # Saques e depósitos foram aleatórios, então verificamos se o saldo final é lógico
            final_balance = contas_correntes().get(user)
            # Verifica se o saldo final não é negativo e não excede o saldo inicial + total possível de depósitos
            self.assertTrue(0 <= final_balance <= initial_balances[user] + 100 * num_operations)



if __name__ == '__main__':
    unittest.main()