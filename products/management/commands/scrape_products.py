import requests
from bs4 import BeautifulSoup
from products.models import Product

base_url = "https://books.toscrape.com/catalogue/page-"

Product_Image = []
Product_name = []
Prices = []
Rating = []
Product_Description = []

for i in range(1, 13):
    url = f"{base_url}{i}.html"
    r = requests.get(url, timeout=10)
    soup = BeautifulSoup(r.text, 'lxml')

    products = soup.find_all("article", class_="product_pod")

    for product in products:
        img_tag = product.find("img", class_="thumbnail")
        if img_tag and img_tag.get("src"):
            img_url = img_tag["src"]
            img_url = f"https://books.toscrape.com/{img_url}"
            Product_Image.append(img_url)

        name = product.find("h3").find("a")["title"]
        Product_name.append(name)

        price = product.find("p", class_="price_color").text
        Prices.append(price)

        rating = product.find("p", class_="star-rating")["class"][1]
        Rating.append(rating)

        description = product.find("p", class_="instock availability").text.strip()
        Product_Description.append(description)

        product_instance = Product(
            name=name,
            price=price,
            rating=rating,
            description=description,
            image_url=img_url
        )
        product_instance.save()
        print(f"Product saved: {name}")

print("Data re-inserted successfully!")
