from sqlalchemy import Column, Integer, String, Text, Enum, Date, Float
from app.repositorys.configDb import Base


class divida(Base):
    id_divida = Column(Integer,primary_key=True,index=True)
    termo_divida = Column(Text,nullable=False)
    data = Column(Date,nullable=False,index=True)
    montante_total = Column(Float,nullable=False)
    montante_atrasado = Column(Float,nullable=False)
    devedor = Column(Integer,ForeignKey("devedor.id_user"),nullable=False,index=True)
    credor = Column(Integer,ForeignKey("credor.id_user"),nullable=False,index=True)
    status = Column(Enum("Paga","Atrasada","Renegociada"),nullable=False)
