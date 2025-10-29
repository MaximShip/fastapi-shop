from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from .category import CategoryResponse

class ProductBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=100,
                      description="The name of the product")
    description: Optional[str] = Field(None, max_length=1000,
                                       description="The description of the product")
    price: float = Field(..., gt=0, description="The price of the product")
    category_id: int = Field(..., description="The ID of the category the product belongs to")
    image_url: Optional[str] = Field(None, description="The URL of the product image")

class ProductCreate(ProductBase):
    pass

class ProductResponse(BaseModel):
    id: int = Field(..., description="The unique identifier of the product")
    name: str
    description: Optional[str]
    price: float
    category_id: int
    category: CategoryResponse = Field(..., description="The category of the product")
    image_url: Optional[str]
    created_at: datetime
    

    class Config:
        from_attributes = True

class ProductListResponse(BaseModel):
    products: list[ProductResponse] = Field(..., description="List of products")
    total: int = Field(..., description="Total number of products")