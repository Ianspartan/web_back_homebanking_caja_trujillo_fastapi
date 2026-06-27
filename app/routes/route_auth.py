"""Rutas de autenticación del Homebanking Caja Trujillo."""

from fastapi import APIRouter, Depends
from sqlalchemy.engine import Connection

from app.controllers import ctrl_auth
from app.core.cfg_database import get_db
from app.schemas.sch_auth import LoginRequest, LoginResponse

router = APIRouter(
    prefix="/auth",
    tags=["Autenticación"],
)


@router.post(
    "/login",
    response_model=LoginResponse,
    summary="Iniciar sesión en Homebanking",
)
def login(
    body: LoginRequest,
    conn: Connection = Depends(get_db),
):
    """
    Autentica a un cliente del Homebanking utilizando:

    - Usuario (codcliente)
    - Clave de Internet

    Devuelve un JWT con la información del cliente.
    """
    return ctrl_auth.login(
        conn,
        body.username,
        body.password,
    )