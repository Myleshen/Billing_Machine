def products(no_of_products):
    quantity_of_products = []
    for index_products in range(0, no_of_products):
        print("Product", index_products + 1, " Quantity = ")
        quantity_of_products.append(int(input()))
    return quantity_of_products


def price_products(no_of_products):
    price_of_products = []
    for index_price in range(0, no_of_products):
        print("Price Of Product", index_price + 1)
        price_of_prod = int(input())
        price_of_products.append(price_of_prod)
    return price_of_products


def amount_of_products(price, quantity, no_of_products):
    prod_amount_list = []
    for index_amount in range(0, no_of_products):
        price_of_per_product = price[index_amount] * quantity[index_amount]
        prod_amount_list.append(price_of_per_product)
    return prod_amount_list


print("Enter The Purchaser's Details : ")
print("Name : ", end="")
name = input()
print("Unique Code : ", end="")
uniqe_id = int(input())
print("Previous Balance : ", end="")
prev_bal = int(input())
if prev_bal < 0:
    prev_bal = abs(prev_bal)
print("Today's Purchases's : ")
print("No Of Products : ")
no_of_prod = int(input())
print("Price of Products : ")
price_of_products_list = price_products(no_of_products=no_of_prod)
quantity_of_products_list = products(no_of_products=no_of_prod)
amount_list = amount_of_products(price=price_of_products_list, quantity=quantity_of_products_list,
                                            no_of_products=no_of_prod)
total_sum = 0
for index in range(0, no_of_prod):
    total_sum = total_sum + amount_list[index]
if total_sum > prev_bal:
    print("Balance Is Low Cannot Purchase...Retry!..\nBalance =", prev_bal)
else:
    print("*************Final Bill*************\n")
    for index in range(0, no_of_prod):
        print("Product", index+1, " *", quantity_of_products_list[index], " = ",amount_list[index])
    print("\t\tTotal Amount = ", total_sum)
    print("\t\tCurrent Balance = ",prev_bal-total_sum)

