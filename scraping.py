import requests
import json
from bs4 import BeautifulSoup


from constantes import BASE_URL



def get_main_entreprise_matrixe_page(session):
    response = session.get(BASE_URL)  
    if response.status_code == 200:
        return response.text
    return None

def matrix_table_parser(content_page):
    soup = BeautifulSoup(content_page, 'html.parser')
    return soup.find('table', class_="matrix side")

def pars_Tactic(tag):
    tactic_name=tag.find("a")
    return [tactic_name.text, tactic_name.get("title")]

def matrix_tactic_name(content_page):
    return [str(pars_Tactic(tag)) for tag in matrix_table_parser(content_page).find_all("td", class_="tactic name")]


if __name__ == "__main__":

    with requests.Session() as session:  
        main_page_content = get_main_entreprise_matrixe_page(session)
        with open("tactic.json", 'w') as f:
            json.dump(matrix_tactic_name(main_page_content), f, indent=4)
