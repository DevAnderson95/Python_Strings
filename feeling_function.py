import math
counter = []
reviews = [
        "This product is really good. I'm impressed with its quality.\n",
        "The performance of this product is excellent. Highly recommended!\n",
        "I had a bad experience with this product. It didn't meet my expectations.\n",
        "Poor quality product. Wouldn't recommend it to anyone.\n",
        "The product was average. Nothing extraordinary about it.\n"
]

def count_up(review):
    
    return len(review)
 
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

positive_word_count = 0
negative_word_count = 0

for review in reviews:
    for positive_word in positive_words:

        if positive_word in review.lower():
            positive_word_count += 1
    
    for negative_word in negative_words:
        if negative_word in review.lower():
            negative_word_count += 1


    


print(positive_word_count)
print(negative_word_count)



    

    
        
    