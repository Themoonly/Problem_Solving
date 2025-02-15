data_dict = { 
    "Thailand": {
        "Central": ["Bangkok"]
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

    try:
        choice = int(input("Enter your choice : "))

        if choice == 0:
            print(f"Your choice = {choice}, program exiting now!!")
            break
        
        elif choice == 1:
            print("=====================")
            print("Enter 1 to add country")
            print("Enter 2 to add region")
            print("Enter 3 to add province")
            print("=====================")

            insert_choice = int(input("Enter your choice : "))

            if insert_choice == 1:
                insert_country = input("Insert new country : ")
                if insert_country not in data_dict:
                    data_dict[insert_country] = {}  # เพิ่มประเทศใหม่
                    print(f"Added new country: {insert_country}")
                else:
                    print(f"{insert_country} already exists!")

            elif insert_choice == 2:
                insert_country = input("Select country : ")
                if insert_country in data_dict:
                    insert_region = input("Insert new region : ")
                    if insert_region not in data_dict[insert_country]:
                        data_dict[insert_country][insert_region] = []  # เพิ่มภูมิภาคใหม่เป็น list ว่าง
                        print(f"Added new region: {insert_region} to {insert_country}")
                    else:
                        print(f"Region {insert_region} already exists in {insert_country}!")
                else:
                    print(f"Country {insert_country} not found!")

            elif insert_choice == 3:
                insert_country = input("Select country : ")
                if insert_country in data_dict:
                    insert_region = input("Select region : ")
                    if insert_region in data_dict[insert_country]:
                        insert_province = input("Enter new province : ")
                        if insert_province not in data_dict[insert_country][insert_region]:
                            data_dict[insert_country][insert_region].append(insert_province)  # เพิ่มจังหวัดใหม่
                            print(f"Added new province: {insert_province} to {insert_region} in {insert_country}")
                        else:
                            print(f"Province {insert_province} already exists in {insert_region}!")
                    else:
                        print(f"Region {insert_region} not found in {insert_country}!")
                else:
                    print(f"Country {insert_country} not found!")

        elif choice == 5:
            print("Current Data:", data_dict)

    except ValueError:
        print("Enter number only!!!")
        break
