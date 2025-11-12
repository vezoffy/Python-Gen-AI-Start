from sqlalchemy import Column, Integer, String, Float
from db import Base


class AccountModel(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)  # maps to accountNum
    owner = Column(String, nullable=False)
    balance = Column(Float, default=0.0)
    type = Column(String, nullable=False)

    # Optional fields used by subclasses
    password = Column(String, nullable=True)
    bonus_point = Column(Integer, nullable=True)
    limit = Column(Integer, nullable=True)

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'base'
    }


class DebitAccountModel(AccountModel):
    __mapper_args__ = {'polymorphic_identity': 'debit'}


class CreditAccountModel(AccountModel):
    __mapper_args__ = {'polymorphic_identity': 'credit'}
