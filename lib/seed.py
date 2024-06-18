from models.__init__ import CONN, CURSOR
from models.museum import Museum
from models.exhibit import Exhibit





def seed_database():

    print("Dropping tables")
    Exhibit.drop_table()
    Museum.drop_table()
    print("Creating tables")
    Museum.create_table()
    Exhibit.create_table()

    # museum1= Museum.create("name", "address", True, "Open")

    print("Creating Museum instances")
    museums=[
        Museum.create("History Museum", "123 Museum St", True, "9 AM - 5 PM"),
        Museum.create("Art Gallery", "456 Gallery Ave", True, "10 AM - 6 PM"),
        Museum.create("Science Center", "789 Science Blvd", True, "8 AM - 4 PM"),
        Museum.create("Dinosaur Museum", "101 Fun Rd", True, "9 AM - 5 PM"),
        Museum.create("Natural History Museum", "202 Dino Dr", True, "10 AM - 6 PM"),]

    # exhibit1= Exhibit.create("name", True, 1)

    print("Creating exhibit instances")
    exhibits=[
        Exhibit.create("History Exhibit", True, museums[0].id),
        Exhibit.create("Roman Exhibit", True, museums[0].id),
        Exhibit.create("Egyptian Exhibit", True, museums[0].id),
        Exhibit.create("Mona Lisa Exhibit", True, museums[1].id),
        Exhibit.create("Space Exhibit", True, museums[2].id),
        Exhibit.create("Dinosaur Bone Exhibit", True, museums[3].id),
        Exhibit.create("Mammal Exhibit", True, museums[4].id),]
    
    CONN.commit()
    pass

seed_database()

