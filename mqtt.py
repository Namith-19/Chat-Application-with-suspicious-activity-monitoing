import mysql.connector as conn
import pandas as pd

# Connect to MySQL
db = conn.connect(host="localhost", user="root", password="namith")
cur = db.cursor()

# Creating database and selecting it
cur.execute("CREATE DATABASE IF NOT EXISTS harshap;")
cur.execute("USE harshap;")

# Creating the table if it does not exist
cur.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id     INT AUTO_INCREMENT PRIMARY KEY,
    name          VARCHAR(255) NOT NULL,
    brand         VARCHAR(255),
    category      VARCHAR(255),
    price         DECIMAL(10,2) NOT NULL,
    currency      VARCHAR(10) DEFAULT 'INR',
    weight        DECIMAL(10,2),
    unit          VARCHAR(50),
    ingredients   TEXT,
    allergens     VARCHAR(255),
    calories      INT,
    protein       DECIMAL(10,2),
    carbohydrates DECIMAL(10,2),
    fats          DECIMAL(10,2),
    sugar         DECIMAL(10,2),
    fiber         DECIMAL(10,2),
    sodium        DECIMAL(10,2),
    availability  INT DEFAULT 0
);
""")

column = [
    "product_id", "name", "brand", "category", "price", "currency", "weight", "unit",
    "ingredients", "allergens", "calories", "protein", "carbohydrates", "fats",
    "sugar", "fiber", "sodium", "availability"
]

def inserting_single_values(values: list):
    if len(values[0]) != 18:
        return "The required column length is not satisfied."

    try:
        # Check if product_id already exists
        cur.execute("SELECT * FROM products WHERE product_id = %s", (values[0][0],))
        if cur.fetchone():
            return "Product ID already exists!"

        cur.execute(
            "INSERT INTO products VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", values[0]
        )
        db.commit()
        return "Product inserted successfully!"
    except conn.errors.IntegrityError as err:
        return str(err)

def search_with_productID(id: int):
    print(f"The ID is: {id}")

    try:
        cur.execute("SELECT * FROM products WHERE product_id = %s", (id,))
        result = pd.DataFrame(cur.fetchall(), columns=column)
        if result.empty:
            return f"There is no entry with ID {id}"
        return result
    except conn.errors.IntegrityError as err:
        return str(err)

# Testing the function
product = [(
    16, "Protein Bar - Chocolate", "Fit Snacks", "Snacks", 2.99, "USD", 60, "g", 
    "Whey Protein, Cocoa, Almonds, Honey", "Dairy, Nuts", 220, 15, 20, 8, 10, 5, 80, 23
)]

print(inserting_single_values(product))
print(search_with_productID(12))
