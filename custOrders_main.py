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


print("Lista de Clientes y sus compras:")
for details in customer_details:
    print(details)
