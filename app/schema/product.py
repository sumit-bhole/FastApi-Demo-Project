from pydantic import (
    AnyUrl,
    BaseModel,
    Field,
    field_validator,
    model_validator,
    computed_field,
    EmailStr,
)
from typing import Annotated, List, Literal, Optional
from uuid import UUID
from datetime import datetime


# Create products
class dimension(BaseModel):
    width: Annotated[
        float, Field(gt=0, lt=50, description="Width of the product in cm")
    ]
    height: Annotated[
        float, Field(gt=0, lt=50, description="Height of the product in cm")
    ]
    length: Annotated[
        float, Field(gt=0, lt=50, description="Length of the product in cm")
    ]

    @computed_field
    @property
    def Volume(self) -> float:
        return round(self.width * self.height * self.length, 2)


class seller(BaseModel):
    id: UUID
    name: Annotated[
        str,
        Field(
            description="Name of the seller",
            min_length=2,
            max_length=50,
            title="Seller Name",
            example="John Doe",
        ),
    ]
    email: EmailStr
    website: Annotated[
        Optional[AnyUrl],
        Field(
            default=None,
            description="Website of the seller",
            title="Seller Website",
            example="https://www.example.com",
        ),
    ]


class Product(BaseModel):
    id: UUID
    sku: Annotated[
        str,
        Field(
            description="Stock Keeping Unit",
            min_length=6,
            max_length=30,
            title="SKU of the product",
            example="SKU-123-456",
        ),
    ]
    name: Annotated[
        str,
        Field(
            description="Name of the product",
            min_length=2,
            max_length=30,
            title="Product Name",
            example="Sample Product",
        ),
    ]
    description: Annotated[
        str,
        Field(
            description="Description of the product",
            min_length=10,
            max_length=200,
            title="Product Description",
            example="This is a sample product description.",
        ),
    ]
    price: Annotated[
        float,
        Field(
            description="Price of the product",
            gt=0,
            title="Product Price",
            example=19.99,
        ),
    ]
    currency: Literal["INR"] = "INR"

    discount_percent: Annotated[
        float,
        Field(
            description="Discount percentage for the product",
            ge=0,
            le=100,
            title="Discount Percentage",
            example=10.0,
        ),
    ]
    stock: Annotated[
        int,
        Field(
            description="Available stock for the product",
            ge=0,
            title="Product Stock",
            example=100,
        ),
    ]
    is_active: bool
    rating: Annotated[
        float,
        Field(
            description="Average rating of the product",
            ge=0,
            le=5,
            title="Product Rating",
            example=4.5,
        ),
    ]
    tags: Annotated[
        Optional[list[str]],
        Field(
            default=None,
            max_length=10,
            description="Tags associated with the product(upto 10 tags)",
            title="Product Tags",
            example=["electronics", "gadget"],
        ),
    ]
    image_url: Annotated[
        List[AnyUrl],
        Field(max_length=1, description="Atleast one image url"),
    ]

    dimension: dimension
    seller: seller

    created_at: datetime

    @field_validator("sku", mode="after")
    @classmethod
    def validate_sku_format(cls, value: str):
        if "-" not in value:
            raise ValueError("SKU must contain a hyphen '-'")

        last = value.split("-")[-1]
        if not (last.isdigit() and len(last) == 3):
            raise ValueError("SKU must end with a number after the hyphen '-' like 234")

        return value

    @model_validator(mode="after")
    @classmethod
    def validate_business_rules(cls, model: "Product"):
        if model.stock <= 0 and model.is_active == True:
            raise ValueError(
                "Product cannot be active if stock is zero or less. Please set is_active to False."
            )

        return model

    @computed_field
    @property
    def discounted_price(self) -> float:
        return round(self.price * (1 - self.discount_percent / 100), 2)


# Update Products
class dimension_update(BaseModel):
    width: Annotated[
        Optional[float], Field(gt=0, lt=50, description="Width of the product in cm")
    ]
    height: Annotated[
        Optional[float], Field(gt=0, lt=50, description="Height of the product in cm")
    ]
    length: Annotated[
        Optional[float], Field(gt=0, lt=50, description="Length of the product in cm")
    ]

    @computed_field
    @property
    def Volume(self) -> float:
        return round(self.width * self.height * self.length, 2)


class seller_update(BaseModel):
    name: Annotated[
        Optional[str],
        Field(
            description="Name of the seller",
            min_length=2,
            max_length=50,
            title="Seller Name",
            example="John Doe",
        ),
    ]
    email: Optional[EmailStr]
    website: Annotated[
        Optional[AnyUrl],
        Field(
            default=None,
            description="Website of the seller",
            title="Seller Website",
            example="https://www.example.com",
        ),
    ]


class product_update(BaseModel):
    name: Optional[str] = Field(min_length=6, max_length=80)
    description: Optional[str] = Field(min_length=20, max_length=200)
    price: Optional[float] = Field(gt=0)
    # currency: Optional[Literal["INR"]]
    discount_percent: Optional[float] = Field(ge=0, le=90)
    stock: Optional[int] = Field(gt=0)
    is_active: Optional[bool]
    rating: Optional[float] = Field(gt=0, lt=5)

    tags: Optional[List[str]] = Field(max_length=10)
    image_url: Optional[AnyUrl]

    dimension: Optional[dimension_update]
    seller: Optional[seller_update]

    @model_validator(mode="after")
    @classmethod
    def validate_business_rules(cls, model: "Product"):
        if model.stock <= 0 and model.is_active == True:
            raise ValueError(
                "Product cannot be active if stock is zero or less. Please set is_active to False."
            )

        return model

    @computed_field
    @property
    def discounted_price(self) -> float:
        return round(self.price * (1 - self.discount_percent / 100), 2)
