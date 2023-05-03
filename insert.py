import random
import sqlite3

# A placeholder script to initialize and populate the styles and user databases for testing purposes.

# Connect to the database.
conn = sqlite3.connect('styles.db')
cursor = conn.cursor()

# Create the clothing table.
cursor.execute("""
CREATE TABLE IF NOT EXISTS clothing (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    price REAL NOT NULL,
    size TEXT NOT NULL,
    color TEXT NOT NULL,
    image BLOB
)
""")

# Define available sizes.
sizes = ['XS', 'S', 'M', 'L', 'XL']

# Predefined colors for each item.
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

# Read and insert the images.
# For dresses
for i in range(1, 5):
    # Set the file path and open the file as binary.
    file_path = f"static/img/clothing photos/dress{i}.png"
    with open(file_path, 'rb') as f:
        image_data = f.read()
    
    # Generate random price and size.
    price = round(random.uniform(20, 100), 2)
    size = random.choice(sizes)
    color = colors[f"dress{i}"]

    # Insert the data into the database.
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clothing (name, type, price, size, color, image) "
                   "VALUES (?, ?, ?, ?, ?, ?)", (f"Dress {i}", "top", price, size, color, image_data))
    conn.commit()

# For men's pants.
for i in range(1, 6):
    # Set the file path and open the file as binary.
    file_path = f"static/img/clothing photos/mpant{i}.png"
    with open(file_path, 'rb') as f:
        image_data = f.read()
    
    # Generate random price and size.
    price = round(random.uniform(20, 100), 2)
    size = random.choice(sizes)
    color = colors[f"mpant{i}"]

    # Insert the data into the database.
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clothing (name, type, price, size, color, image) "
                   "VALUES (?, ?, ?, ?, ?, ?)", (f"Men's Pants {i}", "bottom", price, size, color, image_data))
    conn.commit()

# For men's shirts.
for i in range(1, 6):
    # Set the file path and open the file as binary.
    file_path = f"static/img/clothing photos/mshirt{i}.png"
    with open(file_path, 'rb') as f:
        image_data = f.read()
    
    # Generate random price and size.
    price = round(random.uniform(20, 100), 2)
    size = random.choice(sizes)
    color = colors[f"mshirt{i}"]

    # Insert the data into the database.
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clothing (name, type, price, size, color, image) "
                   "VALUES (?, ?, ?, ?, ?, ?)", (f"Men's Shirt {i}", "top", price, size, color, image_data))
    conn.commit()

# For women's pants.
for i in range(1, 4):
    # Set the file path and open the file as binary.
    file_path = f"static/img/clothing photos/wpant{i}.png"
    with open(file_path, 'rb') as f:
        image_data = f.read()
    
    # Generate random price and size.
    price = round(random.uniform(20, 100), 2)
    size = random.choice(sizes)
    color = colors[f"wpant{i}"]

    # Insert the data into the database.
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clothing (name, type, price, size, color, image) "
                   "VALUES (?, ?, ?, ?, ?, ?)", (f"Women's Pants {i}", "bottom", price, size, color, image_data))
    conn.commit()

# For women's shirts.
for i in range(1, 4):
    # Set the file path and open the file as binary.
    file_path = f"static/img/clothing photos/wshirt{i}.png"
    with open(file_path, 'rb') as f:
        image_data = f.read()
    
    # Generate random price and size.
    price = round(random.uniform(20, 100), 2)
    size = random.choice(sizes)
    color = colors[f"wshirt{i}"]

    # Insert the data into the database.
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clothing (name, type, price, size, color, image) "
                   "VALUES (?, ?, ?, ?, ?, ?)", (f"Women's Shirt {i}", "top", price, size, color, image_data))
    conn.commit()

# Close the connection.
conn.close()

# USERS DATABASE.

# Connect to the database.
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create the clothing table.
cursor.execute("""
CREATE TABLE IF NOT EXISTS "users" (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
""")
