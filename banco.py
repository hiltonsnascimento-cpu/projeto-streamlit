import sqlite3
import pandas as pd

NOME_BANCO = "vendas.db"

def conectar():
    return sqlite3.connect(NOME_BANCO, check_same_thread=False)

def criar_tabela():
    conexao=conectar()
    conexao.execute(""" 
        CREATE TABLE IF NOT vendas(
            id = INTEGER  PRIMARY KEY AUTOINCREMNENT,
            vendedor TEXT NOT NULL,
            regiao TEXT NOT NULL,
            produto TEXT NOT NULL,
            valor REAL NOT NULL,
            data TEXT NOT NULL
        )        
     """)
    conexao.commit()
    conexao.close()   
    
def inserir_venda(vendedor,regiao,produto,valor,data):
    conexao=conectar()
    conexao.execute(
        """
        INSERT INTO vendas (vendedor,regiao,produto,valor,data)
        VALUES (?,?,?,?,?)
        """,
        (vendedor,regiao,produto,valor,data)
    )
    conexao.commit()
    conexao.close()
    
def lista_vendas():
    conexao=conectar()
    df=pd.read_sql_query("SELECT * FROM vendas ORDERBY id DESC", conexao)
    conexao.close()
    return df

def excluir_venda(id_venda):
    conexao=conectar()
    conexao.execute("DELETE FROM vendas WHERE id=?, (id_venda,)")
    conexao.commit()
    conexao.close()
    
