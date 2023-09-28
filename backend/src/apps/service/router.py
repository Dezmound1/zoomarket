from fastapi import APIRouter, Depends, Query
from sqlalchemy import select

from typing import List

from src.apps.schema import PriceSchema, MaterialSchema, ColorSchema, BrandSchema, DescStuffSchema, StuffSchema, CategoriesPetSchema
from src.settings.db import get_async_session, AsyncSession
from src.apps.model import *

router: APIRouter = APIRouter()

@router.get("/categores", response_model=List[CategoriesPetSchema], tags=["Фильтрация данных по категориям"], summary="получение категорий")
async def category_pets_get_all(sesion: AsyncSession = Depends(get_async_session)):
    query = [
        {
            "id": 1,
            "name": 'пенис'
        },
        {
            "id": 2,
            "name": '[empty shit]'
        },
        {
            "id": 3,
            "name": 'иди на хуй :)))))'
        },
    ]
    return query

# @router.get("/stuff_by_categores", response_class=List[StuffSchema], tags=["Фильтрация стафа по категориям"], summary="список стафа по категориям")
# async def stuff_by_category(categores_id:int,
#     sesion: AsyncSession = Depends(get_async_session),
#     page: int = Query(1, description="Номер страницы, стандартно 1"),
#     per_page: int = Query(5, description="Количество выгружаемных рецептов, стандартно 5")
# ):
    
#     return 0

@router.get("/all_color", tags=["Фильтрация по цвету"], summary="выгрузка всех цветов")
async def all_color(sesion: AsyncSession = Depends(get_async_session))->List[ColorSchema]:
    query = [
        {
            "id": 1,
            "name": 'голубой'
        },
        {
            "id": 2,
            "name": 'желтый'
        },
        {
            "id": 3,
            "name": 'красный'
        },
    ]
    return query

@router.get("/all_brand", tags=["Фильтрация по бренду"], summary="выгрузка всех брендов")
async def all_brand(sesion: AsyncSession = Depends(get_async_session))->List[BrandSchema]:
    query = [
        {
            "id": 1,
            "name": 'GUSI',
            "phone": "+79677197082",
            "info": "just trust me",
            "location": "somewhere"
        },
        {
            "id": 2,
            "name": 'FERRARI',
            "phone": "+79677197082",
            "info": "do this bro",
            "location": "here"
        },
        {
            "id": 3,
            "name": 'NIKE',
            "phone": "+79677197082",
            "info": "on my way",
            "location": "Bluhera 39"
        },
    ]
    return query

# @router.get("/all_material", response_class=List[MaterialSchema], tags=["Фильтрация по материалу"], summary="выгрузка всех материалов")
# async def all_material(sesion: AsyncSession = Depends(get_async_session)):
#     query = [
#         {
#             "id": 1,
#             "name": 'металл'
#         },
#         {
#             "id": 2,
#             "name": 'кожа'
#         },
#         {
#             "id": 3,
#             "name": 'хром'
#         },
#     ]
#     return query