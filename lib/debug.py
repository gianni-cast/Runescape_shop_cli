from models.__init__ import CONN, CURSOR
import ipdb

from models.item import Item
from models.shop import Shop


Item.create_table()

Shop.create_table()
    
ipdb.set_trace()