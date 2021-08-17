import requests
from bs4 import BeautifulSoup
from get_data import get_all_data
from download_image import download_img

home = 'http://books.toscrape.com/index.html'
response = requests.get(home)
soup = BeautifulSoup(response.content, 'html.parser')


catLink = soup.find('div', {'class': 'side_categories'})

for li in catLink.find_all('li'):

    b = li.find('a')
    lien = b['href']
    catName = b.text.strip()
    lien = 'http://books.toscrape.com/' + lien

    if catName == 'Books':
        pass

    else:
        count = 0
        url_list = []

        for i in range(1, 10):

            if i == 1:
                print(catName)
                print(lien)
                url_list.append(lien)
                count += 1

            elif i == 2 and (requests.get(lien.replace('index.html', 'page-' + str(i) + '.html')).ok):
                url_list.append(lien.replace('index.html', 'page-' + str(i) + '.html'))
                count += 1

            elif i > 2 and (requests.get(lien.replace('index.html', 'page-' + str(i) + '.html')).ok):
                url_list.append(lien.replace('index.html', 'page-' + str(i) + '.html'))
                count += 1

            else:
                break




        with open(str(catName) + '.csv', 'w', encoding="utf-8") as outf:
            outf.write('url, title, upc, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url \n')

            for j in range(0, count):
                page = url_list[j]

                # page = 'http://books.toscrape.com/catalogue/category/books/mystery_3/page-' + str(i) + '.html'
                response = requests.get(page)

                if response.ok:
                    soup2 = BeautifulSoup(response.content, 'html.parser')

                    # Find all book links on that page
                    liens = soup2.find_all('h3')

                    pages_details = ""

                    for k in liens:
                        a = k.find('a')
                        url = a['href']
                        url = url.replace('../../../', 'http://books.toscrape.com/catalogue/')

                        response2 = requests.get(url)

                        if response2.ok:
                            soup3 = BeautifulSoup(response2.content, 'html.parser')
                            # Get all data
                            all_data = get_all_data(soup3)
                            # Download image
                            download_img(soup3)

                            pages_details = f"{url},{all_data}\n"
                            outf.write(pages_details)

                        page = ""
