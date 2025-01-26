from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncEngine

from sqladmin import Admin


def create_admin_view(app: FastAPI, engine: AsyncEngine):
    # admin = Admin(app, engine) # for using with Models
    Admin(app, engine)
