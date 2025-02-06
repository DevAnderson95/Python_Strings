reviews = [
        "This product is really good. I'm impressed with its quality.\n",
        "The performance of this product is excellent. Highly recommended!\n",
        "I had a bad experience with this product. It didn't meet my expectations.\n",
        "Poor quality product. Wouldn't recommend it to anyone.\n",
        "The product was average. Nothing extraordinary about it.\n"
]


def review_summary(review):
    space_index = review[:30].rfind(" ")
    print(review[:space_index] + "...")

for review in reviews:
    review_summary(review)