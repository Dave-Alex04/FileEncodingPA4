def wordcount():
    prompt = 0
    while True:
        try:
            prompt = int(input("Hello user! Enter any integer (0-9) to get the word count of your file.\nEnter -1 to return to the menu: : "))
        except ValueError:
            print("Invalid input. Please enter an intger: ")
            continue

        if prompt == -1:
            break
        elif 0 <= prompt <= 9:
            try:
                file_input = input("Input the file you would like to get the word count for (.txt file only): ")

                with open('toot.txt', 'r') as file:
                    data = file.read()
                    words = data.split()
                    print(f"Total words: {len(words)}")
        
            except FileNotFoundError:
                print("File not found. )")
        else:
            print("Enter a number from 0-9, or -1 to return to the menu: ")
