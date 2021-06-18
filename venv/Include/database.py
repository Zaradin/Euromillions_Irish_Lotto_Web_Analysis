import main
import sqlite3

from datetime import datetime
con = sqlite3.connect("Results")

date = datetime.today().strftime('%d-%m-%Y')

# TODO I also need to create more tabels in the database for the different lottos, for example. A table for euromillions irish plus draw, and irish lotto plus 1, lotto plus 2 and so on....

def insertEuromillionsResults():
    euroMillionsNumbers = main.getEuroMillionsNumbers()
    con.execute("INSERT INTO euromillionsResults VALUES (?, ?, ?, ?, ?, ?, ?, ?);", (
    date, euroMillionsNumbers[0], euroMillionsNumbers[1], euroMillionsNumbers[2], euroMillionsNumbers[3],
    euroMillionsNumbers[4], euroMillionsNumbers[5], euroMillionsNumbers[6]))
    con.commit()

def insertEuromillionsPlusResults():
    euroMillionsPlusNumbers = main.getEuroMillionsPlusNumbers()
    con.execute("INSERT INTO euromillionsPlusResults VALUES (?, ?, ?, ?, ?, ?);", (
    date, euroMillionsPlusNumbers[0], euroMillionsPlusNumbers[1], euroMillionsPlusNumbers[2], euroMillionsPlusNumbers[3],
    euroMillionsPlusNumbers[4]))
    con.commit()

def insertIrishLottoResults():
    pass

def insertIrishLottoPlus1Results():
    pass

def insertIrishLottoPlus2Results():
    pass
