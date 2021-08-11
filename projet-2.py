import requests
from bs4 import BeautifulSoup
from get_data import get_all_data

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

                                # Get all data
                                all_data = get_all_data(soup3)

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

