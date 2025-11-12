from db import get_session
import models
from sqlalchemy.exc import NoResultFound


def create_account(account_id: int, owner: str, balance: float = 0.0, *,
                   account_type: str = 'base', password: str = None,
                   bonus_point: int = None, limit: int = None):
    """Create and persist an account. account_type: 'base'|'debit'|'credit'"""
    session = get_session()
    try:
        if account_type == 'debit':
            acc = models.DebitAccountModel(id=account_id, owner=owner, balance=balance,
                                           type='debit', password=password)
        elif account_type == 'credit':
            acc = models.CreditAccountModel(id=account_id, owner=owner, balance=balance,
                                            type='credit', bonus_point=bonus_point or 0,
                                            limit=limit or 0)
        else:
            acc = models.AccountModel(id=account_id, owner=owner, balance=balance, type='base')

        session.add(acc)
        session.commit()
        session.refresh(acc)
        return acc
    finally:
        session.close()


def get_account(account_id: int):
    session = get_session()
    try:
        acc = session.query(models.AccountModel).filter_by(id=account_id).one()
        return acc
    except NoResultFound:
        return None
    finally:
        session.close()


def list_accounts():
    session = get_session()
    try:
        return session.query(models.AccountModel).all()
    finally:
        session.close()


def update_balance(account_id: int, new_balance: float):
    session = get_session()
    try:
        acc = session.query(models.AccountModel).filter_by(id=account_id).one_or_none()
        if not acc:
            return None
        acc.balance = new_balance
        session.add(acc)
        session.commit()
        session.refresh(acc)
        return acc
    finally:
        session.close()


def delete_account(account_id: int):
    session = get_session()
    try:
        acc = session.query(models.AccountModel).filter_by(id=account_id).one_or_none()
        if not acc:
            return False
        session.delete(acc)
        session.commit()
        return True
    finally:
        session.close()
