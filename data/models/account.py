from datetime import datetime, timedelta

import bcrypt
import jwt
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime

from database import Base
from settings import SECRET_KEY
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from data.models.transaction import Transaction


class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    default_currency_id = Column(Integer, ForeignKey("currencies.id"))
    balance = Column(DECIMAL(10, 2), default=0.00)

    user = relationship("User", back_populates="accounts")
    currency = relationship("Currency", back_populates="accounts")
    transactions_sent = relationship("Transaction", foreign_keys=[Transaction.sender_account_id],
                                     back_populates="sender_account")
    transactions_received = relationship("Transaction", foreign_keys=[Transaction.receiver_account_id],
                                         back_populates="receiver_account")
