from . import CONN, CURSOR

class Shop:
    def __init__(self, name, location, owner, id=None):
        self.id = id
        self.name = name
        self.location = location
        self.owner = owner
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters.")
        self._name = value
    
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, value):
        if not isinstance(value, str):
            raise TypeError("Location must be a string.")
        self._location = value

    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, value):
        if not isinstance(value, str):
            raise TypeError("Owner must be a string")
        self._owner = value
    
    @property
    def full_location(self):
        return f"{self.name} located in {self.location}"

    def save(self):
        if self.id is None:
            CURSOR.execute('''
                INSERT INTO shops (name, location, owner)
                VALUES (?, ?, ?)
            ''', (self.name, self.location, self.owner))
            CONN.commit()
            self.id = CURSOR.lastrowid
    
    @classmethod
    def create(cls, name, location, owner):
        shop = Shop(name = name, location = location, owner = owner)
        shop.save()
        return shop

    @classmethod
    def all(cls):
        CURSOR.execute('SELECT * FROM shops')
        rows = CURSOR.fetchall()
        shops = []
        for row in rows:
            shop = cls(row[1], row[2], row[3], row[0])
            shops.append(shop)
        return shops
    
    @classmethod
    def delete(cls, shop_id):
        CURSOR.execute('DELETE FROM shops WHERE id=?', (shop_id,))
        CONN.commit()

    @classmethod
    def find_by_id(cls, shop_id):
        CURSOR.execute('SELECT * FROM shops WHERE id=?', (shop_id,))
        row = CURSOR.fetchone()
        if row:
            shop = cls(row[1], row[2], row[3], row[0])
            return shop
        return None
    
    @classmethod
    def create_table(cls): 
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS shops (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                location TEXT,
                owner TEXT
            )
        ''')

        CONN.commit()
    
    def __repr__(self):
        return f"Shop(id={self.id}, name='{self.name}', location='{self.location}', owner='{self.owner}')"