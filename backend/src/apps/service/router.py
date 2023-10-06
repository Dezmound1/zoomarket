from fastapi import APIRouter, Depends, Query
from sqlalchemy import select

from typing import List

from src.apps.schema import PriceSchema, MaterialSchema, ColorSchema, BrandSchema, ItemsSchema, CategoriesSchema
from src.settings.db import get_async_session, AsyncSession
from src.apps.model import *

router: APIRouter = APIRouter()

@router.get("/categores", response_model=List[CategoriesSchema], tags=["Фильтрация данных по категориям"], summary="получение категорий")
async def category_pets_get_all(sesion: AsyncSession = Depends(get_async_session)):
    pass

@router.get("/all_color", tags=["Фильтрация по цвету"], summary="выгрузка всех цветов")
async def all_color(sesion: AsyncSession = Depends(get_async_session))->List[ColorSchema]:
    pass

@router.get("/all_brand", tags=["Фильтрация по бренду"], summary="выгрузка всех брендов")
async def all_brand(sesion: AsyncSession = Depends(get_async_session))->List[BrandSchema]:
    pass

@router.get("/all_material", tags=["Фильтрация по материалу"], summary="выгрузка всех материалов")
async def all_material(sesion: AsyncSession = Depends(get_async_session))->List[MaterialSchema]:
    pass

@router.get("/all_price", tags=["Фильтрация по цене"], summary="выгрузка данных по цене")
async def all_price(sesion: AsyncSession = Depends(get_async_session))->List[PriceSchema]:
    pass
