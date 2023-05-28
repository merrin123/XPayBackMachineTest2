from pydantic import BaseModel

class UserRegistration(BaseModel):
    first_name: str
    password: str
    email: str
    phone: str
    profile_picture: str