def insert_data_country(data_dict):
    country = input("insert new country : ")
    if country.lower() not in data_dict:
        data_dict[country] = {}
        print(f"insert new country : {country}")
    else:
        print(f"can't insert {country}")
def insert_data_region(data_dict):
    country  = input("insert new region : ")
    if country in data_dict:
        region = input("insert new region : ")
        if region not in data_dict[country]:
            data_dict[country][region] = []
            print(f"insert new region {region} to {country}")
        else:
            print(f"can't insert {region} to {country}")
    else:
        print(f"not found {country}")
def insert_data_province(data_dict):
    country  = input("insert new region : ")
    if country in data_dict:
        region = input("insert new region : ")
        if region in data_dict[country]:
            province = input("insert new province : ")
            if province not in data_dict[country][region]:
                data_dict[country][region].append(province)
                print(f"insert {province} to {region} in {country}")
            else:
                print(f"can't insert {province} to {region}")
        else:
            print(f"not found {region}")
    else:
        print(f"not found {country}")

def update_country(data_dict):
    country = input("select country for chang : ")
    if country in data_dict:
        new_country = input(f"Enter new name for {country}: ")
        # data_dict = new_country
        data_dict[new_country] = data_dict.pop(country)
        # data_dict.update({data_dict : new_country})

        print(f"Updated {country} to {new_country}")
    else:
        print(f"Country {country} not found!")
def update_region(data_dict):
    country = input("select country : ")
    if country in data_dict:
        region = input("select region for chang : ")
        if region in data_dict[country]:
            new_region = input(f"Enter new name for {region}: ")
            data_dict.update({country : new_region})
            print(f"update {region} to {new_region}")
        else:
            print(f"region {region} not found")
    else:
        print(f"country {country} not found")
def update_province(data_dict):
    country = input("Select country : ")
    if country in data_dict:
        region = input("Select region : ")
        if region in data_dict[country]:
            province = input("Select province to change : ")
            if province in data_dict[country][region]:
                new_province = input(f"Enter new name for {province} : ")
                index = data_dict[country][region].index(province)
                data_dict[country][region][index] = new_province
                # data_dict.update({province : new_province})
                print(f"Updated {province} to {new_province}")
            else:
                print(f"Province {province} not found in {region}!")
        else:
            print(f"Region {region} not found in {country}!")
    else:
        print(f"Country {country} not found!")

def search_country(data_dict):
    country = input("search country : ")
    if country in data_dict:
        print(f"country : {country}")
    else:
        print(f"can't find : {country}")
def search_region(data_dict):
    region = input("search region : ")
    for key_country , country in data_dict.items():
        if region in country:
            print(f"region : {region} in {key_country}")
        else:
            print(f"can't find : {region} ")
def search_province(data_dict):
    province = input("search province : ")
    for key_conutry , country in data_dict.items():
        for key_region , region in country:
            if province in region:
                print(f"province : {province} in {key_region} at {key_conutry}")
            else:
                print(f"can't find : {province}")

def delete_country(data_dict):
    country = input("select  country : ")
    if country in data_dict:
        data_dict.pop(country)
        print(f"delete country : {country}")
    else:
        print(f"can't found : {country}")
def delete_region(data_dict):
    country = input("select  country : ")
    if country in data_dict:
        region = input("select region : ")
        if region in data_dict[country]:
            data_dict[country].pop(region)
            print(f"delete region : {region}")
        else:
            print(f"can't found : {country}")
    else:
        print(f"can't found : {country}")
def delete_province(data_dict):
    country = input("select  country : ")
    if country in data_dict:
        region = input("select region : ")
        if region in data_dict[country]:
            province = input("select province : ")
            if province in data_dict[country][region]:
                data_dict[country][region].pop(province)
            else:
                print(f"can't found : {province}")
        else:
            print(f"can't found : {country}")
    else:
        print(f"can't found : {country}")

def view_data(data_dict):
    print(data_dict)

def main():
    data_dict = {"thailand" : {"central" : ["bangkok"]}}

    while True:
        print("================================")
        print("Select   1   for      InsertData")
        print("Select   2   for      UpdateData")
        print("Select   3   for      SearchData")
        print("Select   4   for      DeleteData")
        print("Select   5   for     ViewAllData")
        print("================================")
        print("      enter '0' to exit         ")
        print("================================")

        choice = int(input("please select your choice : "))
        if choice == 0:
            print(f"your choice = {choice}, program exting now!!!")
            break

        elif choice == 1:
            print("=====================")
            print("Enter 1 to add country")
            print("Enter 2 to add region")
            print("Enter 3 to add province")
            print("=====================")

            insert_choice = int(input(f"enter yout choice : "))
            
            if insert_choice == 1:
                insert_data_country(data_dict)
            elif insert_choice == 2:
                insert_data_region(data_dict)
            elif insert_choice == 3:
                insert_data_province(data_dict)
            else:
                print("invalid choice!")

        elif choice == 2:
            print("=====================")
            print("Enter 1 to update country")
            print("Enter 2 to update region")
            print("Enter 3 to update province")
            print("=====================")

            update_choice = int(input(f"enter yout choice : "))

            if update_choice == 1:
                update_country(data_dict)
            elif update_choice == 2:
                update_region(data_dict)
            elif update_choice == 3:
                update_province(data_dict)
   
        elif choice == 3:
            print("=====================")
            print("Enter 1 to update country")
            print("Enter 2 to update region")
            print("Enter 3 to update province")
            print("=====================")

            search_choice = int(input(f"enter yout choice : "))

            if search_choice  == 1:
                search_country(data_dict)
            elif search_choice  == 2:
                search_region(data_dict)
            elif update_choice == 3:
                search_province(data_dict)


        elif choice == 4:
            print("=====================")
            print("Enter 1 to delete country")
            print("Enter 2 to delete region")
            print("Enter 3 to delete province")
            print("=====================")

            delete_choice = int(input(f"enter yout choice : "))

            if delete_choice == 1:
                delete_country(data_dict)
            elif delete_choice == 2:
                delete_region(data_dict)
            elif delete_choice == 3:
                delete_province(data_dict)

        elif choice == 5:
            view_data(data_dict)

main()
