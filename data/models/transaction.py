from datetime import datetime, timedelta
from database import Base

from sqlalchemy import DateTime
from sqlalchemy import Column, ForeignKey, Integer, DECIMAL
from sqlalchemy.orm import relationship


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
