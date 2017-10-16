#!/usr/bin/env python3.6
from pwd_locker import Credentials, Users


def create_users(user_id, fullname, username, user_password):
    new_user = Users(user_id, fullname, username, user_password)
    return new_user


def save_users(user):
    return user.save_user()


def find_user(user_id):
    return Users.find_user_by_id(user_id)


def check_users(user_id):
    return Users.check_user_existence(user_id)


def authenticate_users(user_id, username, user_password):
    return Users.authenticate_user(user_id, username, user_password)


def display_all_users():
    return Users.display_users()


def create_credentials(acc_id, acc_name, acc_email, acc_username, acc_password):
    new_account = Credentials(
        acc_id, acc_name, acc_email, acc_username, acc_password)
    return new_account


def gen_random_pwd():
    return Credentials.gen_random_password()


def save_credentials(account):
    return account.save_account()


def find_accounts(acc_name):
    return Credentials.find_account(acc_name)


def check_accounts(acc_name):
    return Credentials.check_account_existence(acc_name)


def display_user_accounts():
    return Credentials.display_users()


def main():
    print("Hello, Welcome to the Password L0cker.")
    print("Please enter your username:")
    username = input()

    print(f"Hello {username}. Please enter your Password:")
    user_password = input()
    print('\n')

    while True:
        print("Use this short codes: cu - create new user, du - display users. su - search user, cc - create new credential, dc - display credentials, sc - search credentials")
        short_code = input().lower()
        if short_code == 'cu':
            print("Create New User Pwd Locker Account")
            print("-" * 10)

            print("Assign id....")
            user_id = input()

            print("Enter Full Name....")
            fullname = input()

            print("Enter Username....")
            username = input()

            print("Enter Password....")
            user_password = input()
            # create and save new employee
            save_users(create_users(
                user_id, fullname, username, user_password))
            print('\n')
            print(
                f"New Pwd Locker User Account {user_id} {username} created for {fullname}")
            print('\n')

        elif short_code == "du":
            if display_all_users():
                print("Pwd Locker User Accounts")
                print('\n')

                for user in display_users():
                    print(
                        f"{user.user_id}{user.fullname}{user.username}{user.user_password}")
                    print('\n')

            else:
                print('\n')
                print(
                    "User Account not saved yet.... Create an account with Pwd Locker... Choose cu")
                print('\n')

        elif short_code == 'cc':
            print("Create Pwd Locker Account")
            print("-" * 10)

            print("Assign Account ID....")
            acc_id = input()

            print("Enter Account Name....")
            acc_name = input()

            print("Enter Email....")
            acc_email = input()

            print("Enter Username....")
            acc_username = input()

            print("Enter Account Password")
            print(
                "Choose to enter existing password or Generate a random password - genpwd")
            acc_pwd = input()
            while True:
                if acc_pwd == genpwd:
                    acc_password = gen_random_pwd()

            # create and save new employee
            save_credentials(create_credentials(
                acc_id, acc_name, acc_email, acc_username, acc_password))
            print('\n')
            print(
                f"New Pwd Locker Account of {acc_id}, account_name {acc_name} created for {username} ")
            print('\n')


if __name__ == '__main__':
    main()
