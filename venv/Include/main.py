import requests
from bs4 import BeautifulSoup

#URLs
euroMillionsResultsURL = 'https://www.lottery.ie/draw-games/results/view?game=euromillions'
irishLottoResultsURL = 'https://www.lottery.ie/draw-games/results/view?game=lotto'

#Euromillons
euromillions_html_text = requests.get(euroMillionsResultsURL).text
soup = BeautifulSoup(euromillions_html_text, 'html.parser')

#IrishLotto
irish_lotto_html_text = requests.get(irishLottoResultsURL).text
soup2 = BeautifulSoup(irish_lotto_html_text, 'html.parser')

#Euromillions functions for scraping the results

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


#Irish Lotto functions for scraping the results

def getLottoNumbers():
    lottoNumbers = []
    winningResults = soup2.find_all("div", {"class": "pick-number"})
    for numbers in range(7):
        lottoNumbers.append(winningResults[numbers].findChild("label").text)
    return lottoNumbers

def getLottoPlusOneNumbers():
    lottoPlusOneNumbers = []
    winningResults = soup2.find_all("div", {"class": "pick-number"})
    for numbers in range(7, 14):
        lottoPlusOneNumbers.append(winningResults[numbers].findChild("label").text)
    return lottoPlusOneNumbers

def getLottoPlusTwoNumbers():
    lottoPlusTwoNumbers = []
    winningResults = soup2.find_all("div", {"class": "pick-number"})
    for numbers in range(14, 21):
        lottoPlusTwoNumbers.append(winningResults[numbers].findChild("label").text)
    return lottoPlusTwoNumbers
