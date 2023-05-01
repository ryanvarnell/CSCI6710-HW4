import sqlite3
import random

# Connect to the database
conn = sqlite3.connect('styles.db')

# Define available sizes
sizes = ['XS', 'S', 'M', 'L', 'XL']

# Predefined colors for each item
colors = {
    "dress1": "Black",
    "dress2": "Green",
    "dress3": "Black",
    "dress4": "Pink",
    "mpant1": "Black",
    "mpant2": "Navy",
    "mpant3": "Tan",
    "mpant4": "Blue",
    "mpant5": "Blue",
    "mshirt1": "Black",
    "mshirt2": "Green",
    "mshirt3": "White",
    "mshirt4": "Brown",
    "mshirt5": "Blue",
    "wpant1": "White",
    "wpant2": "Black",
    "wpant3": "Blue",
    "wshirt1": "Blue",
    "wshirt2": "Pink",
    "wshirt3": "Yellow",
}

# Read and insert the images
for i in range(1, 5):
    # Set the file path and open the file as binary
    file_path = f"C:/Users/cris/Documents/ECU Classes/CSCI 6710 Developing E-Commerce Systems/HW4/clothing photos/dress{i}.png"
    with open(file_path, 'rb') as file:
        blob_data = file.read()

    # Generate random price and size
    price = round(random.uniform(20, 100), 2)
    size = random.choice(sizes)
    color = colors[f"dress{i}"]

    # Insert the data into the database
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clothing (name, type, price, size, color, image) VALUES (?, ?, ?, ?, ?, ?)", (f"Dress {i}", "top", price, size, color, blob_data))
    conn.commit()

for i in range(1, 6):
    # Set the file path and open the file as binary
    file_path = f"C:/Users/cris/Documents/ECU Classes/CSCI 6710 Developing E-Commerce Systems/HW4/clothing photos/mpant{i}.png"
    with open(file_path, 'rb') as file:
        blob_data = file.read()

    # Generate random price and size
    price = round(random.uniform(20, 100), 2)
    size = random.choice(sizes)
    color = colors[f"mpant{i}"]

    # Insert the data into the database
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clothing (name, type, price, size, color, image) VALUES (?, ?, ?, ?, ?, ?)", (f"Men's Pants {i}", "bottom", price, size, color, blob_data))
    conn.commit()

for i in range(1, 6):
    # Set the file path and open the file as binary
    file_path = f"C:/Users/cris/Documents/ECU Classes/CSCI 6710 Developing E-Commerce Systems/HW4/clothing photos/mshirt{i}.png"
    with open(file_path, 'rb') as file:
        blob_data = file.read()

    # Generate random price and size
    price = round(random.uniform(20, 100), 2)
    size = random.choice(sizes)
    color = colors[f"mshirt{i}"]

    # Insert the data into the database
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clothing (name, type, price, size, color, image) VALUES (?, ?, ?, ?, ?, ?)", (f"Men's Shirt {i}", "top", price, size, color, blob_data))
    conn.commit()

for i in range(1, 4):
    # Set the file path and open the file as binary
    file_path = f"C:/Users/cris/Documents/ECU Classes/CSCI 6710 Developing E-Commerce Systems/HW4/clothing photos/wpant{i}.png"
    with open(file_path, 'rb') as file:
        blob_data = file.read()

    # Generate random price and size
    price = round(random.uniform(20, 100), 2)
    size = random.choice(sizes)
    color = colors[f"wpant{i}"]

    # Insert the data into the database
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clothing (name, type, price, size, color, image) VALUES (?, ?, ?, ?, ?, ?)", (f"Women's Pants {i}", "bottom", price, size, color, blob_data))
    conn.commit()

for i in range(1, 4):
    # Set the file path and open the file as binary
    file_path = f"C:/Users/cris/Documents/ECU Classes/CSCI 6710 Developing E-Commerce Systems/HW4/clothing photos/wshirt{i}.png"
    with open(file_path, 'rb') as file:
        blob_data = file.read()

    # Generate random price and size
    price = round(random.uniform(20, 100), 2)
    size = random.choice(sizes)
    color = colors[f"wshirt{i}"]

    # Insert the data into the database
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clothing (name, type, price, size, color, image) VALUES (?, ?, ?, ?, ?, ?)", (f"Women's Shirt {i}", "top", price, size, color, blob_data))
    conn.commit()

# Close the connection
conn.close()

