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
    if product_description.isspace():
        product_description = "No description"
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

    all_data = f"{title},{attributes},{product_description},{category},{review_rating},{imglink}"
    return all_data
