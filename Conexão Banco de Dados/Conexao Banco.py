import sqlite3 
from sqlite3 import Error

#################### Criar Conexão
def ConexaoBanco():
    caminho="E:\\Python\\banco\\agenda.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon=ConexaoBanco()

################### Create Table

vsql="""CREATE TABLE tb_contatos(
             N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
             T_NOMECONTATO VARCHAR(30),
             T_TELEFONECONTATO VARCHAT(14),
             T_EMAILCONTATO VARCHAR(30)
        );"""
def criarTabela(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("Tabela Criada")
    except Error as ex:
        print(ex)

criarTabela(vcon,vsql)

vsql="""CREATE TABLE tb_contatos_dois(
             N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
             T_NOMECONTATO VARCHAR(30),
             T_TELEFONECONTATO VARCHAT(14),
             T_EMAILCONTATO VARCHAR(30)
        );"""
criarTabela(vcon,vsql)

vcon.close()