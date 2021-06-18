import requests
from bs4 import BeautifulSoup

euroMillionsResultsURL = 'https://www.lottery.ie/draw-games/results/view?game=euromillions'
irishLottoResultsURL = 'https://www.lottery.ie/draw-games/results/view?game=lotto'
html_text = requests.get(euroMillionsResultsURL).text
soup = BeautifulSoup(html_text, 'html.parser')

def getEuroMillionsNumbers():
    euroMillionsNumbers = []
    winningResults = soup.find_all("div", {"class": "pick-number"})
    for numbers in range(7):
        euroMillionsNumbers.append(winningResults[numbers].findChild("label").text)
    return euroMillionsNumbers

def getEuroMillionsPlusNumbers():
    euroMillionsPlusNumbers = []
    winningResults = soup.find_all("div", {"class": "pick-number"})
    for plusNumbers in range(7, 12):
        euroMillionsPlusNumbers.append(winningResults[plusNumbers].findChild("label").text)
    return euroMillionsPlusNumbers

def getLuckyStars():
    luckyStars = []
    winningResults = soup.find_all("div", {"class": "pick-number"})
    for luckyNumbers in range(5, 7):
        luckyStars.append(winningResults[luckyNumbers].findChild("label").text)
    return luckyStars

def getResultsDate():
    resultDate = soup.select('h4')[0].text.strip()
    return resultDate
