import requests
from bs4 import BeautifulSoup


with open('scraping.csv', 'w') as outf:
    outf.write('url, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, image_url \n')
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
                availability = data.text
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

        product_description = product_description.replace(',', '-')


        print('Link : ' + url)
        print('Title : ' + title)
        print('UPC : ' + upc)
        print('Price excluding tax : ' + price)
        print('Price including tax : ' + pricetax)
        print('Number available : ' + availability)
        print('Product description : ' + product_description)
        print('Image link : ' + imglink)
        print('Category : ' + category)
        outf.write(url + ',' + upc + ',' + title + ',' + price + ',' + pricetax + ',' + availability + ',' + product_description + ',' + category + ',' + imglink + '\n')