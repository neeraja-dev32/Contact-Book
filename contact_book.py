while True:
    print("\n--- Contact Book ---")
    
    print("1.Add Contact")
    print("2.View Contacts")
    print("3.Search Contact")
    print("4.Delete Contact")
    print("5.Exit")

    choice = input("enter choice: ")
    

    if choice == "1":
        
        name = input("enter name: ")
        phone = input("enter phone: ")
        

        file = open("contacts.txt", "a")
        file.write(name + "," + phone + "\n")
        file.close()

        print("Contacts added successfully")

    elif choice == "2":
         file = open("contacts.txt", "r")
         data = file.readlines()
         file.close()
    
         if len(data) == 0:
            print("no contacts found")
         else:
             for line in data:
                 name,phone = line.strip().split(",")
                 print("name:", name, "|phone:", phone)

    elif choice == "3":
         search_name = input("enter name to search: ").lower()

         file = open("contacts.txt", "r")
         found = False

         for line in file:
             name,phone = line.strip().split(",")
             if name.lower() == search_name:
                print("found - name:", name, "|phone:", phone)
                found = True
                break
         file.close()

         if not found:
             print("contact not found")

    elif choice == "4":
         delete_name = input("enter name to delete: ").lower()

         file = open("contacts.txt", "r")
         lines = file.readlines()
         file.close()

         file = open("contacts.txt", "w")
         found = False

         for line in lines:
            name,phone = line.strip().split(",")

            if name.lower() != delete_name:
               file.write(line)

            else:
                found = True

         file.close()

         if found:
             print("contact deleted successfully")
         else:
             print("contact not found")

    elif choice == "5":
      print("exiting...")
      break


    else:
      print("invalid choice")
    

    
