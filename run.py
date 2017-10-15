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


def save_credentials(account):
    return account.save_account(account)


def find_accounts(acc_name):
    return Credentials.find_account(acc_name)


def check_accounts(acc_name):
    return Credentials.check_account_existence(acc_name)


def display_user_accounts():
    return Credentials.display_users()


def main():
    print("Hello, Welcome to the Password L0cker.")
    username = input()

    print(f"Hello {user_name}. Please enter your Password:
    user_password=input()
    print('\n')
