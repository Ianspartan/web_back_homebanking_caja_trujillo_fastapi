"""HOMEBANKING — Backend FastAPI · Caja Trujillo.

Portal del CLIENTE. Proyecto separado del Core Financiero; se conecta a la base
PostgreSQL existente bd_core_financiero. Corre en el puerto 8002.

Levantar: uvicorn main:app --reload --port 8002
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.cfg_config import settings
from app.routes import route_auth, route_creditos, route_cuentas, route_operaciones

app = FastAPI(
    title="Caja Trujillo — Homebanking API",
    description=(
        "Portal del cliente de Caja Trujillo. Permite consultas y operaciones "
        "del cliente usando las tablas dcliente y usuarios_homebanking."
    ),
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(route_auth.router)
app.include_router(route_cuentas.router)
app.include_router(route_operaciones.router)
app.include_router(route_creditos.router)


@app.get("/", tags=["root"])
def raiz():
    return {
        "servicio": "Caja Trujillo — Homebanking API",
        "version": "1.0.0",
        "estado": "ok",
        "docs": "/docs",
        "puerto": settings.PORT,
    }