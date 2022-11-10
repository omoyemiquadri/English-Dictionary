from bs4 import BeautifulSoup
import requests
import pyfiglet as figlet

fig = figlet.figlet_format('Dictionary')

print(fig, '''              ONLINE ENGLISH DICTIONARY ''' ,)
def dictionary(word):
    page = requests.get( 'https://www.dictionary.com/browse/'+word)
    soup = BeautifulSoup(page.content, 'html.parser')
    site = soup.find_all('div', {'value': '1'})
    print(site[0].get_text())
    
word = input('Enter your search term: ')
dictionary(word)
print('Do you want to search again?')
 
opt = input('yes or no: ')
if opt == 'yes':
     word= input('Enter your search term: ')
     dictionary(word)
     while opt == 'yes':
         opt = input('yes or no: ')
         word= input('Enter your search term: ')
         dictionary(word)
         if opt == 'no':
             print('Thanks and have a nice day')
quit()
