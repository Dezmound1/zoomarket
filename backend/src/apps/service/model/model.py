from sqlalchemy.orm import Mapped, mapped_column
import sqlalchemy as sa

from src.settings.db import Base
from src.apps.schema import PriceSchema, MaterialSchema, ColorSchema, BrandSchema, ItemsSchema, CategoriesSchema

class Price(Base):
    __tablename__ = 'prices'

    price_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    price: Mapped[float] = mapped_column(sa.Float())

    def to_read_model(self) -> PriceSchema:
        return PriceSchema(price_id=self.price_id, price=self.price)

class Color(Base):
    __tablename__ = 'colors'

    color_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(sa.String(500))

    def to_read_modal(self) -> ColorSchema:
        return ColorSchema(color_id=self.color_id, title=self.title)
    
class Material(Base):
    __tablename__ = 'materials'

    mat_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    desc: Mapped[str] = mapped_column(sa.String(500))

    def to_read_modal(self) -> MaterialSchema:
        return MaterialSchema(mat_id=self.mat_id, desc=self.desc)

class Brand(Base):
    __tablename__ = 'brands'

    brand_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(sa.String(500))
    phone: Mapped[str] = mapped_column(sa.String(50))
    info: Mapped[str] = mapped_column(sa.String(500))
    location: Mapped[str] = mapped_column(sa.String())

    def to_read_modal(self) -> BrandSchema:
        return BrandSchema(brand_id=self.id, name=self.name, phone=self.phone, info=self.info, location=self.location)
    
class Categories(Base):
    __tablename__ = 'categories'

    cat_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    desc: Mapped[str] = mapped_column(sa.String(500))

    def to_read_model(self) -> CategoriesSchema:
        return CategoriesSchema(cat_id=self.cat_id, desc=self.desc)

class Items(Base):
    __tablename__ = 'items'

    item_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(sa.String(500))
    url_image: Mapped[str] = mapped_column(sa.String(500))
    size: Mapped[float] = mapped_column(sa.Float())
    desc: Mapped[str] = mapped_column(sa.String(500))
    price_price_id: Mapped[int] = mapped_column(sa.ForeignKey('prices.price_id'))
    mat_mat_id: Mapped[int] = mapped_column(sa.ForeignKey('materials.mat_id'))
    brand_brand_id: Mapped[int] = mapped_column(sa.ForeignKey('brands.brand_id'))
    cat_cat_id: Mapped[int] = mapped_column(sa.ForeignKey('categories.cat_id'))
    color_color_id: Mapped[int] = mapped_column(sa.ForeignKey('colors.color_id'))

    def to_read_madel(self) -> ItemsSchema:
        return ItemsSchema(item_id=self.item_id, title=self.title, url_image=self.url_image, size=self.size, desc=self.desc)
