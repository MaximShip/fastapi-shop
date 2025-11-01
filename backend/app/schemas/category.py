from pydantic import BaseModel, Field

class CategoryBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=100,
                      description="The name of the category")
    
    slug: str = Field(..., min_length=5, max_length=100,
                      description="The URL-friendly slug for the category")

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int = Field(..., description="The unique identifier of the category")

    class Config:
        from_attributes = True