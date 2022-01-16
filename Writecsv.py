import csv

# csv header
fieldnames = ['id', 'product_name', 'customer_average_rating']

# csv data
rows = [
    {'id': 132,
     'product_name': 'Massoub gift card',
     'customer_average_rating': 5.0},
    {'id': 154,
     'product_name': 'Kebdah gift card',
     'customer_average_rating': 3.2},
    {'id': 12,
     'product_name': 'Fatayer gift card',
     'customer_average_rating': 1.8}
]

with open('products.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)