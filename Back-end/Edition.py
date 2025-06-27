import pandas as pd
import random
import os

CAMINHO_CSV = "Banco/Dados.csv"

# Função para gerar um ID aleatório de 10 dígitos
def gerar_id():
    return str(random.randint(10**9, 10**10 - 1))

def cadastrarCliente(nome, saldo):
    id_novo = gerar_id()
    #Função para verificar se o id que gerou já existe, se existir ele vai criar novamente
    #até criar um que não existe
    while id_novo in df["id"].astype(str).values:
        id_novo = gerar_id()
    
    df = pd.read_csv(CAMINHO_CSV)
    
    novo_cliente = {
        "id": id_novo,
        "nome": nome,
        "saldo": saldo
    }

    df = pd.concat([df, pd.DataFrame([novo_cliente])], ignore_index=True)
    df.to_csv(CAMINHO_CSV, index=False)
    

def excluirCliente(id_cliente):
    # Carrega os dados
    df = pd.read_csv(CAMINHO_CSV)

    # Converte IDs para string para garantir comparação correta
    df["id"] = df["id"].astype(str)
    id_cliente = str(id_cliente)

    # Verifica o saldo do cliente
    saldo_cliente = df.loc[df["id"] == id_cliente, "saldo"].values[0]
    if float(saldo_cliente) != 0:
        print(f"Cliente com ID {id_cliente} não pode ser excluído: saldo é {saldo_cliente}.")
        return

    # Exclui o cliente
    df = df[df["id"] != id_cliente]
    df.to_csv(CAMINHO_CSV, index=False)

def adicionarValorCliente(id,valor):
    df = pd.read_csv(CAMINHO_CSV)
    
    