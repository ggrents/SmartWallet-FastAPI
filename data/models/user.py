from datetime import datetime, timedelta

import bcrypt
import jwt
from sqlalchemy import DateTime

from database import Base
from settings import SECRET_KEY
from sqlalchemy import Boolean, Column, Integer, String, DECIMAL
from sqlalchemy.orm import relationship


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
