def output_csv(catName, book_list):

    with open(str(catName) + '.csv', 'w', encoding="utf-8") as outf:
        outf.write('url, title, upc, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url \n')
        for book in book_list:
            pages_details = f"{book.url},{book.fstring}\n"
            outf.write(pages_details)
