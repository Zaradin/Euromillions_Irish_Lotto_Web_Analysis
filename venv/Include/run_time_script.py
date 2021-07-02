import schedule
import time
import database
import create_database

# Create Database and Tables if they do not already exisits
create_database.create_tables_if_not_exisits()

def do_euromillions():
    database.insertEuromillionsResults()
    database.insertEuromillionsPlusResults()

def do_irishlotto():
    database.insertIrishLottoResults()
    database.insertIrishLottoPlusOneResults()
    database.insertIrishLottoPlusTwoResults()

#Euromillions results
schedule.every().tuesday.at("21:30").do(do_euromillions)
schedule.every().friday.at("21:30").do(do_euromillions)

#Irish Lotto Results with plus draws
schedule.every().wednesday.at("21:30").do(do_irishlotto)
schedule.every().saturday.at("21:30").do(do_irishlotto)


while True:
    schedule.run_pending()
    time.sleep(1)