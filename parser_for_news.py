from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('https://www.mk.ru/social/')

html = req.read()

soup = BeautifulSoup(html, 'html.parser')
news = soup.find_all("li", class_="article-listing__item")
results = []

for item in news:
    title = item.find('h3', class_='listing-preview__title').get_text(strip=True)
    desc = item.find('p', class_='listing-preview__desc').get_text(strip=True)
    href = item.a.get('href')

    results.append({
        'title': title,
        'desc': desc,
        'href': href
    })

f = open('news.txt', 'w', encoding='utf-8')
i = 1
for item in results:
    f.write(f'Новость № {i}\n\nНазвание: {item["title"]}\nОписание: {item["desc"]}\nСсылка: {item["href"]}\n**********\n\n')
    i += 1
f.close()