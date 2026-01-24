from pydantic import BaseModel
from typing import List, Optional

class Product(BaseModel):
    title: str
    description: str
    images: Optional[List[str]] = []
    price: Optional[float] = None
    cost: Optional[float] = None
    inventory: Optional[int] = None
