import requests
from bs4 import BeautifulSoup
euroMillionsResultsURL = 'https://www.lottery.ie/draw-games/results/view?game=euromillions'
irishLottoResultsURL = 'https://www.lottery.ie/draw-games/results/view?game=lotto'
#Euromillons
euromillions_html_text = requests.get(euroMillionsResultsURL).text
soup = BeautifulSoup(euromillions_html_text, 'html.parser')

#IrishLotto
irish_lotto_html_text = requests.get(irishLottoResultsURL).text
soup2 = BeautifulSoup(irish_lotto_html_text, 'html.parser')


def get_euroMillionsHTML():
    #URL
    euroMillionsResultsURL = 'https://www.lottery.ie/draw-games/results/view?game=euromillions'

    # Euromillons
    euromillions_html_text = requests.get(euroMillionsResultsURL).text
    soup = BeautifulSoup(euromillions_html_text, 'html.parser')
    return soup

def get_irishLottoHTML():
    #URL
    irishLottoResultsURL = 'https://www.lottery.ie/draw-games/results/view?game=lotto'

    # IrishLotto
    irish_lotto_html_text = requests.get(irishLottoResultsURL).text
    soup2 = BeautifulSoup(irish_lotto_html_text, 'html.parser')
    return soup2

#Euromillions functions for scraping the results
def getEuroMillionsNumbers():
    soup = get_euroMillionsHTML()
    euroMillionsNumbers = []
    winningResults = soup.find_all("div", {"class": "pick-number"})
    for numbers in range(7):
        euroMillionsNumbers.append(winningResults[numbers].findChild("label").text)
    return euroMillionsNumbers

def getEuroMillionsPlusNumbers():
    soup = get_euroMillionsHTML()
    euroMillionsPlusNumbers = []
    winningResults = soup.find_all("div", {"class": "pick-number"})
    for plusNumbers in range(7, 12):
        euroMillionsPlusNumbers.append(winningResults[plusNumbers].findChild("label").text)
    return euroMillionsPlusNumbers

def getLuckyStars():
    soup = get_euroMillionsHTML()
    luckyStars = []
    winningResults = soup.find_all("div", {"class": "pick-number"})
    for luckyNumbers in range(5, 7):
        luckyStars.append(winningResults[luckyNumbers].findChild("label").text)
    return luckyStars

def getResultsDate():
    resultDate = soup.select('h4')[0].text.strip()
    return resultDate
print(soup.select('h4')[0].text)

#Irish Lotto functions for scraping the results
def getLottoNumbers():
    soup2 = get_irishLottoHTML()
    lottoNumbers = []
    winningResults = soup2.find_all("div", {"class": "pick-number"})
    for numbers in range(7):
        lottoNumbers.append(winningResults[numbers].findChild("label").text)
    return lottoNumbers

def getLottoPlusOneNumbers():
    soup2 = get_irishLottoHTML()
    lottoPlusOneNumbers = []
    winningResults = soup2.find_all("div", {"class": "pick-number"})
    for numbers in range(7, 14):
        lottoPlusOneNumbers.append(winningResults[numbers].findChild("label").text)
    return lottoPlusOneNumbers

def getLottoPlusTwoNumbers():
    soup2 = get_irishLottoHTML()
    lottoPlusTwoNumbers = []
    winningResults = soup2.find_all("div", {"class": "pick-number"})
    for numbers in range(14, 21):
        lottoPlusTwoNumbers.append(winningResults[numbers].findChild("label").text)
    return lottoPlusTwoNumbers
