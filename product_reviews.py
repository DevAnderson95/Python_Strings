reviews = [
        "This product is really good. I'm impressed with its quality.\n",
        "The performance of this product is excellent. Highly recommended!\n",
        "I had a bad experience with this product. It didn't meet my expectations.\n",
        "Poor quality product. Wouldn't recommend it to anyone.\n",
        "The product was average. Nothing extraordinary about it.\n"
]

keys = ['good', 'bad', 'excellent', 'poor', 'average']
def product_review(reviews,keys):
        capped_words = []
        for review in reviews: 
            for key in keys:
                if key in review:
                     
                    review = review.replace(key, key.upper()) 
                    capped_words.append(review)
                elif key.capitalize() in review:
                    review = review.replace(key.capitalize(), key.upper()) 
                    capped_words.append(review)
                     
        return capped_words

         
new_review = product_review(reviews, keys)


for review in new_review:
    print(review)

        
        
    
    
    

    


        
