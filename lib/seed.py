from models.__init__ import CONN, CURSOR
from models.museum import Museum
from models.exhibit import Exhibit





def seed_database():
    Exhibit.drop_table()
    Museum.drop_table()
    Museum.create_table()
    Exhibit.create_table()

    # museum1= Museum.create("name", "address", True, "Open")

    museum1= Museum.create("History Museum", "123 Museum St", True, "9 AM - 5 PM")
    museum2= Museum.create("Art Gallery", "456 Gallery Ave", True, "10 AM - 6 PM")
    museum3= Museum.create("Science Center", "789 Science Blvd", True, "8 AM - 4 PM")
    museum4= Museum.create("Dinosaur Museum", "101 Fun Rd", True, "9 AM - 5 PM")
    museum5= Museum.create("Natural History Museum", "202 Dino Dr", True, "10 AM - 6 PM")

    # exhibit1= Exhibit.create("name", True, 1)

    exhibit1= Exhibit.create("Exhibit A", True, 1),
    exhibit2= Exhibit.create("Exhibit B", True, 2),
    exhibit3= Exhibit.create("Exhibit C", True, 3),
    exhibit4= Exhibit.create("Exhibit D", True, 4),
    exhibit5= Exhibit.create("Exhibit E", True, 5)
    
    CONN.commit()
    pass


