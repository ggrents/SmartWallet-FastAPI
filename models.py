from datetime import datetime, timedelta

import bcrypt
import jwt
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.dialects import registry
from sqlalchemy.orm import relationship

from database import Base, SECRET_KEY

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    balance = Column("balance", DECIMAL(10, 2), default=0.00)
    is_active = Column(Boolean, default=True)
    registration_date = Column(DateTime, default=datetime.utcnow)

    accounts = relationship("Account", back_populates="user")

    def hash_password(self, password: str):
        self.hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def verify_password(self, password: str):
        return bcrypt.checkpw(password.encode('utf-8'), self.hashed_password)

    def generate_token(self):
        expiration = datetime.utcnow() + timedelta(hours=24)
        payload = {
            "sub": str(self.id),
            "exp": expiration.timestamp()
        }

        return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    sender_account_id = Column(Integer, ForeignKey("accounts.id"))
    receiver_account_id = Column(Integer, ForeignKey("accounts.id"))
    transaction_date = Column(DateTime, default=datetime.utcnow)
    amount = Column(DECIMAL(10, 2))

    sender_account = relationship("Account", foreign_keys=[sender_account_id], back_populates="transactions_sent")
    receiver_account = relationship("Account", foreign_keys=[receiver_account_id],
                                    back_populates="transactions_received")


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


class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True, index=True)
    currency_code = Column(String(3), unique=True, index=True)
    currency_symbol = Column(String(5))
    exchange_rate = Column(DECIMAL(10, 4), default=1.0000)

    accounts = relationship("Account", back_populates="currency")
