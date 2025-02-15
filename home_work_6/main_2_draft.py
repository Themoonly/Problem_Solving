data_dict = { 
    "Thailand" : {
        "Central" : ["Bangkok"]
        }
    }

while True:

    print("================================")
    print("Select   1   for      InsertDAta")
    print("Select   2   for      UpdateData")
    print("Select   3   for      SearchData")
    print("Select   4   for      DeleteData")
    print("Select   5   for     ViewAllData")
    print("================================")
    print("      enter '0' continue        ")
    print("================================")

    try:
        choice = int(input("Enter your choice : "))
        if choice == 0:
            print(f"your choice = {choice} program break now!!")
            break

# insert_dict

        elif choice == 1:
            print("=====================")
            print("enter 1 for country")
            print("enter 2 for region")
            print("enter 3 for province")
            print("=====================")

            insert_choice = int(input("enter your choice : "))
            if insert_choice == 1:
                insert_country = input("insert new country :")
                if insert_country not in data_dict:
                    data_dict[insert_country] = {}

            elif insert_choice == 2:
                insert_country = input("select country :")
                if insert_country in data_dict:
                    insert_region = input("insert new region : ")
                    if insert_region not in data_dict[insert_country]:
                        data_dict[insert_country][insert_region] = []
                    
            elif insert_choice == 3:
                insert_country = input("select country : ")
                if insert_country in data_dict:
                    insert_region = input("select region : ")
                    if insert_region in data_dict[insert_country]:
                        insert_province = input("enter new province : ")
                        if insert_province not in data_dict[insert_country][insert_region]:
                            data_dict[insert_country][insert_region].append(insert_province)
# UpdateData

        elif choice == 2:
            print(choice)

# SearchData

        elif choice == 3:
            print(choice)
# DeleteData

        elif choice == 4:
            print(choice)
# view_dict
        elif choice == 5:
            print(data_dict)

    except ValueError():
        print("Enter number only!!!")
        break

   

