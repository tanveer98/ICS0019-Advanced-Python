from sqlalchemy import Column, ForeignKey, Integer, String, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Provider(Base):
    __tablename__ = 'providers'
    id = Column(Integer,primary_key=True)
    provider_name = Column(String)
    childern = relationship("Canteen")

    def __str__(self):
        return f"Name: {self.provider_name} id: {self.id}"
    
    def __repr__(self):
        return f"<Provider> Name: {self.provider_name} id: {self.id}"

class Canteen(Base):
    __tablename__ = 'canteens'
    id = Column(Integer,primary_key=True)
    provider_id = Column(Integer, ForeignKey('providers.id'))
    name = Column(String, nullable=False)
    location = Column(String)
    time_open = Column(Time)
    time_closed = Column(Time)
    provider = relationship("Provider", backref="provider") #holds a reference to the foreign key object its related to!

    def __init__(self, provider, name, loc, t_open,t_close):
        self.provider_id = provider
        self.name = name
        self.location = loc
        self.time_open = t_open
        self.time_closed = t_close
        return

    def __repr__(self):
        return f"<Canteen> Name: {self.name} id: {self.id}"

    def __str__(self):
        str_ = f'\nCanteen: {self.name} \nLocation:{self.location} \nTime Open: {self.time_open} \nTime Close: {self.time_closed}\n\n'

        return str_

    