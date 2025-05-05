from gettext import install

import pip


class InventoryItem:
    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        assert isinstance(category, object)
        self.category = category


# List to store inventory items
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def update_quantity(self, item_name, new_quantity):
        for item in self.items:
            if item.name == item_name:
                item.quantity = new_quantity
                break

    def generate_report(self):
        # generate inventory reports
        pass


# Create inventory items
item1 = InventoryItem(name="led bulbs", price=100.99, quantity=100, category="Electronics")
item2 = InventoryItem(name="rice", price=200.99, quantity=50, category="cereals")

# Initialize the inventory
my_inventory = Inventory()
my_inventory.add_item(item1)
my_inventory.add_item(item2)

pip
install()
mysql - connector - python
import mysql.connector

class InventoryDatabase:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

        # Create the inventory table (if not exists)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS inventory (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                price DECIMAL(10, 2),
                quantity INT,
                category VARCHAR(255)
            )
        """)
        self.conn.commit()

    def insert_item(self, item):
        self.cursor.execute("""
            INSERT INTO inventory (name, price, quantity, category)
            VALUES (%s, %s, %s, %s)
        """, (item.name, item.price, item.quantity, item.category))
        self.conn.commit()

    def close(self):
        self.conn.close()

# Initialize the database (replace with your MySQL credentials)
inventory_db = InventoryDatabase(
    host="localhost",
    user="prime",
    password="Underscore12",
    database="inventory_db"
)
class InventoryDatabase:
    def __init__(self, config):
        self.conn = mysql.connector.connect(**config)
        self.cursor = self.conn.cursor()

    def insert_item(self, item):
        query = """
            INSERT INTO Items (item_name, price, quantity)
            VALUES (%s, %s, %s)
        """
        values = (item.name, item.price, item.quantity)
        self.cursor.execute(query, values)
        self.conn.commit()

    # Implement other methods (e.g., update_item, get_items, etc.)

    def close(self):
        self.conn.close()

# Insert sample items into the database
inventory_db.insert_item(item1)
inventory_db.insert_item(item2)

# Close the database connection
inventory_db.close()
