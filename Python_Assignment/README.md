SQLAlchemy integration for existing account classes

This small example shows how to map your existing account classes into SQLAlchemy models and perform basic CRUD operations using SQLite.

Setup
1. Activate your virtual environment (Windows PowerShell):

   .\myenv\Scripts\Activate.ps1

2. Install SQLAlchemy in the environment:

   pip install SQLAlchemy

How to run
1. Change directory to the `Python_Assignment` folder:

   Set-Location -Path "c:\Users\riteshmishra.a\Desktop\Python_Start\Python_Assignment"

2. Run the CRUD example:

   python .\crud_example.py

Files added
- `db.py` — SQLAlchemy engine, Base, Session factory, and init function.
- `models.py` — SQLAlchemy models (single-table inheritance): AccountModel, DebitAccountModel, CreditAccountModel.
- `repository.py` — Simple CRUD helper functions wrapping sessions.
- `crud_example.py` — Example script showing create/read/update/delete flow.

Notes and next steps
- These models use single-table inheritance; optional subclass fields (password, bonus_point, limit) are stored in the same table.
- For production, consider using Alembic for migrations and stronger password handling (hashing).
- If you want the SQLAlchemy models to interoperate with existing plain-Python classes (`Account`, `DebitAccount`, `CreditAccount`), I can add conversion helpers (to/from model instances).
