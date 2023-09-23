from sqlalchemy.orm import Mapped, mapped_column
import sqlalchemy as sa

from src.settings.db import Base
from src.apps.schema import PriceSchema, MaterialSchema, ColorSchema, BrandSchema, DescStuffSchema, StuffSchema, CategoriesPetSchema

class Price(Base):
    __tablename__ = 'price'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    price: Mapped[float] = mapped_column(sa.Float())
    discount: Mapped[float] = mapped_column(sa.Float())
    discounted_price: Mapped[float] = mapped_column(sa.Float())

    def to_read_model(self) -> PriceSchema:
        return PriceSchema(id=self.id, price=self.price, discount=self.discount, discount_price=self.discounted_price)

class Material(Base):
    __tablename__ = 'material'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(sa.String(500))

    def to_read_modal(self) -> MaterialSchema:
        return MaterialSchema(id=self.id, name=self.name)

class Color(Base):
    __tablename__ = 'color'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(sa.String(500))

    def to_read_modal(self) -> ColorSchema:
        return ColorSchema(id=self.id, name=self.name)
    
class Brand(Base):
    __tablename__ = 'brand'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(sa.String(500))
    phone: Mapped[str] = mapped_column(sa.String(50))
    info: Mapped[str] = mapped_column(sa.String(500))
    location: Mapped[str] = mapped_column(sa.String())

    def to_read_modal(self) -> BrandSchema:
        return BrandSchema(id=self.id, name=self.name, phone=self.phone, info=self.info, location=self.location)

class DescStuff(Base):
    __tablename__ = 'desc_stuff'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    price_id: Mapped[int] = mapped_column(sa.ForeignKey('price.id'))
    size: Mapped[float] = mapped_column(sa.Float())
    desc: Mapped[str] = mapped_column(sa.String(500))
    brand_id: Mapped[int] = mapped_column(sa.ForeignKey('brand.id'))
    stuff_id: Mapped[int] = mapped_column(sa.ForeignKey('stuff.id'))
    color_id: Mapped[int] = mapped_column(sa.ForeignKey('color.id'))
    material_id: Mapped[int] = mapped_column(sa.ForeignKey('material.id'))

    def to_read_madel(self) -> DescStuffSchema:
        return DescStuffSchema(id=self.id, size=self.size, desc=self.desc)

class Stuff(Base):
    __tablename__ = 'stuff'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(sa.String(500))
    categories_pet_id: Mapped[int] = mapped_column(sa.ForeignKey('categories_pet.id'))

    def to_read_model(self) -> StuffSchema:
        return StuffSchema(id=self.id, name=self.name)

class CategoriesPet(Base):
    __tablename__ = 'categories_pet'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(sa.String(500))

    def to_read_model(self) -> CategoriesPetSchema:
        return CategoriesPetSchema(id=self.id, name=self.name)

