from sqlalchemy import Table, Column, Integer, String, Float
from sqlalchemy.orm import registry
from db import Base, get_session, engine

# Import your original classes (plain Python)
from Account import Account
from DebitAccount import DebitAccount
from CreditAccount import CreditAccount

# Create a registry that will use the same metadata as Base
mapper_registry = registry(metadata=Base.metadata)

# Single table that stores all account types (nullable columns for subclass fields)
accounts_table = Table(
    'accounts',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('owner', String, nullable=False),
    Column('balance', Float, default=0.0),
    Column('type', String, nullable=False),
    Column('password', String, nullable=True),
    Column('bonus_point', Integer, nullable=True),
    Column('limit', Integer, nullable=True),
)

# Map the attributes of your existing classes to the table columns.
# Note: your classes use attribute names `accountNum`, `accountOwner`, `balance`,
# `password`, `bonusPoint`, `limit` so we map columns to those attribute names.

mapper_registry.map_imperatively(
    Account,
    accounts_table,
    properties={
        'accountNum': accounts_table.c.id,
        'accountOwner': accounts_table.c.owner,
        'balance': accounts_table.c.balance,
        'type': accounts_table.c.type,
    },
    polymorphic_on=accounts_table.c.type,
    polymorphic_identity='base',
)

mapper_registry.map_imperatively(
    DebitAccount,
    None,
    inherits=Account,
    properties={
        # DebitAccount already uses attribute name `password` which maps
        # automatically to the `password` column on the table.
    },
    polymorphic_identity='debit',
)

mapper_registry.map_imperatively(
    CreditAccount,
    None,
    inherits=Account,
    properties={
        'bonusPoint': accounts_table.c.bonus_point,
        'limit': accounts_table.c.limit,
    },
    polymorphic_identity='credit',
)


def init_mappings():
    """Ensure tables exist. Call this before using the ORM mappings."""
    Base.metadata.create_all(bind=engine)


def save(instance):
    """Add or update a mapped instance (your original class instance) and commit.

    Example:
        a = DebitAccount(10, 'Alice', 100.0, 's3cr3t')
        orm_mapping.save(a)
    """
    session = get_session()
    try:
        session.add(instance)
        session.commit()
        session.refresh(instance)
        return instance
    finally:
        session.close()


def get_by_id(account_id):
    session = get_session()
    try:
        return session.query(Account).filter_by(accountNum=account_id).one_or_none()
    finally:
        session.close()


def list_all():
    session = get_session()
    try:
        return session.query(Account).all()
    finally:
        session.close()


def delete(instance):
    session = get_session()
    try:
        session.delete(instance)
        session.commit()
        return True
    finally:
        session.close()
