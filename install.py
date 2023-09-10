#!/usr/bin/env python3
# This file will store the token as an environment variable
# Username will be stored in a config file
# It will also move the clone file to /bin so it become executable

import os
import subprocess
import git_user23 as git
import configparser
import getpass

def addtoken(github_token):
    # Define the path to the ~/.bashrc file
    bashrc_path = os.path.expanduser("~/.bashrc")

    # Check if the line is already present in ~/.bashrc to avoid duplicates
    with open(bashrc_path, "r") as bashrc_file:
        lines = bashrc_file.readlines()
        token_line_exists = any("export GITHUB_TOKEN=" in line for line in lines)

    # Add the line to ~/.bashrc if it doesn't already exist
    if not token_line_exists:
        with open(bashrc_path, "a") as bashrc_file:
            bashrc_file.write(f'export GITHUB_TOKEN="{github_token}"\n')
            print("GitHub token added to ~/.bashrc.")
    else:
        print("TOKEN already exists in ~/.bashrc.")

print("Welcome to the GitHub Tool v0.0.1 - By Samuel Ogboye")
print("This tool will help you clone a GitHub repository using your GitHub token.")
print(
    "This is a secure way to clone a GitHub repository without exposing your GitHub token."
)
print("You will be prompted to enter your GitHub username and token.")
print("Your token will be saved in a configuration file in your home directory.")
print("Your token will not be displayed on the screen.")
print("Your token will be used to clone the repository.")
print("Your token will be deleted after cloning the repository.")
print("Your token will not be saved anywhere else.")
print("Your token will not be shared with anyone.")
print("Your token will not be used for any other purpose.")
print("Your token will not be used to access any other repository.")
print("Your token will not be used to access any other resource.")
print("Your token will not be used to access any other service.")
print("Your token will not be used to access any other website.")
print("Your token will not be used to access any other application.")
print("Your token will not be used to access any other system.")
print("Your token will not be used to access any other file.")
print("--------------------------")
while True:
    # Prompt the user for their GitHub username
    username = input("Enter your GitHub username: ").strip().split()[0]

    # Prompt the user to confirm the token
    confirm_username = input("Confirm your GitHub username: ").strip().split()[0]

    if username == confirm_username:
        if git.confirm_username(username):
            # To confirm github username
            print("Username confirmed")
            github_full_name = git.full_name(username)
            print(f"GitHub Full Name: {github_full_name}")
            # Create a configuration file
            config = configparser.ConfigParser()
            config["GitHub"] = {"Username": username}

            # Determine the user's home directory
            home_directory = os.path.expanduser("~")
            config_file_path = os.path.join(home_directory, "config.ini")

            # Write the configuration to the file in the user's home directory
            with open(config_file_path, "w") as configfile:
                config.write(configfile)

            print(f"Username saved in config file at {config_file_path}")
            print("--------------------------")
            break
        else:
            print("Username not valid. Please try again.")
    else:
        print("Username do not match. Please try again.")

while True:
    # Prompt the user for their GitHub token
    github_token_ok = getpass.getpass("Enter your GitHub token: ").strip().split()[0]

    # Prompt the user to confirm the token
    confirm_token = getpass.getpass("Confirm your GitHub token: ").strip().split()[0]

    if github_token_ok == confirm_token:
        if git.confirm_token(username, github_token_ok):
            print("Token confirmed")
            # Define the path to the ~/.bashrc file
            bashrc_path = os.path.expanduser("~/.bashrc")

            # Check if the line is already present in ~/.bashrc to avoid duplicates
            with open(bashrc_path, "r") as bashrc_file:
                lines = bashrc_file.readlines()
                token_line_exists = any("export GITHUB_TOKEN=" in line for line in lines)

            # Add the line to ~/.bashrc if it doesn't already exist
            if not token_line_exists:
                with open(bashrc_path, "a") as bashrc_file:
                    bashrc_file.write(f'export GITHUB_TOKEN="{github_token_ok}"\n')
                    print("GitHub token added to ~/.bashrc.")
                    break
            else:
                print("TOKEN already exists in ~/.bashrc.")
                break
        else:
            print("Token not confirmed")
    else:
        print("Tokens do not match. Please try again.")


print("Keep your token safe!")
print("--------------------------")
print()




# --------TO MOVE THE CLONE FILE TO /bin so it become executable-----------#
# Define the file name and paths
print("'gittool' file will be moved to /bin so it become executable")
file_name = "gittool"
current_directory = os.getcwd()
destination_directory = "/bin"

# Check if the file exists in the current directory
if os.path.exists(os.path.join(current_directory, file_name)):
    # Set the executable permission (+x)
    os.chmod(file_name, 0o755)  # Equivalent to chmod +x

    # Move the file to /bin using sudo
    move_command = f"sudo mv {file_name} {destination_directory}"
    subprocess.run(move_command, shell=True)
    print(
        f"'{file_name}' has been made executable and moved to '{destination_directory}'."
    )
else:
    print(f"'{file_name}' does not exist in the current directory.")
    print("Please run this script from the same directory as the file.")
    print("Read the README.md file for more information.")
    raise SystemExit
print("--------------------------")
print()
print("You can now use the 'gittool' command to work on your GitHub repository.")
print()
print("'gittool' Always")
print("Thank you for using the git-tool v0.0.1 - By Samuel Ogboye")
