import requests
from bs4 import BeautifulSoup


class EuromillionsToHTML():
    def __init__(self):
        self.euroMillionsResultsURL = 'https://www.lottery.ie/draw-games/results/view?game=euromillions'
        self.euromillions_html_text = requests.get(self.euroMillionsResultsURL).text
        self.soup = BeautifulSoup(self.euromillions_html_text, 'html.parser')

    #Euromillions functions for scraping the results
    def getEuroMillionsNumbers(self):
        self.euroMillionsNumbers = []
        self.winningResults = self.soup.find_all("div", {"class": "pick-number"})
        for numbers in range(7):
            self.euroMillionsNumbers.append(self.winningResults[numbers].findChild("label").text)
        return self.euroMillionsNumbers

    def getEuroMillionsPlusNumbers(self):
        self.euroMillionsPlusNumbers = []
        self.winningResults = self.soup.find_all("div", {"class": "pick-number"})
        for plusNumbers in range(7, 12):
            self.euroMillionsPlusNumbers.append(self.winningResults[plusNumbers].findChild("label").text)
        return self.euroMillionsPlusNumbers

    def getLuckyStars(self):
        self.luckyStars = []
        self.winningResults = self.soup.find_all("div", {"class": "pick-number"})
        for luckyNumbers in range(5, 7):
            self.luckyStars.append(self.winningResults[luckyNumbers].findChild("label").text)
        return self.luckyStars

    def getResultsDate(self):
        self.resultDate = self.soup.select('h4')[0].text.strip()
        return self.resultDate



class IrishLottoToHTML():
    def __init__(self):
        self.irishLottoResultsURL = 'https://www.lottery.ie/draw-games/results/view?game=lotto'
        self.irish_lotto_html_text = requests.get(self.irishLottoResultsURL).text
        self.soup = BeautifulSoup(self.irish_lotto_html_text, 'html.parser')

    # Irish Lotto functions for scraping the results
    def getLottoNumbers(self):
        self.lottoNumbers = []
        self.winningResults = self.soup.find_all("div", {"class": "pick-number"})
        for numbers in range(7):
            self.lottoNumbers.append(self.winningResults[numbers].findChild("label").text)
        return self.lottoNumbers

    def getLottoPlusOneNumbers(self):
        self.lottoPlusOneNumbers = []
        self.winningResults = self.soup.find_all("div", {"class": "pick-number"})
        for numbers in range(7, 14):
            self.lottoPlusOneNumbers.append(self.winningResults[numbers].findChild("label").text)
        return self.lottoPlusOneNumbers

    def getLottoPlusTwoNumbers(self):
        self.lottoPlusTwoNumbers = []
        self.winningResults = self.soup.find_all("div", {"class": "pick-number"})
        for numbers in range(14, 21):
            self.lottoPlusTwoNumbers.append(self.winningResults[numbers].findChild("label").text)
        return self.lottoPlusTwoNumbers

    def getResultsDate(self):
        self.resultDate = self.soup.select('h4')[0].text.strip()
        return self.resultDate