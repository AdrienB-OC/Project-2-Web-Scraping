import requests
from bs4 import BeautifulSoup


def get_review_rating(soup):
    review_rating = soup.find('div', {'class': 'col-sm-6 product_main'})
    p = review_rating.find('p', {'class': 'star-rating'})
    review_rating = p.get('class')
    review_rating = str(review_rating)
    review_rating = review_rating.replace("['star-rating', '", "")
    review_rating = review_rating.replace("']", "")

    return review_rating

def get_category(soup):
    col = 0
    for data in soup.find_all('li'):
        data = data
        if col == 2:
            category = data.text
        elif col > 2:
            break
        col += 1
    category = category.strip()

    return category

def get_product_description(soup):
    col = 0
    for data in soup.find_all('p'):
        data = data.get_text()
        if col == 3:
            product_description = data
        elif col > 3:
            break
        col += 1
    product_description = product_description.replace(',', '')
    product_description = product_description.replace('"', "'")
    return product_description

def get_attributes(soup):
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
    attributes = f"{upc}, {price}, {pricetax}, {availability}"
    return attributes

def get_imglink(soup):
    data = soup.find('img')
    imglink = (data['src'])
    imglink = imglink.replace('../..', 'http://books.toscrape.com')
    return imglink

def get_all_data(soup):
    # Get UPC, Prices, Availability
    attributes = get_attributes(soup)

    # Get Title
    title = soup.find('h1').text
    title = title.replace(',', '-')

    # Get Product Description
    product_description = get_product_description(soup)

    # Get Category
    category = get_category(soup)

    # Get Review Rating
    review_rating = get_review_rating(soup)

    # Get Image link
    imglink = get_imglink(soup)

    # Test
    print('Link : ' + url)
    print('Title : ' + title)
    # print('UPC : ' + upc)
    # print('Price excluding tax : ' + price)
    # print('Price including tax : ' + pricetax)
    # print('Number available : ' + availability)
    # print('Product description : ' + product_description)
    # print('Image link : ' + imglink)
    print('Category : ' + category)
    # print(review_rating)
    
    all_data = f"{title},{attributes},{product_description},{category},{review_rating},{imglink}"
    return all_data

home = 'http://books.toscrape.com/index.html'
response = requests.get(home)
soup = BeautifulSoup(response.content, 'html.parser')

multiplePages = False
catLink = soup.find('div', {'class': 'side_categories'})
ligne = 1
for li in catLink.find_all('li'):

    b = li.find('a')
    lien = b['href']
    catName = b.text.strip()
    lien = 'http://books.toscrape.com/' + lien

    if catName == 'Books':
        pass
    else:
        for i in range(1,10):
            if i == 1:
                print(catName)
                print(lien)

            elif i == 2 and (requests.get(lien.replace('index.html', 'page-' + str(i) + '.html')).ok):
                lien = lien.replace('index.html', 'page-' + str(i) + '.html')
                print(lien)
            elif i > 2 and (requests.get(lien.replace('page-2.html', 'page-' + str(i) + '.html')).ok):
                lienB = lien.replace('page-2.html', 'page-' + str(i) + '.html')
                print(lienB)
                multiplePages = True
            else:
                multiplePages = False

                break



            with open(str(catName) + '.csv', 'w', encoding="utf-8") as outf:
                outf.write('url, title, upc, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url \n')



                for j in range(1, 10):


                    if j == 1:
                        page = lien
                        response = requests.get(page)
                    elif j == 2 and i == 2 and (requests.get(lien.replace('index.html', 'page-' + str(i) + '.html')).ok):
                        page = lien
                        response = requests.get(page)
                    elif multiplePages and i > 2 and j > 2:
                        page = lienB
                        response = requests.get(page)
                    else:
                        response = requests.get('http://books.toscrape.com/index8.html')
                        break
                    #page = 'http://books.toscrape.com/catalogue/category/books/mystery_3/page-' + str(i) + '.html'





                    if response.ok:

                        soup2 = BeautifulSoup(response.content, 'html.parser')
                        liens = soup2.find_all('h3')

                        pages_details = ""

                        for lienC in liens:
                            a = lienC.find('a')
                            url = a['href']
                            url = url.replace('../../../', 'http://books.toscrape.com/catalogue/')


                            response2 = requests.get(url)
                            if response2.ok:
                                soup3 = BeautifulSoup(response2.content, 'html.parser')

                                all_data = get_all_data(soup3)
                                # Get UPC, Prices, Availability
                                #attributes = get_attributes(soup3)

                                # Get Title
                                #title = soup3.find('h1').text
                                #title = title.replace(',', '-')

                                # Get Product Description
                                #product_description = get_product_description(soup3)

                                # Get Category
                                #category = get_category(soup3)

                                # Get Review Rating
                                #review_rating = get_review_rating(soup3)
                                #print(review_rating)

                                # Get Image link
                                #imglink = get_imglink(soup3)



                                # Test
                                #print('Link : ' + url)
                                #print('Title : ' + title)
                                #print('UPC : ' + upc)
                                #print('Price excluding tax : ' + price)
                                #print('Price including tax : ' + pricetax)
                                #print('Number available : ' + availability)
                                #print('Product description : ' + product_description)
                                #print('Image link : ' + imglink)
                                #print('Category : ' + category)
                                #print(review_rating)
                                pages_details = f"{url},{all_data}\n'"
                                #Output CSV
                            outf.write(pages_details)

                           # else:
                                #break

