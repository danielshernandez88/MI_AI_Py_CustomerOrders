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
    customer_dict[customer] = {'Total Spent': total_spent, 'Classification': classification}

    #print(f"The total spend from {customer} is ${total_spent} and they are classified as a {classification}.")


""""
4. Generate business insights 
• Calculate the total revenue per product category and store it in a dictionary 
• Extract unique products from all orders using a set 
• Use a list comprehension to find all customers who purchased electronics 
• Identify the top three highest-spending customers using sorting """



"""5. Organize and display data 
• Print a summary of each customer’s total spending and their classification 
• Use set operations to find customers who purchased from multiple categories 
• Identify common customers who bought both electronics and clothing
"""
