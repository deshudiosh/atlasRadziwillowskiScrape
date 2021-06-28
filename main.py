import requests
from bs4 import BeautifulSoup


def main():
    url = "https://plock.ap.gov.pl/index.php/2021/06/08/atlas-radziwillowski-wystawa-wirtualna/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    # print(soup.prettify())

    img_tags = soup.find_all('img')

    urls = [img['src'] for img in img_tags]

    for url in urls:
        print(url)
        s = url.split("/")[-1]
        if s.find('-') > -1:
            s = s.split("-")[-1]
            if s.find('x') > -1:
                newurl = ".".join([url[0:-(len(s)+1)], url.split('.')[-1]])
                # print(newurl)
                r = requests.get(newurl)
                filename = newurl.split("/")[-1]
                open(f'img/{filename}', 'wb').write(r.content)


if __name__ == '__main__':
    main()

