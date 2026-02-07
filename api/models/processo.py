from datetime import datetime, timezone
from enum import Enum
from sqlalchemy import Column, Integer, String, DateTime
from api.core.database import Base


class ProcessoTipo(String, Enum):
    ATIVO = "ativo"
    ARQUIVADO = "arquivado"
    SUSPENSO = "suspenso"


class Processo(Base):
    __tablename__ = "processos"

    id = Column(Integer, primary_key=True, index=True)
    numero_processo = Column(String, unique=True, nullable=False)
    data_criacao = Column(DateTime, default=datetime.now(timezone.utc))
    vara = Column(String, nullable=False)
    comarca = Column(String, nullable=False)
    assunto = Column(String, nullable=False)
    status = Column(ProcessoTipo)    
