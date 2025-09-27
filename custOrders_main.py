# Example of a tuple (ordered, immutable sequence)
customers_list = ['Jose','Maria','Carlos','Ana','Luis']

product_prices = [('Laptop', 120),   
                    ('Smartphone', 80),
                    ('Smartwatch', 20),
                    ('Dress', 8),
                    ('Jacket', 10),
                    ('Shoes', 12),
                    ('T-shirt', 4),
                    ('Coffee Maker', 15),
                    ('Blender', 10),
                    ('Vacuum Cleaner', 15),
                    ('Microwave', 20)]

customer_purchases = { 'Jose': ['Laptop', 'Smartphone', 'Jacket'],
                       'Maria': ['Coffee Maker', 'Dress', 'Shoes'],
                       'Carlos': ['Smartphone', 'Jacket', 'Blender'],
                       'Ana': ['Vacuum Cleaner', 'Microwave', 'T-shirt'],
                       'Luis': ['Blender', 'Coffee Maker', 'Smartwatch']}


"""" . Classify products by category 
• Use a dictionary to map each product to its respective category 
• Create a set of unique product categories 
• Display all available product categories """

customer_dict = {'Electronics': set(), 'Clothing': set(), 'Home Essentials': set()}

category_electronics = {'Laptop', 'Smartphone', 'Smartwatch'}
category_clothing = {'Dress', 'Jacket', 'Shoes', 'T-shirt'}
category_home_essentials = {'Coffee Maker', 'Blender', 'Vacuum Cleaner', 'Microwave'}

for category in customer_dict.keys():
    for customer, products in customer_purchases.items():
        for product in products:
            if product in category_electronics and category == 'Electronics':
                customer_dict[category].add(product)
            elif product in category_clothing and category == 'Clothing':
                customer_dict[category].add(product)
            elif product in category_home_essentials and category == 'Home Essentials':
                customer_dict[category].add(product)   



"""
3. Analyze customer orders 
• Use a loop to calculate the total amount each customer spends 
• If the total purchase value is above $100, classify the customer as a high-value buyer 
• If it is between $50 and $100, classify the customer as a moderate buyer 
• If it is below $50, classify them as a low-value buyer """

customer_dict_2 = {}

for customer, product in customer_purchases.items():
    total_spent = 0
    for item in product:
        for prod, price in product_prices:
            if item == prod:
                total_spent += price
    if total_spent > 100:
        classification = 'High-Value Buyer'
    elif 50 <= total_spent <= 100:
        classification = 'Moderate Buyer'
    else:
        classification = 'Low-Value Buyer'
    customer_dict_2[customer] = {'Total Spent': total_spent, 'Classification': classification}

    #print(f"The total spend from {customer} is ${total_spent} and they are classified as a {classification}.")


""""
4. Generate business insights 
• Calculate the total revenue per product category and store it in a dictionary 
• Extract unique products from all orders using a set 
• Use a list comprehension to find all customers who purchased electronics 
• Identify the top three highest-spending customers using sorting """

product_dict = dict(product_prices)
revenue_per_category = {'Electronics': 0, 'Clothing': 0, 'Home_Essentials': 0}
products_set = set()

for customer, products in customer_purchases.items():
    for product in products:
        if not(product in products_set):
            products_set.add(product)

product_prices

customer_purchases

for customer, products in customer_purchases.items():
    for product in products:
        if product in category_electronics:
            revenue_per_category['Electronics'] += product_dict[product]
        elif product in category_clothing:
            revenue_per_category['Clothing'] += product_dict[product]
        elif product in category_home_essentials:
            revenue_per_category['Home_Essentials'] += product_dict[product]

#[new_item_expression for variable in iterable if condition]

electronic_buyers = [customer for customer, products in customer_purchases.items() if any(product in category_electronics for product in products)]
#print(electronic_buyers)

top_spenders = sorted(customer_dict_2.items(), key=lambda x: x[1]['Total Spent'], reverse=True)[:3]
#print(top_spenders)




"""5. Organize and display data 
• Print a summary of each customer’s total spending and their classification 
• Use set operations to find customers who purchased from multiple categories 
• Identify common customers who bought both electronics and clothing
"""
# Print summary of each customer's total spending and classification
for customer, details in customer_dict_2.items():
    print(f"Customer: {customer}, Total Spent: ${details['Total Spent']}, Classification: {details['Classification']}")


# Build sets of customers per category
electronics_customers = {
    cust for cust, products in customer_purchases.items()
    if any(p in category_electronics for p in products)
}
clothing_customers = {
    cust for cust, products in customer_purchases.items()
    if any(p in category_clothing for p in products)
}
home_customers = {
    cust for cust, products in customer_purchases.items()
    if any(p in category_home_essentials for p in products)
}

# Customers who bought both electronics AND clothing (intersection)
electronics_and_clothing = electronics_customers & clothing_customers

print("Customers who purchased both electronics and clothing:", electronics_and_clothing)