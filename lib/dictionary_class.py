from bs4 import BeautifulSoup
import requests

class Dict:
    def __init__(self):
        self.word = ""

    def dictionary(self, word):
        try:
            page = requests.get('https://www.dictionary.com/browse/'+word)
            soup = BeautifulSoup(page.content, 'html.parser')
            dic = soup.find_all('div', {'value':'1'})
            print(dic[0].get_text())
        except (IndexError):
            print("Wrong Input.")

    def run(self):
        while True:
            self.word = input("Enter your search: ")
            self.dictionary(self.word)
            x = input("Do you want to run again (Y/N): ").lower()
            if x == 'y':
                continue
            elif x == 'n':
                break
            else:
                print("Wrong entry.")
                break

