import requests
import pathlib
import os
from get_data import get_imglink

def download_img(soup):


    folder = pathlib.Path(__file__).parent.resolve()
    path = str(folder) + '/Images'
    try:
        os.mkdir(path)
    except OSError:
        pass


    title = soup.find('h1').text
    title = title.replace(":", " ")
    url = get_imglink(soup)
    r = requests.get(url)

    with open(str(path) + '/' + title + '.jpg', 'wb') as f:
        f.write(r.content)