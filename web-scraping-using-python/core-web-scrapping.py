import bs4, requests

def getAmazonPrice(productUrl):

    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    elems = soup.select(
        '#soldByThirdParty > span.a-size-medium.a-color-price.inlineBlock-display.offer-price.a-text-normal.price3P')

    elems[0].text

    return elems[0].text.strip()

price = getAmazonPrice('https://www.amazon.com/Jump-Start-your-software-career/dp/1977035655')
print('the price is ' + price)
