from models.museum import Museum
from models.exhibit import Exhibit

def exit_program():
    print("Thank you for visiting the Musuem Network, Have a great day!")
    exit()

####################################################################
#museum menu
def museum_menu():
    
    print("""
          
          |-------------------------------------------|
          |***************|Museum Menu|***************|
          |-------------------------------------------|
    
          """)
    print("*********** Museum Menu ***********")
    print("0. Exit Program")
    print("1. View List of All Museums")
    print("2. View Specific Museum")
    print("3. Create/ Add Museum")
    print("4. Update Museum")
    print("5. Delete Museum")
    print("*********************************")

    museum_menu_choice= input("Enter command here: ")
    if museum_menu_choice == "0":
        exit_program()
    if museum_menu_choice == "1":
        list_of_all_museums()
    if museum_menu_choice == "2":
        view_museum()
    if museum_menu_choice == "3":
        add_museum()
    if museum_menu_choice == "4":
        update_museum()
    if museum_menu_choice == "5":
        delete_museum()


####################################################################
#Museum_menu/ View List of All Museums 
def list_of_all_museums():
    print("""
          
          |-------------------------------------------|
          |***********|List of All Museum|************|
          |-------------------------------------------|
    
          """)
    museums_list = Museum.get_all()
    for museum in museums_list:
        print(f"|Museum ID: {museum.id}|Museum name: {museum.name} |address: {museum.address} |Open: {museum.status}|Open hours:{museum.open_hours}|")
    print("*********** List of Museums ***********")
    print("0. Exit Program")
    print("-. to go back")
    print("*To view more details about a museum, please input the Museum ID*")
    print("*********************************")

    museum_id = input("Select museum: ")
    museum = Museum.find_museum_by_id(museum_id)
    if museum:
        view_museum()
    elif museum_id == "0":
        exit_program()
    elif museum_id == "-":
        museum_menu()
    else:
        print("Invalid choice")

####################################################################
#Museum_menu/ View Specific Museum   
def view_museum():
    museum_id = input("Enter museum ID to view: ")
    museum = Museum.find_museum_by_id(museum_id)
    if museum:
        print(f"""
          
          |-------------------------------------------|
          |*****|Selected Museum: {museum.name}|******|
          |-------------------------------------------|
    
          """)
        print("************** Selected Museum *******************")
        print(f"|Museum ID: {museum.id}|Museum name: {museum.name} |address: {museum.address} |Open: {museum.status}|Open hours:{museum.open_hours}|")
        print("*********************************")
        museum_menu()
    else:
        print("museum not found.")

####################################################################
#Museum_menu/ Add/Create Museum  
def add_museum():
    name = input("Enter museum name: ")
    address = input("Enter museum address: ")
    status = input("What is the status of museum? (1 for Open, 0 for Closed): ")
    open_hours = input ("Enter museum open hours(Ex. 9 AM - 5 PM): ")
    museum = Museum.create(name, address, bool(int(status)), open_hours)
    print(f"""
          
          |-------------------------------------------|
          |*******|Added Museum: {museum.name}|*******|
          |-------------------------------------------|
    
          """)
    print("************** Added Museum *******************")
    print(f"Added museum: |Museum ID: {museum.id}|Museum name: {museum.name} |address: {museum.address} |Open: {museum.status}|Open hours:{museum.open_hours}")
    print("*********************************")
    list_of_all_museums()

####################################################################
# Museum_menu/ Update Museum 
def update_museum():
    museum_id = input("Enter museum ID to update: ")
    museum = Museum.find_museum_by_id(museum_id)
    if museum:
        museum.name = input(f"Enter new name ({museum.name}): ") or museum.name
        museum.address = input(f"Enter new address ({museum.address}): ") or museum.address
        museum.status = bool(int(input(f"Is the museum Open or Closed? (1 for Yes, 0 for No, current status==>{museum.status}): ") or museum.status))
        museum.open_hours= input(f"Enter new Open Hours ({museum.open_hours}): ")
        museum.save()
        museum.update()
        print(f"""
          
          |-------------------------------------------|
          |******|Updated Museum: {museum.name}|******|
          |-------------------------------------------|
    
          """)
        print("************** Updated Museum *******************")
        print(f"Updated museum:|Museum ID: {museum.id}|Museum name: {museum.name} |address: {museum.address} |Open: {museum.status}|Open hours:{museum.open_hours}")
        print("*********************************")
        list_of_all_museums()
    else:
        print("museum not found.")


####################################################################
#Museum_menu/ Delete Museum 
def delete_museum():
    museum_id = input("Enter museum ID to delete: ")
    museum = Museum.find_museum_by_id(museum_id)
    if museum:
        museum.delete()
        print(f"""
          
          |-------------------------------------------|
          |******|Deleted Museum: {museum.name}|******|
          |-------------------------------------------|
    
          """)
        print("************** Deleted Museum *******************")
        print(f"Deleted museum:|Museum name: {museum.name} |address: {museum.address} |Open: {museum.status}|Open hours:{museum.open_hours}")
        print("*********************************")
        list_of_all_museums()
    else:
        print("museum not found.")

