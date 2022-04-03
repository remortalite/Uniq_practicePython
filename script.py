from bs4 import BeautifulSoup as bs
import requests
import sys

def print_error(e) -> None:
    print("ERROR!")
    print(e, file=sys.stderr)

def get_page(url: str):
    try:
        page = requests.get(url)
    except Exception as e:
        print_error(e)
        exit(-1)
    return page

def run(url: str) -> list:
    #page = requests.get(url)
    page = get_page(url)

    soup = bs(page.text, "html.parser")

    table = soup.find_all(class_="cmc-table")[0]
    table_rows = table.find_all("tbody")[0].find_all("tr")

    data = []
    for i in range(len(table_rows)):
        if (table_rows[i].get("class")): continue;
        try : 
            name = table_rows[i].find_all("td")[2].find('p').text
            price = table_rows[i].find_all("td")[3].find('span').text
            market_cup = table_rows[i].find_all("td")[6].find('span').text
            data.append({'name': name, 'price': price, 'market_cup': market_cup})
        except Exception as e:
            print_error(e)
            continue
        
    for i in range(len(data)):
        print(f"{data[i]['name']:16} {data[i]['price']:16} {data[i]['market_cup']}")

    return data

if __name__ == "__main__":
    url = r"https://coinmarketcap.com/"

    data = run(url)
