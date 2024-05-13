def main():
    strings_list = []  

    
    while True:
        user_input = input("Enter a string (or type 'stop' to end): ")
        if user_input.lower() == 'stop':
            break 
        strings_list.append(user_input) 

    # Print the list of strings
    print("\nList of strings:")
    for string in strings_list:
        print(string)

if __name__ == "__main__":
    main()
