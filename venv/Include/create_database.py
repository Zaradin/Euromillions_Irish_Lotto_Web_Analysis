import sqlite3

con = sqlite3.connect("Results")
cursor = con.cursor()

def create_tables_if_not_exisits():
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