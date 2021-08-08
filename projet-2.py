import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/a-study-in-scarlet-sherlock-holmes-1_656/index.html'

response = requests.get(url)



if response.ok:
    soup = BeautifulSoup(response.content, 'html.parser')

# UPC, Prices, Availability
    rows = soup.find_all('tr')
    col = 0
    for row in rows:
        data = row.find('td')
        if col == 0:
            upc = data.text
        if col == 2:
            price = data.text
        if col == 3:
            pricetax = data.text
        if col == 5:
            availablity = data.text
        col += 1


#Title
    title = soup.find('h1').text


#Product Description
    col = 0
    for data in soup.find_all('p'):
        data = data.get_text()
        if col == 3:
            product_description = data
        col += 1


#Category
    col = 0
    for data in soup.find_all('li'):
        data = data
        if col == 2:
            category = data.text
        col += 1
    category = category.strip()


#Image link
    data = soup.find('img')
    imglink = (data['src'])
    imglink = imglink.replace('../..', 'http://books.toscrape.com')



    print('Link : ' + url)
    print('Title : ' + title)
    print('UPC : ' + upc)
    print('Price excluding tax : ' + price)
    print('Price including tax : ' + pricetax)
    print('Number available : ' + availablity)
    print('Product description : ' + product_description)
    print('Image link : ' + imglink)
    print('Category : ' + category)