####################################################################
#Exhibit menu
def exhibit_menu():
    
    print("""
          
          |-------------------------------------------|
          |***************|Exhibit Menu|**************|
          |-------------------------------------------|
    
          """)
    print("************** Exhibit Menu *******************")
    print("0. Exit Program")
    print("1. View List of All Exhibits")
    print("2. View Specific Exhibit")
    print("3. Create/ Add Exhibit")
    print("4. Update Exhibit")
    print("5. Delete Exhibit")
    print("*********************************")
    exhibit_menu_choice= input("Enter command here: ")
    if exhibit_menu_choice == "0":
        exit_program()
    if exhibit_menu_choice == "1":
        list_of_all_exhibits()
    if exhibit_menu_choice == "2":
        view_exhibit()
    if exhibit_menu_choice == "3":
        add_exhibit()
    if exhibit_menu_choice == "4":
        update_exhibit()
    if exhibit_menu_choice == "5":
        delete_exhibit()
####################################################################
#Exhibit_menu/ View List of All Exhibits  
def list_of_all_exhibits():
    print("""
          
          |-------------------------------------------|
          |**********|List of All Exhibits|***********|
          |-------------------------------------------|

          """)
    exhibit_list = Exhibit.get_all()
    for exhibit in exhibit_list:
        print(f"|Exhibit name: {exhibit.name} |status: {exhibit.status} |Exhibit located: {exhibit.museum_id}|")
    print("************** List of Exhibits *******************")
    print("0. Exit Program")
    print("-. to go back")
    print("*********************************")
    exhibit_list_choice = input("Enter Command Here: ")
    if exhibit_list_choice == "0":
        exit_program()
    elif exhibit_list_choice == "-":
        exhibit_menu()
    else:
        print("Invalid choice")

####################################################################
#Exhibit_menu/ View Specific Exhibit  
def view_exhibit():
    exhibit_id = input("Enter exhibit ID to view: ")
    exhibit = Exhibit.find_exhibit_by_id(exhibit_id)
    if exhibit:
        print(f"""
          
          |-------------------------------------------|
          |****|Selected exhibit: {exhibit.name}|*****|
          |-------------------------------------------|
    
          """)
        print("************** Selected Exhibit *******************")
        print(f"|Exhibit name: {exhibit.name} |status: {exhibit.status} |Museum located: {exhibit.museum_id}|")
        print("*********************************")
        exhibit_menu()
    else:
        print("exhibit not found.")

####################################################################
#Exhibit_menu/ Add/Create Exhibit  
def add_exhibit():
    name = input("Enter exhibit name: ")
    status = input("What is the status of exhibit? (1 for Open, 0 for Closed): ")
    museum_id = input ("Enter museum Id, the exhibit is located: ")
    exhibit = Exhibit.create(name, bool(int(status)), museum_id)
    print(f"""
          
          |-------------------------------------------|
          |******|Added Exhibit: {exhibit.name}|******|
          |-------------------------------------------|
    
          """)
    print("************** Added Exhibit *******************")
    print(f"Added museum:|Exhibit name: {exhibit.name}|Open: {exhibit.status}|Museum Located: {exhibit.museum_id}")
    print("*********************************")
    list_of_all_exhibits()


####################################################################
#Exhibit_menu/ Update Exhibit 
def update_exhibit():
    exhibit_id = input("Enter exhibit ID to update: ")
    exhibit = Exhibit.find_exhibit_by_id(exhibit_id)
    if exhibit:
        exhibit.name = input(f"Enter new name ({exhibit.name}): ") or exhibit.name
        exhibit.status = bool(int(input(f"Is the exhibit Open or Closed? (1 for Yes, 0 for No, current status==>{exhibit.status}): ") or exhibit.status))
        exhibit.museum_id= input(f"Enter new museum location ({exhibit.museum_id}): ") or exhibit.museum_id
        exhibit.save()
        exhibit.update()
        print(f"""
          
          |-------------------------------------------|
          |*******|Added Exhibit: {exhibit.name}|*****|
          |-------------------------------------------|
    
          """)
        print("************** Update Exhibit *******************")
        print(f"Updated exhibit:|Exhibit Id: {exhibit.id} |Exhibit name: {exhibit.name}|Open: {exhibit.status}|Museum Located: {exhibit.museum_id}")
        print("*********************************")
        list_of_all_exhibits()
    else:
        print("exhibit not found.")

####################################################################
#Exhibit_menu/ Delete Exhibit 
def delete_exhibit():
    exhibit_id = input("Enter exhibit ID to delete: ")
    exhibit = Exhibit.find_exhibit_by_id(exhibit_id)
    if exhibit:
        exhibit.delete()
        print(f"""
          
          |-------------------------------------------|
          |*****|Updated Exhibit: {exhibit.name}|*****|
          |-------------------------------------------|
    
          """)
        print("************** Deleted Exhibit *******************")
        print(f"Deleted exhibit:|Exhibit name: {exhibit.name}|Open: {exhibit.status}|Museum Located: {exhibit.museum_id}")
        print("*********************************")
        list_of_all_exhibits()
    else:
        print("exhibit not found.")