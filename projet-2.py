import requests
from bs4 import BeautifulSoup


with open('scraping.csv', 'w', encoding="utf-8") as outf:
    outf.write('url, upc, title, price_including_tax, price_excluding_tax, number_available, product_description, category, image_url \n')

    for i in range(1,50):
        page = 'http://books.toscrape.com/catalogue/category/books/mystery_3/page-' + str(i) + '.html'
        response = requests.get(page)

        if response.ok:
            soup = BeautifulSoup(response.content, 'html.parser')

            liens = soup.find_all('h3')
            x = 0
            for lien in liens:
                a = lien.find('a')
                url = a['href']
                url = url.replace('../../../', 'http://books.toscrape.com/catalogue/')

                response2 = requests.get(url)
                if response2.ok:
                    soup2 = BeautifulSoup(response2.content, 'html.parser')

                    # UPC, Prices, Availability
                    rows = soup2.find_all('tr')
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
                    title = soup2.find('h1').text
                    title = title.replace(',', '-')

                    #Product Description
                    col = 0
                    for data in soup2.find_all('p'):
                        data = data.get_text()
                        if col == 3:
                            product_description = data
                        col += 1


                    #Category
                    col = 0
                    for data in soup2.find_all('li'):
                        data = data
                        if col == 2:
                            category = data.text
                        col += 1
                    category = category.strip()


                    #Image link
                    data = soup2.find('img')
                    imglink = (data['src'])
                    imglink = imglink.replace('../..', 'http://books.toscrape.com')

                    product_description = product_description.replace(',', '-')

                    #Test
                    print('Link : ' + url)
                    print('Title : ' + title)
                    print('UPC : ' + upc)
                    print('Price excluding tax : ' + price)
                    print('Price including tax : ' + pricetax)
                    print('Number available : ' + availability)
                    print('Product description : ' + product_description)
                    print('Image link : ' + imglink)
                    print('Category : ' + category)

                    #Output CSV
                    outf.write(url + ',' + upc + ',' + title + ',' + price + ',' + pricetax + ',' + availability + ',' + product_description + ',' + category + ',' + imglink + '\n')

        else:
            break