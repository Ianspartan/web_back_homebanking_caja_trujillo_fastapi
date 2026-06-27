"""Conexión a PostgreSQL mediante SQLAlchemy.

El Homebanking comparte la base de datos bd_core_financiero con el
Core Financiero. Se trabaja con SQL nativo usando text() y una conexión
por cada petición.
"""

from sqlalchemy import create_engine
from sqlalchemy.engine import Connection

from app.core.cfg_config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,   # Reconecta automáticamente si la conexión se pierde
    future=True,
)


def get_db() -> Connection:
    """
    Entrega una conexión a la base de datos por cada request.

    Los controladores que realizan INSERT, UPDATE o DELETE deben ejecutar:

        conn.commit()

    antes de finalizar la operación.
    """
    conn = engine.connect()

    try:
        yield conn

    finally:
        conn.close()