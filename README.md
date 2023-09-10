[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

### GitHub Tool

Welcome to the GitHub Tool, a command-line utility for simplifying interactions with GitHub. This tool allows you to perform various GitHub-related tasks, such as cloning repositories, creating repositories, and managing your GitHub access token.

### Table of Contents

    - Getting Started
    - Usage
        - Clone a Repository
        - Create a Repository
        - Remove a Token
        - Exit
    - Prerequisites
    - Contributing
    - License

# Getting Started

# Installations

## Dependencies

Python >3.0

Request Package

```bash
pip install requests
```

git-user23 Package https://pypi.org/project/git-user23/

```bash
pip install git_user23
```

Clone this repository to your local machine:

```bash
git clone https://github.com/samuelogboye/git-tool.git
```

Navigate to the project directory:

```bash
cd git-tool
```

Run Make

```bash
make
```

```bash
samuel@samuel-HP-EliteBook-x360-1030-G3:~/Documents/practice/git_clone_script/git-tool$ make
Welcome to the GitHub Tool v0.0.1 - By Samuel Ogboye
This tool will help you clone a GitHub repository using your GitHub token.
This is a secure way to clone a GitHub repository without exposing your GitHub token.
You will be prompted to enter your GitHub username and token.
Your token will be saved in a configuration file in your home directory.
Your token will not be displayed on the screen.
Your token will be used to clone the repository.
Your token will be deleted after cloning the repository.
Your token will not be saved anywhere else.
Your token will not be shared with anyone.
Your token will not be used for any other purpose.
Your token will not be used to access any other repository.
Your token will not be used to access any other resource.
Your token will not be used to access any other service.
Your token will not be used to access any other website.
Your token will not be used to access any other application.
Your token will not be used to access any other system.
Your token will not be used to access any other file.
--------------------------
Enter your GitHub username:
```

Follow the prompt

```bash
Username confirmed
GitHub Full Name: Samuel Ogboye
Username saved in config file at /root/config.ini
--------------------------
Enter your GitHub token:
Confirm your GitHub token:
Token confirmed
GitHub token added to ***.
Keep your token safe!
--------------------------

'gittool' file will be moved to /bin so it become executable
'gittool' has been made executable and moved to '/bin'.
--------------------------

You can now use the 'gittool' command to work on your GitHub repository.

'gittool' Always
Thank you for using the git-tool v0.0.1 - By Samuel Ogboye
```

You can close the browser or close your session or run the refresh command

```bash
source ~/.bashrc
```

You are now ready to use gittool

You can run 'gittool' in any directory of your choice

```bash
root@e142617b2a78:~/pract/git-tool# gittool
Welcome to the GitHub Tool by Samuel Ogboye
1. Clone a Repository
2. Create a Repository
3. Remove a Token
4. Exit
--------------------------
Select what you want to do:
```

If you get

```bash
Token is not set. You wanna set now? (y/n):
```

Dont worry, your token that is in the environment is not yet synchornized.
Just refresh as said earlier

### Usage

The git-tool provides the following options:

## Clone a Repository

Allows you to clone your GitHub repository to your local machine in 3 steps.

- run gittool
- choose 1 to clone and youll see the list of all your public repos
- choose 1 and it clones immediately

## Create a Repository

Enables you to create a new public GitHub repository in 3 steps

- run gittool
- choose 2 to create
- type the name then hit enter

## Remove a Token

Allows you to remove your GitHub access token from your environment variables.

## Exit

Exits the GitHub Tool.

### Prerequisites

Before using the GitHub Tool, ensure you have the following:

    - Python 3.x installed on your system.
    - Request module installed
    - git-user23 module installed

### Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please create an issue or submit a pull request.
License

This project is licensed under the MIT License - see the LICENSE file for details.
