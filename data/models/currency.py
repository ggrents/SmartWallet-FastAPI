from sqlalchemy import Column, Integer, String, DECIMAL
from sqlalchemy.orm import relationship

from database import Base


class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True, index=True)
    currency_code = Column(String(3), unique=True, index=True)
    currency_symbol = Column(String(5))
    exchange_rate = Column(DECIMAL(10, 4), default=1.0000)

    accounts = relationship("Account", back_populates="currency")