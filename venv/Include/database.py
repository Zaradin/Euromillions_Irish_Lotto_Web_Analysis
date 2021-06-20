import main
import sqlite3

from datetime import datetime
con = sqlite3.connect("Results")

date = datetime.today().strftime('%d-%m-%Y')

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
    irishLottoNumbers = main.getLottoNumbers()
    con.execute("INSERT INTO irishLottoResults VALUES (?, ?, ?, ?, ?, ?, ?, ?);", (
    date, irishLottoNumbers[0], irishLottoNumbers[1], irishLottoNumbers[2], irishLottoNumbers[3],
    irishLottoNumbers[4], irishLottoNumbers[5], irishLottoNumbers[6]))
    con.commit()

def insertIrishLottoPlusOneResults():
    irishLottoPlusOneNumbers = main.getLottoPlusOneNumbers()
    con.execute("INSERT INTO irishLottoPlusOneResults VALUES (?, ?, ?, ?, ?, ?, ?, ?);", (
    date, irishLottoPlusOneNumbers[0], irishLottoPlusOneNumbers[1], irishLottoPlusOneNumbers[2], irishLottoPlusOneNumbers[3],
    irishLottoPlusOneNumbers[4], irishLottoPlusOneNumbers[5], irishLottoPlusOneNumbers[6]))
    con.commit()

def insertIrishLottoPlusTwoResults():
    irishLottoPlusTwoNumbers = main.getLottoPlusTwoNumbers()
    con.execute("INSERT INTO irishLottoPlusTwoResults VALUES (?, ?, ?, ?, ?, ?, ?, ?);", (
    date, irishLottoPlusTwoNumbers[0], irishLottoPlusTwoNumbers[1], irishLottoPlusTwoNumbers[2], irishLottoPlusTwoNumbers[3],
    irishLottoPlusTwoNumbers[4], irishLottoPlusTwoNumbers[5], irishLottoPlusTwoNumbers[6]))
    con.commit()

