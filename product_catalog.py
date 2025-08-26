from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.
print(products)


# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.

#Create a list to store the customers preferences
customer_preferences = []
response = ""

#Loop to ask user to input preferences until they signify they are done
while response != "N":
    preference = input("Input a preference: ").lower()
    # Add the customer preference to the list
    customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()
print(customer_preferences)
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_preferences = set(customer_preferences)
print(customer_preferences)


# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []
for value in products:
    tags = {
        "name" : value["name"],
        "tags" : set(value["tags"])
    }
    converted_products.append(tags)

print(converted_products)


# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(product_tags.intersection(customer_tags))

# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    #Create a list to store the results
    result = []
    #For each product, if there is a match, append it to the results
    for product in products:
        #Calls count_matches function
        matches = count_matches(product["tags"], customer_tags)
        if matches > 0:  # Only include products with at least 1 match
            result.append((product["name"], matches))
    
    #Sorts the result from most matches to least
    result.sort(key=lambda x: x[1], reverse=True)
    return result



# TODO: Step 7 - Call your function and print the results
recommendations = recommend_products(converted_products, customer_preferences)
print("Recommended Products: ")
for name, matches in recommendations:
    print(f"{name} ({matches} match(es))")


# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
"""
In our assignment I have used several core opperations. First, I had used a 
while loop so that the user can input as many preferences as they would like. 
This would continue to ask until they state they are done. Next, using "set" I
converted different lists into sets in order to have quicker comparisons. I 
also used for loops in order to go through all products or tags so we would be
able to find and return matches. I used an if statement to only include products
who had at least one match. Finally, I used intersections to get all matching 
values between the product tags and customer tags. 

"""
# 2. How might this code change if you had 1000+ products?
"""
This code would change if we had 1000+ products. I believe instead of looking through and checking
each and every product for a match we could first, just look at what the customers want and start there.
We would look up the customer tag to get the list of products instead of going through the list of products 
to look for each tag. This would allow us to save more time and processing power. 
"""