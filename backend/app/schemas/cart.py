from pydantic import BaseModel, Field
from typing import Optional

class CartItemBase(BaseModel):
    product_id: int = Field(..., description="The ID of the product")
    quantity: int = Field(..., gt=0, description="The quantity of the product in the cart")

class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(BaseModel):
    product_id: int = Field(..., description="The ID of the product")
    quantity: int = Field(..., gt=0, description="The updated quantity of the product in the cart")

class CartItem(BaseModel):
    product_id: int
    name: str = Field(..., description="The name of the product")
    price: float = Field(..., description="The price of the product")
    quantity: int = Field(..., description="The quantity of the product in the cart")
    subtotal: float = Field(..., description="The subtotal price for this cart item")
    image_url: Optional[str] = Field(None, description="The URL of the product image")

class CartResponse(BaseModel):
    items: list[CartItem] = Field(..., description="List of items in the cart")
    total_quantity: int = Field(..., description="Total quantity of items in the cart")
    total_price: float = Field(..., description="Total price of all items in the cart")