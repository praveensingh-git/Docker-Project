user_name = input("Enter your name to store or press Enter to proceed: ").strip()

if user_name:
    with open('userinfo.txt', 'a') as file:
        file.write(user_name + '\n')

show_info = input("Do you want to see all stored user names? (Y/N): ").strip().lower()

if show_info in ['y', 'yes']:
    try:
        with open('userinfo.txt', 'r') as file:
            content = file.readlines()
    except FileNotFoundError:
        print("No user data found.")
    else:
        print("\nStored User Names:")
        for line in content:
            print(f'- {line}')

elif show_info in ['n', 'no']:
    print("Okay, not showing any user data.")

else:
    print("Invalid option. Please enter 'Y' or 'N'.")
