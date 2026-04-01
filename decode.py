import codecs

def decode():
    prompt = 0
    while True:
            try:
                prompt = int(input("Hello user! Enter any integer (0-9) to begin decoding your file.\nEnter -1 to return to the menu: : "))
            except ValueError:
                print("Invalid input. Please enter an intger: ")
                continue

            if prompt == -1:
                break
            elif 0 <= prompt <= 9:
                try: #receive the .txt file from the user
                    file_input = input("Input the file you would like to decode (.txt file only): ")

                    with open(file_input, "r") as file:
                        text = file.read()
                    
                    #apply ROT-13 decryption
                    decoded = codecs.encode(text, 'rot_13')
                    output_file = input("Enter the output file name (____.txt): ")

                    with open(output_file, "w") as f:
                        f.write(decoded)

                    print("Your file has been decoded and saved.")
                except FileNotFoundError: #ensures file can be found before decyrption
                    print("File not found.")
            else: #ensures the user stays within the prompt restraints
                print("Invalid input.. Enter a number from 0-9 to continue, or -1 to return to the menu: ")
    