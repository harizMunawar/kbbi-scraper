from bs4 import BeautifulSoup
import requests
import random

def definition(word:str):
    host = requests.get(f'https://kbbi.co.id/arti-kata/{word}')
    soup = BeautifulSoup(host.text, 'html.parser')
    meaning = soup.find('p', attrs={'class': 'arti'}).find_next('i').next_sibling
    
    return meaning

def random_word(definition:bool = False): 
    host = requests.get('https://kbbi.co.id/')       
    soup = BeautifulSoup(host.text, 'html.parser')
    rw_container = soup.find('div', attrs={'class': 'panel panel-default'})
    rw_body = rw_container.find('div', attrs={'class': 'panel-body'})

    return(random.choice([word.contents[0] for word in rw_body.find_all('a')]))