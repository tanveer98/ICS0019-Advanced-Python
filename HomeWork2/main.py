#from ITCollege_Diners_Mhasan.query import find_by_time,find_by_provider
from diners.db import start
from diners.models import Provider,Canteen
from datetime import time
# query to get list of canteens.
def find_canteens(session):
    t_open = time(16,15)
    t_closed = time(18,00)
    canteens = session.query(Canteen).filter(Canteen.time_open <= t_open, Canteen.time_closed >= t_closed)
    all = canteens.all()
    print(f"Canteens open between {t_open} and {t_closed} \n\n")
    for canteen in canteens:
        print(str(canteen))

    prov = "Rahva Toit"
    canteens = session.query(Canteen,Provider).filter(Canteen.provider_id == Provider.id, Provider.provider_name == prov)
    all = canteens.all()
    print(f"Canteens owned by {prov} \n\n")
    for canteen in canteens:
        str_ = f"Provider: {canteen[0].provider.provider_name}" + str(canteen[0])
        print(str_)
    return


if __name__ == "__main__":
    # provide a new path to the db if you want!
    session = start("diners.db")
    find_canteens(session)