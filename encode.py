import codecs

def encode():
    prompt = 0
    
    while True:
            try:
                prompt = int(input("Hello user! Enter any integer (0-9) to begin encoding your file.\nEnter -1 to return to the menu: : "))
            except ValueError:
                print("Invalid input. Please enter an intger: ")
                continue

            if prompt == -1:
                break
            elif 0 <= prompt <= 9:
                try:
                    file_input = input("Input the file you would like to encode (.txt file only): ")

                    with open(file_input, "r") as file:
                        text = file.read()
                    
                    #apply ROT-13 encryption
                    encoded = codecs.encode(text, 'rot_13')
                    output_file = input("Enter the output file name (____.txt): ")

                    with open(output_file, "w") as f:
                        f.write(encoded)

                    print("Your file has been encoded and saved.")
                except FileNotFoundError:
                    print("File not found.")
            else:
                print("Enter a number from 0-9, or -1 to return to the menu: ")
