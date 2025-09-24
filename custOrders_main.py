# Example of a tuple (ordered, immutable sequence)
customers_list = ['Jose','Maria','Carlos','Ana','Luis']

customer_details = [('Jose', 'Laptop', 1200, 'Electronics'),
                    ('Maria', 'Dress', 80, 'Clothing'),
                    ('Carlos', 'Smartphone', 800, 'Electronics'),
                    ('Ana', 'Vacuum Cleaner', 150, 'Home Essentials'),
                    ('Luis', 'Blender', 100, 'Home Essentials')]

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


print(customer_dict)
