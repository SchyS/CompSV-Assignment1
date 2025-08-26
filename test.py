from product_data import products

# create a python dictionary 
d = {"name": "Geeks", "topic": "dict", "task": "iterate"}

# iterating both key and values
for value in d.items():
    print(f"{value}")

print(products.dict.values())

#How to just get tags in list, although still in a list
converted_products = []
for value in products:
    converted_products.append(value["tags"])

converted_products = set(converted_products)

# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    count = 0
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    for value in customer_tags:
        if value in product_tags:
            print(value)
            count += 1
        else:
            continue
    print(count)
    pass

count_matches(converted_products, customer_preferences)

#Example
d = {'dict1': {'foo': 1, 'bar': 2}, 'dict2': {'baz': 3, 'quux': 4}}

for k1,v1 in d.iteritems(): # the basic way
    temp = ""   
    temp+=k1
    for k2,v2 in v1.iteritems():
        temp = temp+" "+str(k2)+" "+str(v2)
    print(temp)