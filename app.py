import encode
import decode
import wordcount

def menu():
    while True:
        print("\n----- FILE PROCESSING MENU -----")
        print("1. Encode a file")
        print("2. Decode a file")
        print("3. Word count")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            encode.encode()
        elif choice == "2":
            decode.decode()
        elif choice == "3":
            wordcount.wordcount()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

menu()