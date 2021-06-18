import main
import sqlite3

from datetime import datetime
# TODO create functions for each euromillions and irish lotto results, "insert euromillions results in to database", "insert irish lotto plus 1 into database and so on...."
con = sqlite3.connect("euromillionsResults")

euroMillionsNumbers = main.getEuroMillionsNumbers()
date = datetime.today().strftime('%d-%m-%Y')

con.execute("INSERT INTO euromillionsResults VALUES (?, ?, ?, ?, ?, ?, ?, ?);", (date, euroMillionsNumbers[0], euroMillionsNumbers[1], euroMillionsNumbers[2], euroMillionsNumbers[3], euroMillionsNumbers[4], euroMillionsNumbers[5], euroMillionsNumbers[6]))
con.commit()

# TODO I also need to create more tabels in the database for the different lottos, for example. A table for euromillions irish plus draw, and irish lotto plus 1, lotto plus 2 and so on....