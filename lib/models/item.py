from . import CONN, CURSOR

class Item:
    def __init__(self, name, description, price, shop_id, id=None):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.shop_id = shop_id
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Name must be a string.')
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters.")
        self._name = value
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError('Description must be a string.')
        self._description = value
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Price must be an integer.')
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value
    
    def save(self):
        if self.id is None:
            CURSOR.execute('''
                INSERT INTO items (name, description, price, shop_id)
                VALUES (?, ?, ?, ?)
            ''', (self.name, self.description, self.price, self.shop_id))
            CONN.commit()
            self.id = CURSOR.lastrowid
    
    @classmethod
    def create(cls, name, description, price, shop_id):
        item = Item(name = name, description = description, price = price, shop_id = shop_id)
        item.save()
        return item


    @classmethod
    def all(cls):
        CURSOR.execute('SELECT * FROM items')
        rows = CURSOR.fetchall()
        print(rows)
        items = []
        for row in rows:
            print(row)
            item = cls(row[1], row[2], row[3], row[0])
            items.append(item)
        return items
    
    @classmethod
    def delete(cls, item_id):
        CURSOR.execute('DELETE FROM items WHERE id=?', (item_id,))
        CONN.commit()
    
    @classmethod
    def find_by_id(cls, item_id):
        CURSOR.execute('SELECT * FROM items WHERE id=?', (item_id,))
        row = CURSOR.fetchone()
        if row:
            item = cls(row[1], row[2], row[3], row[0])
            return item
        return None
    
    @classmethod
    def find_by_shop_id(cls, shop_id):
        CURSOR.execute('SELECT * FROM items WHERE shop_id=?', (shop_id,))
        rows = CURSOR.fetchall()
        items = []
        for row in rows:
            item = cls(row[1], row[2], row[3], row[0])
            items.append(item)
        return items

    @classmethod
    def create_table(cls):
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                price INTEGER,
                shop_id INTEGER,
                FOREIGN KEY (shop_id) REFERENCES shops (id)
            )
        ''')
        CONN.commit()
    

    def __repr__(self):
        return f"Item(id={self.id}, name='{self.name}', description='{self.description}', price={self.price})"
