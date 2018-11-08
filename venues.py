from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Venue(Base):
    __tablename__ = "venues"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    events = relationship('Event', back_populates = 'venue')

class Artist(Base):
    __tablename__ = "artists"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    events = relationship('Event', secondary='artists_events')

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    venue_id = Column(Integer, ForeignKey('venues.id'))
    venue = relationship('Venue', back_populates = 'events')
    artists = relationship('Artist', secondary='artists_events')

class Artists_Event(Base):
    __tablename__ = 'artists_events'
    artist_id = Column(Integer, ForeignKey('artists.id'), primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'), primary_key=True)

engine = create_engine('sqlite:///events.db')
Base.metadata.create_all(engine)
