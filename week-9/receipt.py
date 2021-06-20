def main():
    products = read_products()

    for i in products:
        print(f"{i}: {products[i]}")

    process_request(products)

def read_products():

    product_dict = {}

    with open("products.csv", "rt") as products:

        next(products)
        
        for product in products:
            product_info = product.strip().split(",")
            product_dict[product_info[0]] = product_info[1], product_info[2]
            
    return product_dict

def process_request(dictionary):
    
    with open("request.csv", "rt") as requests:

        next(requests)

        for request in requests:
            request_info = request.strip().split(",")
            if request_info[0] in dictionary.keys():
                item_info = dictionary.get(request_info[0])
                name = item_info[0]
                price = item_info[1]
                quantity = request_info[1]
                print(f"{name}: {quantity} @ {price}")



main()