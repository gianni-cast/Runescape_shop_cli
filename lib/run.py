from models.__init__ import CONN, CURSOR
from models.item import Item
from models.shop import Shop
# import CLI

def main():
    Item.create_table()
    Shop.create_table()

if __name__ == "__main__":
    main()


# start your cli here