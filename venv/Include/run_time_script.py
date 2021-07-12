import schedule
import time
import database

# Create Database and Tables if they do not already exisits
import sqlite3

con = sqlite3.connect("Results")
cursor = con.cursor()

#Euromillions Table
cursor.execute("CREATE TABLE IF NOT EXISTS euromillionsResults ( date DATE (10), lottoNum1 INTEGER (2), lottoNum2 INTEGER (2), lottoNum3 INTEGER (2), lottoNum4 INTEGER (2), lottoNum5 INTEGER (2), lottoNum6 INTEGER (2), lottoNum7 INTEGER (2) )")
#Euromillions Plus Table
cursor.execute("CREATE TABLE IF NOT EXISTS euromillionsPlusResults ( date DATE (10), lottoNum1 INTEGER (2), lottoNum2 INTEGER (2), lottoNum3 INTEGER (2), lottoNum4 INTEGER (2), lottoNum5 INTEGER (2) )")


#irishLotto Table
cursor.execute("CREATE TABLE IF NOT EXISTS irishLottoResults ( date DATE (10), lottoNum1 INTEGER (2), lottoNum2 INTEGER (2), lottoNum3 INTEGER (2), lottoNum4 INTEGER (2), lottoNum5 INTEGER (2), lottoNum6 INTEGER (2), lottoNum7 INTEGER (2) )")
#irishLottoPlusOne Table
cursor.execute("CREATE TABLE IF NOT EXISTS irishLottoPlusOneResults ( date DATE (10), lottoNum1 INTEGER (2), lottoNum2 INTEGER (2), lottoNum3 INTEGER (2), lottoNum4 INTEGER (2), lottoNum5 INTEGER (2), lottoNum6 INTEGER (2), lottoNum7 INTEGER (2) )")
#irishLottoPlusTwo Table
cursor.execute("CREATE TABLE IF NOT EXISTS irishLottoPlusTwoResults ( date DATE (10), lottoNum1 INTEGER (2), lottoNum2 INTEGER (2), lottoNum3 INTEGER (2), lottoNum4 INTEGER (2), lottoNum5 INTEGER (2), lottoNum6 INTEGER (2), lottoNum7 INTEGER (2) )")
con.commit()
cursor.close()
con.close()

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