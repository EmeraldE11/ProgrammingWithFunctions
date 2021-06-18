from random import uniform

def append_random_numbers(numbers_list, quantity = 1):
    
    for _ in range(quantity):
        rand_num = uniform(1, 99)
        rand_num = round(rand_num, 1)
        numbers_list.append(rand_num)

def main():
    randnums = [16.2, 75.1, 52.3]
    print(randnums)
    append_random_numbers(randnums)
    print(randnums)
    append_random_numbers(randnums, 3)
    print(randnums)


main()