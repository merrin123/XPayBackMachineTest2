
from .postgresdatabase import PostgresBase
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class User(PostgresBase):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    password = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)
    profile_id = Column(Integer, ForeignKey('profiles.id'))
    profile = relationship("Profile", back_populates="user")


class Profile(PostgresBase):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    profile_picture = Column(String)
    user = relationship("User", back_populates="profile")