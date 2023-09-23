from pydantic import BaseModel
from typing import List

class PriceSchema(BaseModel):
    id: int
    price: float
    discount: float
    discounted_price: float

class MaterialSchema(BaseModel):
    id: int
    name: str

class ColorSchema(BaseModel):
    id: int
    name: str

class BrandSchema(BaseModel):
    id: int
    name: str
    phone: str
    info: str
    location: str

class DesccStuffSchema(BaseModel):
    id: int
    size: float
    desc: str

class StuffSchema(BaseModel):
    id: int
    name: str

class CategoriesPetSchema(BaseModel):
    id: int
    name: str
