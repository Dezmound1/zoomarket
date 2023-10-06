from pydantic import BaseModel
from typing import List

class PriceSchema(BaseModel):
    price_id: int
    price: float

class ColorSchema(BaseModel):
    color_id: int
    title: str

class MaterialSchema(BaseModel):
    mat_id: int
    desc: str

class BrandSchema(BaseModel):
    brand_id: int
    name: str
    phone: str
    info: str
    location: str

class CategoriesSchema(BaseModel):
    cat_id: int
    desc: str

class ItemsSchema(BaseModel):
    item_id: int
    title: str
    size: float
    desc: str

