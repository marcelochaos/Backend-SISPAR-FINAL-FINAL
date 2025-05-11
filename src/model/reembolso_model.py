from src.model import db
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, DECIMAL, String, Date
from sqlalchemy import func 


class Reembolso(db.Model):
   
    id= Column(Integer, primary_key=True,
    autoincrement=True)
    colaborador = Column(String(200), nullable=False)
    empresa = Column(String(50,), nullable=False)
    num_prestacao = Column(Integer, nullable=False)
    descricao = Column(String(255))
    data = db.Column(db.Date, nullable=False, default=func.current_date())
    tipo_reembolso = Column(String(30), nullable=False)
    centro_custo = Column(String(100), nullable=False)
    ordem_interna = Column(String(25))
    divisao = Column(String(25))
    pep = Column(String(25))
    moeda = Column(String(10), nullable=False)
    distancia_km = Column(String(255))
    valor_km = Column(DECIMAL(10,2))
    valor_faturado = Column(DECIMAL(10,2), nullable=False)
    despesa = Column(DECIMAL(10,2))
    id_colaborador = Column(Integer, ForeignKey('colaborador.id'), nullable=False)

    status = Column(String(30), nullable=False)

    
    def __init__ (self, colaborador, empresa, num_prestacao, descricao, data, tipo_reembolso, centro_custo, ordem_interna, divisao, pep, moeda, distancia_km, valor_km, valor_faturado, despesa, id_colaborador, status='Em analise'):
        self.colaborador = colaborador
        self.empresa = empresa
        self.num_prestacao = num_prestacao
        self.descricao = descricao
        self.data = data
        self.tipo_reembolso = tipo_reembolso
        self.centro_custo = centro_custo
        self.ordem_interna = ordem_interna
        self.divisao = divisao
        self.pep = pep
        self.moeda = moeda
        self.distancia_km = distancia_km
        self.valor_km = valor_km
        self.valor_faturado = valor_faturado
        self.despesa = despesa
        self.id_colaborador = id_colaborador
        self.status = status