# Import the datatime module so that
# it can be used in this program.
from datetime import datetime

def main():
    products = read_products()

    #for i in products:
    #    print(f"{i}: {products[i]}")

    print("Inkom Emporium\n")
    process_request(products)
    print("\nThank you for shopping at the Inkom Emporium.")
    date()

def read_products():

    product_dict = {}

    try:
        with open("products.csv", "rt") as products:

            next(products)

            for product in products:
                product_info = product.strip().split(",")
                product_dict[product_info[0]] = product_info[1], product_info[2]

        return product_dict
    except PermissionError as perm_err:
        print()
        print(f"You don't have permission to read products.csv.")
        print("Run the program again and enter the name of a file that you are allowed to read.")
    except FileNotFoundError as file_not_found_err:
        print()
        print(f"The file products.csv doesn't exist.")
        print("Run the program again and enter the name of an existing file.")
    except KeyError as key_err:
        print()
        print("The entered key does not exist in the products.csv.")
        print("Please enter a valid key.")


def process_request(dictionary):
    
    with open("request.csv", "rt") as requests:

        next(requests)
        count = 0
        total = 0

        for request in requests:
            request_info = request.strip().split(",")
            if request_info[0] in dictionary.keys():
                item_info = dictionary.get(request_info[0])
                name = item_info[0]
                price = item_info[1]
                quantity = request_info[1]
                print(f"{name}: {quantity} @ {price}")

                count += int(quantity)
                total += round(float(price) * float(quantity), 2)
        
        tax = total*.06
        final = total + total * .06

        print(f"\nNumber of Items: {count}")
        print(f"Subtotal: {total}")
        print(f"Sales Tax: {tax:.2f}")
        print(f"Total: {final:.2f}")

def date():
    current_date_and_time = datetime.now()

    print(f"{current_date_and_time:%c}")


main()