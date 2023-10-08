"""insert_data_test

Revision ID: e26438775af3
Revises: 79d2959176de
Create Date: 2023-10-07 10:40:02.932874

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e26438775af3'
down_revision: Union[str, None] = '79d2959176de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Добавляем товары для рыб
    op.execute("insert into items (item_id, title, size, desc, url_image, price_price_id, mat_mat_id, brand_brand_id, cat_cat_id, color_color_id) values (2, 'Аквариум', 50.00, 'Прекрасный аквариум для рыбок', 'https://example.com/aquarium.jpg', 1, 1, 1, 1, 1)")
    op.execute("insert into brands (brand_id, name, phone, info, location) values (1, 'FishBrand', '+71234567890', 'лучший бренд для рыб', 'кирова 32, дом 5')")
    op.execute("insert into categories (cat_id, desc) values (1, 'рыбы')")
    op.execute("insert into colors (color_id, title) values (1, 'желтый')")
    op.execute("insert into materials (mat_id, desc) values (1, 'стекло')")
    op.execute("insert into prices (price_id, price) values (1, 2300.00)")

    # Добавляем товары для собак
    op.execute("insert into items (item_id, title, size, desc, url_image, price_price_id, mat_mat_id, brand_brand_id, cat_cat_id, color_color_id) values (3, 'Шлейка', 1.00, 'Удобная шлейка для собаки', 'https://example.com/dog_leash.jpg', 2, 2, 2, 2, 2)")
    op.execute("insert into brands (brand_id, name, phone, info, location) values (2, 'DogBrand', '+79876543210', 'лучший бренд для собак', 'кирова 32, дом 5')")
    op.execute("insert into categories (cat_id, desc) values (2, 'собаки')")
    op.execute("insert into colors (color_id, title) values (2, 'серый')")
    op.execute("insert into materials (mat_id, desc) values (2, 'нейлон')")
    op.execute("insert into prices (price_id, price) values (2, 150.00)")

    # Добавляем товары для птиц
    op.execute("insert into items (item_id, title, size, desc, url_image, price_price_id, mat_mat_id, brand_brand_id, cat_cat_id, color_color_id) values (4, 'Гнездо', 10.00, 'Уютное гнездо для птиц', 'https://example.com/bird_nest.jpg', 3, 3, 3, 3, 3)")
    op.execute("insert into brands (brand_id, name, phone, info, location) values (3, 'BirdBrand', '+74444444444', 'лучший бренд для птиц', 'кирова 32, дом 5')")
    op.execute("insert into categories (cat_id, desc) values (3, 'птицы')")
    op.execute("insert into colors (color_id, title) values (3, 'голубой')")
    op.execute("insert into materials (mat_id, desc) values (3, 'пластик')")
    op.execute("insert into prices (price_id, price) values (3, 2500.00)")

    # Добавляем товары для грызунов
    op.execute("insert into items (item_id, title, size, desc, url_image, price_price_id, mat_mat_id, brand_brand_id, cat_cat_id, color_color_id) values (5, 'Клетка', 20.00, 'Просторная клетка для грызуна', 'https://example.com/cage.jpg', 4, 4, 4, 4, 4)")
    op.execute("insert into brands (brand_id, name, phone, info, location) values (4, 'RodentBrand', '+75555555555', 'лучший бренд для грызунов', 'кирова 32, дом 5')")
    op.execute("insert into categories (cat_id, desc) values (4, 'грызуны')")
    op.execute("insert into colors (color_id, title) values (4, 'коричневый')")
    op.execute("insert into materials (mat_id, desc) values (4, 'металл')")
    op.execute("insert into prices (price_id, price) values (4, 9990.00)")

def downgrade() -> None:
    # Удаляем товары для рыб
    op.execute("delete from items where cat_cat_id = 1")
    op.execute("delete from brands where brand_brand_id = 1")
    op.execute("delete from categories where cat_id = 1")
    op.execute("delete from colors where color_color_id = 1")
    op.execute("delete from materials where mat_mat_id = 1")
    op.execute("delete from prices where price_price_id = 1")

    # Удаляем товары для собак
    op.execute("delete from items where cat_cat_id = 2")
    op.execute("delete from brands where brand_brand_id = 2")
    op.execute("delete from categories where cat_id = 2")
    op.execute("delete from colors where color_color_id = 2")
    op.execute("delete from materials where mat_mat_id = 2")
    op.execute("delete from prices where price_price_id = 2")

    # Удаляем товары для птиц
    op.execute("delete from items where cat_cat_id = 3")
    op.execute("delete from brands where brand_brand_id = 3")
    op.execute("delete from categories where cat_id = 3")
    op.execute("delete from colors where color_color_id = 3")
    op.execute("delete from materials where mat_mat_id = 3")
    op.execute("delete from prices where price_price_id = 3")
 
    # Удаляем товары для грызунов
    op.execute("delete from items where cat_cat_id = 4")
    op.execute("delete from brands where brand_brand_id = 4")
    op.execute("delete from categories where cat_id = 4")
    op.execute("delete from colors where color_color_id = 4")
    op.execute("delete from materials where mat_mat_id = 4")
    op.execute("delete from prices where price_price_id = 4")
