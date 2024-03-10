from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import text

Base = declarative_base()

class ProductCategory(Base):
    __tablename__ = 'product_category'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    desc = Column(Text)
    created_at = Column(DateTime)
    modified_at = Column(DateTime)
    deleted_at = Column(DateTime)

class Product(Base):
    __tablename__ = 'product'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    desc = Column(Text)
    SKU = Column(String)
    
    category_id = Column(Integer, ForeignKey('product_category.id'))
    category = relationship("ProductCategory")
    
    inventory_id = Column(Integer, ForeignKey('product_inventory.id'))
    inventory = relationship("ProductInventory")
    
    price = Column(Float)
    discount_id = Column(Integer, ForeignKey('discount.id'))
    discount = relationship("Discount")
    
    created_at = Column(DateTime)
    modified_at = Column(DateTime)
    deleted_at = Column(DateTime)


class ProductInventory(Base):
    __tablename__ = 'product_inventory'

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    created_at = Column(DateTime)
    modified_at = Column(DateTime)
    deleted_at = Column(DateTime)


class Discount(Base):
    __tablename__ = 'discount'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    desc = Column(Text)
    discount_percent = Column(Float)
    active = Column(Boolean)
    created_at = Column(DateTime)
    modified_at = Column(DateTime)
    deleted_at = Column(DateTime)
