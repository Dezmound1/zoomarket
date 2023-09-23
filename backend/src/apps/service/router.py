from fastapi import APIRouter, Depends
from sqlalchemy import select

from typing import List

from src.apps.schema import PriceSchema, MaterialSchema, ColorSchema, BrandSchema, DesccStuffSchema, StuffSchema, CategoriesPetSchema
from src.settings.db import get_async_session, AsyncSession
from src.apps.model import *

router: APIRouter = APIRouter()
