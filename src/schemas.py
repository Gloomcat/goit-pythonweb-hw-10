from typing import Optional, Annotated, Union

from datetime import date

from pydantic import BaseModel, Field, EmailStr, PastDate
from pydantic_extra_types.phone_numbers import PhoneNumber, PhoneNumberValidator

ContactNumberType = Annotated[Union[str, PhoneNumber], PhoneNumberValidator()]


class ContactModel(BaseModel):
    first_name: Optional[str] = Field(None, min_length=2, max_length=25)
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[ContactNumberType] = None
    date_of_birth: Optional[PastDate] = Field(None, ge=date(1900, 1, 1))


class ContactCreateModel(ContactModel):
    first_name: str
    phone: ContactNumberType


class ContactResponseModel(ContactModel):
    id: int
