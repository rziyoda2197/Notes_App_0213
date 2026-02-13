from notes import add_note, show_notes, delete_note, search_note

while True:
    print("\n--- NOTES APP ---")
    print("1. Add note")
    print("2. Show notes")
    print("3. Delete note")
    print("4. Search")
    print("0. Exit")

    choice = input("Select: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        show_notes()
    elif choice == "3":
        delete_note()
    elif choice == "4":
        search_note()
    elif choice == "0":
        break
    else:
        print("Invalid")
