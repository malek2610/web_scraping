# WEB SCRAPING TRAINING

## Description
Web scraping is a method helps to extract data and information from any web site. This project was created to learn web scraping using python.
It was based on the flowing tutorial [[1](https://www.youtube.com/watch?v=HCV6nEACQo4)]

It will cover:
- First steps of web scraping using [requests](https://docs.python-requests.org/en/latest/index.html) and [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/)
- How to get around web sites protections against web scraping
- What is legal and not on web scraping
- How to create an advanced project for web scraping
- How to use the AI to generate codes for scraping

## Requirements
```bash
beautifulsoup4==4.12.3
requests==2.31.0
html5lib==1.1
```

## Examples
### Scraping Cooking Recipe
This is the very first example, where it is demonstrated how to use `requests` and `bs4` libraries to perform web scraping

The script is in the `scraping_recipe.py` file

#### STEP 1 - IMPORT `Requests` & `BeautifulSoup` LIBRARIES
```python
import requests
from bs4 import BeautifulSoup
```

#### STEP 2 - GET THE HTML SOURCE FROM THE URL
```python
url = "..."
response = requests.get(url)
```

The encoding is important for special characters, therefore, the following code can be used to use the exact encoding of the `url`

```python
response.encoding = response.apparent_encoding
```

The status of the `response` can be displayed using `response.status_code`

#### STEP 3 - PARSING & EXTRACTION OF DATA 
```python
soup = BeautifulSoup(html, "html5lib")
```

The `find` command can be used to extract data by searching specific `html` tag, the following example shows how to get the first `<h1>`. We can also obtain the content only by adding `.text` to the `find` command

```python
soup.find("h1")
soup.find("h1").text
```

If we would like to extract content from a specific tag (*i.e.* using a special `class`), we can add an argument to the `find` command

```python
soup.find("p", class_ = "...").text
```

**Note:** We have to add the underscore to the word `class_` here to differentiate it with the python key word `class`

Now, if we would like to obtain all elements, we have to use the `find_all` command instead of `find`

```python
soup.find_all("...")
```

We can also search inside a specific part of the page by creating new `soup` element, and use either `find` or `find_all` on this new element

```python
soup_element = soup.find("...", class_="...")
soup_element.find_all("...")
```

**Note:** On this example, we used only `find` and `find_all` commands. However, it is also possible to use other commands to extract same data such `select` ...etc. For more details, read the documentation of `BeautifulSoup` library

## Links
- [Cooking recipe web site](https://codeavecjonathan.com/scraping/recette/)
- [ScrapeThisSite.com](https://www.scrapethissite.com/pages/)

## Authors
- [Malek B.](https://www.github.com/malek2610)
