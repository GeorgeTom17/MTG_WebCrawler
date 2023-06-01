import csv
import numpy as np
from urllib.request import urlopen

temp = []
with open('jrnintonyx.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for i in reader:
        temp.append(i)

tab = np.asarray(temp, dtype=int)

finaldata = []
for z in range(1, 16):
    url = "https://www.cardmarket.com/en/Magic/Products/Singles/Journey-into-Nyx"
    site = "?site=" + str(z)
    url += site
    page = urlopen(url)
    html = page.read().decode("utf-8")
    for i in tab:
        to_find = "<div class=\"col-md-2 d-none d-lg-flex has-content-centered\">" + str(i[0]) + "</div>"
        index = html.find(to_find)
        if index != -1:
            link_start = 0
            link_end = 0
            found = False
            for j in range(0, 150):
                if not found and link_end == 0:
                    if html[index - j] == "\"":
                        link_end = index - j
                        continue
                if not found and link_end != 0:
                    if html[index - j] == "\"":
                        link_start = index - j
                        found = True
                if found:
                    break
            card_link = "https://www.cardmarket.com" + html[link_start:link_end]
            card_page = urlopen(card_link.replace('\"', ''))
            card_html = card_page.read().decode("utf-8")
            header = card_html.find("<h1>")
            name_end = 0
            name_found = False
            for k in range(4, 50):
                if card_html[header + k] == "<":
                    name_end = header + k
            final_card_name = str(card_html[(header + 4):name_end])
            if i[2] == 0:
                price_index = card_html.find("30-days average price")
                price_start = price_index + len("30-days average price") + 38
                price_end = price_start + 7
                raw_price = card_html[price_start:price_end]
                final_price = raw_price.replace('<', '')
                final_price = final_price.replace('/', '')
                final_price = final_price.replace('s', '')
                print(final_card_name + " " + final_price)

            else:
                card_link_foil = "https://www.cardmarket.com" + html[link_start:link_end] + "?isFoil=Y"
                card_page_foil = urlopen(card_link_foil.replace('\"', ''))
                card_html_foil = card_page_foil.read().decode("utf-8")
                price_index = card_html_foil.find("30-days average price")
                price_start = price_index + len("30-days average price") + 38
                price_end = price_start + 9
                raw_price = card_html_foil[price_start:price_end]
                final_price = raw_price.replace('<', '')
                final_price = final_price.replace('/', '')
                final_price = final_price.replace('s', '')
                print(final_card_name + " " + final_price)
            final_price = float(final_price[0:-2].replace(',', '.'))
            card_all_info = [final_card_name, i[1], i[2], final_price, i[1] * final_price]
            finaldata.append(card_all_info)
np.array(finaldata)
total_suma = 0
for i in finaldata:
    print(i)
    total_suma += i[4]
print(total_suma)