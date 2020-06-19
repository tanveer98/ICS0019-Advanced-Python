from .models import Provider, Canteen, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import time

# creates a connection to the database, returns a 'session' object which is used to perform queries in the db.
def create_db(file_path):
    engine = create_engine('sqlite:///' + file_path)
    # tables don't exist, create them..
    if engine.dialect.has_table(
            engine.connect(),
            Provider.__tablename__) == False or engine.dialect.has_table(
                engine.connect(), Canteen.__tablename__) == False:
        Base.metadata.create_all(engine)
    
    session = None

    if engine != None:
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session() 
    
    return session

# to insert providers
def insert_providers(session):
    providers = [
        Provider(id=1,provider_name="Rahva Toit"),
        Provider(id=2,provider_name="Baltic Restaurants Estonia AS"),
        Provider(id=3,provider_name="TTÜ Sport"),
        Provider(id=4,provider_name="Bitstop Kohvik OÜ")
    ]
    
    for p in providers:
        #only if provider does not exist, add
        query = session.query(Provider).filter_by(provider_name=p.provider_name)
        if query.all() == []:
            session.add(p)
    
    session.commit()
    return

#to insert canteens
def insert_canteens(session):
    ttu = [
        Canteen(1,'Economics- and social science building canteen','Akadeemia tee 3SOC- building',time(8,30),time(18,30)),
        Canteen(1,'Libary canteen','Akadeemia tee 1/Ehitajate tee 7',time(8,30),time(19,00)),
        Canteen(1,'U06 building canteen',"Ehitajate tee 5/6",time(9,00),time(16,00)),
        Canteen(2,'Main building Daily lunch restaurant','Ehitajate tee 5 U01 building',time(9,00),time(16,30)),
        Canteen(2,'Main building Deli cafe', 'Ehitajate tee 5 U01 building',time(9,00), time(16,30)),
        Canteen(2,'ICT building canteen','Raja 15/Mäepealse 1',time(9,00),time(16,00)),
        Canteen(2,'Natural Science building canteen','Akadeemia tee 15 SCI building',time(9,00),time(16,00)),
        Canteen(3,'Sports building canteen','Männiliiva 7 S01 building',time(11,00),time(20,00))
    ]
    
    itc = Canteen(4,'bitStop CAFE','Raja 4C',time(9,30),time(16,00))
    for c in ttu:
        #only if canteen does not exist, add
        query = session.query(Canteen).filter_by(name=c.name)
        if query.all() == []:
            session.add(c)
    
    session.add(itc)
    session.commit()
    return

# function to create a connection to the db and initialize it (if required)
def start(file_path="db.diners"):
    if(file_path == ''):
        print("No file path provided!")
        return
        
    session = create_db(file_path)
    insert_providers(session)
    insert_canteens(session)
    return session