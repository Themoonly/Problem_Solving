#6706022510395 ธีรยุทธ ปาแก้ว
#6706022510280 ขจรศักดิื ศรีอุบล 
#6706022510298 ภูริบัญชร เข็มเงิน
def insert_data_country(data_dict):
    country = input("insert new country : ")
    country = country.lower()
    if country not in data_dict:
        data_dict[country] = {}
        print("-----New country successfully added-----")
    else:
        print("-----can't insert-----")
def insert_data_region(data_dict):
    country  = input("Search your country : ")
    country = country.lower()
    if country in data_dict:
        region = input("insert new region : ")
        if region not in data_dict[country]:
            data_dict[country][region] = []
            print("-----New country successfully added-----")
        else:
            print("-----can't insert-----")
    else:
        print(f"not found {country}")
def insert_data_province(data_dict):
    country  = input("Search your country : ")
    country = country.lower()
    if country in data_dict:
        region = input("Search your region : ")
        region = region.lower()
        if region in data_dict[country]:
            province = input("insert new province : ")
            province = province.lower()
            if province not in data_dict[country][region]:
                data_dict[country][region].append(province)
                print(f"insert {province} in {region} at {country}")
                print("-----New country successfully added-----")
            else:
                print(f"can't insert {province} in {region}")
                print("-----can't insert-----")
        else:
            print(f"not found {region}")
            print("-----can't insert-----")
    else:
        print(f"not found {country}")
        print("-----can't insert-----")

def update_country(data_dict):
    country = input("Select country for change: ")
    country = country.lower()
    if country not in data_dict:
        print(f"Country {country} not found!")
    else:
        new_country = input(f"Enter new name for {country}: ")
        # Update the dictionary by renaming the country
        data_dict[new_country] = data_dict.pop(country)
        print(f"Updated {country} to {new_country}")
        

def update_region(data_dict):
    country = input("select country : ")
    country = country.lower()
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
    country = country.lower()
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
    country = country.lower()
    if country in data_dict:
        print(f"country : {country}")
    else:
        print(f"can't find : {country}")
def search_region(data_dict):
    region = input("Search region: ")
    region = region.lower()
    found = False
    
    for key_country, country in data_dict.items():
        if region in country:
            print(f"Region: {region} at {key_country}")
            found = True
    if not found:
        print(f"Can't find: {region}")


def search_province(data_dict):
    province = input("search province : ")
    province = province.lower()
    found = False
    for key_conutry , country in data_dict.items():
        for key_region , region in country.items():
            if province in region:
                print(f"province : {province} in {key_region} at {key_conutry}")
                found = True
    if not found:
        print(f"can't find : {province}")

def delete_country(data_dict):
    country = input("select  country : ")
    country = country.lower()
    if country in data_dict:
        data_dict.pop(country)
        print(f"delete country : {country}")
    else:
        print(f"can't found : {country}")
def delete_region(data_dict):
    country = input("select  country : ")
    country = country.lower()
    if country in data_dict:
        region = input("select region : ")
        region = region.lower()
        if region in data_dict[country]:
            data_dict[country].pop(region)
            print(f"delete region : {region}")
        else:
            print(f"can't found : {country}")
    else:
        print(f"can't found : {country}")
def delete_province(data_dict):
    country = input("select  country : ")
    country = country.lower()
    if country.lower() in data_dict:
        region = input("select region : ")
        region = region.lower()
        if region in data_dict[country]:
            province = input("select province : ")
            province = province.lower()
            if province in data_dict[country][region]:
                data_dict[country][region].remove(province)
            else:
                print(f"can't found : {province}")
        else:
            print(f"can't found : {country}")
    else:
        print(f"can't found : {country}")

def view_data(data_dict):
    for country, regions in data_dict.items():
        print(f"{country.capitalize()}:")
        if isinstance(regions, dict) and regions:
            for region, cities in regions.items():
                print(f"  {region.capitalize()}:")
                for city in cities:
                    print(f"    - {city.capitalize()}")
        else:
            print("  No regions available.")
        print()

def main():
    data_dict = {
    "thailand": {
        "central": ["bangkok", "suphanburi", "chainat", "ayutthaya", "nonthaburi", "pathumthani"],
        "northeastern": ["kalasin", "khon kaen", "chaiyaphum", "ubon ratchathani", "nakhon ratchasima", "mahachai"],
        "northern": ["chiang mai", "chiang rai", "lampang", "lamphun", "payao", "phayao"],
        "southern": ["hat yai", "phuket", "krabi", "surat thani", "chumphon", "nakhon si thammarat"]
    },
    "america": {
        "northern": ["guatemala", "el salvador", "honduras", "nicaragua", "costarica", "panama"],
        "western": ["california", "oregon", "washington", "nevada", "utah"],
        "eastern": ["new york", "florida", "texas", "virginia", "north carolina"],
        "southern": ["georgia", "alabama", "mississippi", "louisiana", "tennessee"]
    }
}

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
            print("Enter 1 to search country")
            print("Enter 2 to search region")
            print("Enter 3 to search province")
            print("=====================")

            search_choice = int(input(f"enter yout choice : "))

            if search_choice  == 1:
                search_country(data_dict)
            elif search_choice  == 2:
                search_region(data_dict)
            elif search_choice == 3:
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
        input("Please Enter to continue ")
main()
