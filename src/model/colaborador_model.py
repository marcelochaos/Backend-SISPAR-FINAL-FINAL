from src.model import db 
from sqlalchemy.schema import Column 
from sqlalchemy.types import String, DECIMAL, Integer 

class Colaborador(db.Model): 
    id = Column(Integer, primary_key=True, autoincrement=True) 
    nome = Column(String(255)) 
    email = Column(String(150))
    senha = Column(String(255))
    cargo = Column(String(100))
    salario = Column(DECIMAL(10,2))

    

    def __init__ (self, nome, email, senha, cargo, salario):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo
        self.salario = salario       

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'email': self.email,
            'senha': self.senha,
        }
        
    def all_data(self) -> dict:
        return {
            'id': self.id,
            'nome': self.nome,
            'cargo': self.cargo,
            'salario': self.salario
        }