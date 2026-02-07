from datetime import datetime, timezone
from enum import Enum
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from api.core.database import Base


class AudienciaTipo(String, Enum):
    CONCILIACAO = "conciliacao"
    INSTRUCAO = "instrução"
    JULGAMENTO = "julgamento"


class Audiencia(Base):
    __tablename__ = "audiencias"

    id = Column(Integer, primary_key=True, index=True)
    data_criacao = Column(DateTime, default=datetime.now(timezone.utc))
    tipo = Column(AudienciaTipo)
    local = Column(String, nullable=False)

    # Chave estrangeira para processo
    id_processo = Column(Integer, ForeignKey("processo.id"), nullable=False, unique=False)  # ignore E501

    #  Relacionamento com processo
    processo = relationship("Processo", back_populates="audiencias")
    # lista armazenada
