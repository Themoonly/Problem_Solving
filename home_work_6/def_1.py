def insert_country(data_dict):
    country = input("Insert new country: ")
    if country not in data_dict:
        data_dict[country] = {}
        print(f"Added new country: {country}")
    else:
        print(f"{country} already exists!")

def insert_region(data_dict):
    country = input("Select country: ")
    if country in data_dict:
        region = input("Insert new region: ")
        if region not in data_dict[country]:
            data_dict[country][region] = []
            print(f"Added new region: {region} to {country}")
        else:
            print(f"Region {region} already exists in {country}!")
    else:
        print(f"Country {country} not found!")

def insert_province(data_dict):
    country = input("Select country: ")
    if country in data_dict:
        region = input("Select region: ")
        if region in data_dict[country]:
            province = input("Enter new province: ")
            if province not in data_dict[country][region]:
                data_dict[country][region].append(province)
                print(f"Added new province: {province} to {region} in {country}")
            else:
                print(f"Province {province} already exists in {region}!")
        else:
            print(f"Region {region} not found in {country}!")
    else:
        print(f"Country {country} not found!")

def view_all_data(data_dict):
    print("Current Data:", data_dict)

def main():
    data_dict = {"Thailand": {"Central": ["Bangkok"]}}
    
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
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 0:
                print(f"Your choice = {choice}, program exiting now!!")
                break
            elif choice == 1:
                print("=====================")
                print("Enter 1 to add country")
                print("Enter 2 to add region")
                print("Enter 3 to add province")
                print("=====================")
                insert_choice = int(input("Enter your choice: "))
                
                if insert_choice == 1:
                    insert_country(data_dict)
                elif insert_choice == 2:
                    insert_region(data_dict)
                elif insert_choice == 3:
                    insert_province(data_dict)
                else:
                    print("Invalid choice!")
            elif choice == 5:
                view_all_data(data_dict)
            else:
                print("Functionality not implemented yet!")
                
        except ValueError:
            print("Enter number only!!!")
            break

if __name__ == "__main__":
    main()
