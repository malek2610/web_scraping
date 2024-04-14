import requests
from bs4 import BeautifulSoup

url = "https://codeavecjonathan.com/scraping/recette/"

def get_text_if_not_none(e):
    # Return the text of html element if available or None if not
    if e:
        return e.text.strip()
    
    return None

response = requests.get(url)
response.encoding = response.apparent_encoding

if response.status_code == 200:
    print(f"OK - RESPONSE CODE = {response.status_code}")

    html = response.text
    # print(html)

    # Save the source into html file
    src_file = open("source.html", "w")
    src_file.write(html)
    src_file.close()

    # Parsing and extracting the data
    soup = BeautifulSoup(html, "html5lib")

    title = soup.find("h1").text
    print(f"Recipe: {title}")

    description = get_text_if_not_none(soup.find("p", class_="description"))
    print(f"Description: \n{description}")

    div_ingredients = soup.find("div", class_="ingredients")
    ingredients = div_ingredients.find_all("p")

    print("Ingredients:")

    for ingredient in ingredients:
        print(f"- {get_text_if_not_none(ingredient)}")
    
    preparation_table = soup.find("table", class_="preparation")
    steps = preparation_table.find_all("td", class_="preparation_etape")

    print("Preparation:")

    for step in steps:
        print(f"- {get_text_if_not_none(step)}")

else:
    print(f"ERROR - RESPONSE CODE = {response.status_code}")