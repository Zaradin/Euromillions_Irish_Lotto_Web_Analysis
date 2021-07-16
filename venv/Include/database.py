import main
import sqlite3

from datetime import datetime
con = sqlite3.connect("Results")


class insertEuro():
    def __init__(self):
        self.date = datetime.today().strftime('%d-%m-%Y')

    def insertEuromillionsResults(self):
        self.euroMillionsNumbers = main.EuromillionsToHTML().getEuroMillionsNumbers()
        con.execute("INSERT INTO euromillionsResults VALUES (?, ?, ?, ?, ?, ?, ?, ?);", (
        self.date, self.euroMillionsNumbers[0], self.euroMillionsNumbers[1], self.euroMillionsNumbers[2], self.euroMillionsNumbers[3],
        self.euroMillionsNumbers[4], self.euroMillionsNumbers[5], self.euroMillionsNumbers[6]))
        con.commit()

    def insertEuromillionsPlusResults(self):
        self.euroMillionsPlusNumbers = main.EuromillionsToHTML().getEuroMillionsPlusNumbers()
        con.execute("INSERT INTO euromillionsPlusResults VALUES (?, ?, ?, ?, ?, ?);", (
        self.date, self.euroMillionsPlusNumbers[0], self.euroMillionsPlusNumbers[1], self.euroMillionsPlusNumbers[2], self.euroMillionsPlusNumbers[3],
        self.euroMillionsPlusNumbers[4]))
        con.commit()

class insertIrish():
    def __init__(self):
        self.date = datetime.today().strftime('%d-%m-%Y')

    def insertIrishLottoResults(self):
        self.irishLottoNumbers = main.IrishLottoToHTML().getLottoNumbers()
        con.execute("INSERT INTO irishLottoResults VALUES (?, ?, ?, ?, ?, ?, ?, ?);", (
        self.date, self.irishLottoNumbers[0], self.irishLottoNumbers[1], self.irishLottoNumbers[2], self.irishLottoNumbers[3],
        self.irishLottoNumbers[4], self.irishLottoNumbers[5], self.irishLottoNumbers[6]))
        con.commit()

    def insertIrishLottoPlusOneResults(self):
        self.irishLottoPlusOneNumbers = main.IrishLottoToHTML().getLottoPlusOneNumbers()
        con.execute("INSERT INTO irishLottoPlusOneResults VALUES (?, ?, ?, ?, ?, ?, ?, ?);", (
        self.date, self.irishLottoPlusOneNumbers[0], self.irishLottoPlusOneNumbers[1], self.irishLottoPlusOneNumbers[2], self.irishLottoPlusOneNumbers[3],
        self.irishLottoPlusOneNumbers[4], self.irishLottoPlusOneNumbers[5], self.irishLottoPlusOneNumbers[6]))
        con.commit()

    def insertIrishLottoPlusTwoResults(self):
        self.irishLottoPlusTwoNumbers = main.IrishLottoToHTML().getLottoPlusTwoNumbers()
        con.execute("INSERT INTO irishLottoPlusTwoResults VALUES (?, ?, ?, ?, ?, ?, ?, ?);", (
        self.date, self.irishLottoPlusTwoNumbers[0], self.irishLottoPlusTwoNumbers[1], self.irishLottoPlusTwoNumbers[2], self.irishLottoPlusTwoNumbers[3],
        self.irishLottoPlusTwoNumbers[4], self.irishLottoPlusTwoNumbers[5], self.irishLottoPlusTwoNumbers[6]))
        con.commit()

