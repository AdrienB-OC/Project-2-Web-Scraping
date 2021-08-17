import requests

def get_cat_links(catName, lien):


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

    return count, url_list
