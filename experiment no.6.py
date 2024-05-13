def verify_data(data):
   
    if data.isalpha():
        return True
    else:
        return False

def main():
    user_data = input("Enter your data: ")
    if verify_data(user_data):
        print("Welcome, " + user_data + "!")
    else:
        print("Invalid data! Please enter only alphabets.")

if __name__ == "__main__":
    main()
