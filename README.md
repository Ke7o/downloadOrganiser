# Download Organiser

A command-line based program that sorts files by their types and organizes them into respective subfolders. This is a particularly useful tool for managing your downloads folder or any directory with a large number of unsorted files.

This is the first program I built using Neovim on my Debian system.

## Features

- Automatically detects file types and moves them into categorized subfolders.
- Supports a variety of file types, such as documents, images, installers/installable files, project files, and more.
- Simple and easy to use with minimal setup required.

## How to use

1. Change the first Path variable to the file path where the files you with to organise are contained, and save your changes.

2. In your command-line, once in the directory where the downloadOrganiser.py file is located, enter 'python3 downloadOrganiser.py' to run the program.

3. Sit back, relax, and watch all your files dissapear into their appropriate folders. :)

   

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠈⠁⠀⠀⠈⠀⠠⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⡅⠀⠀⠀⠀⠀⢀⠤⢄⠀⠀⠁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣧⠀⠀⠀⠀⠀⠀⣾⣦⣾⡇⠀⠀⠰⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⠇⠀⠀⠀⠀⠀⠸⣟⣛⡁⠇⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠆⢄⣀⠤⠤⠤⠤⠄⢀⣀⣀⠤⠀⠀⢡⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢢⢚⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡀⠀⠘⡲⠤⢄⣐⣈⢀⣀⣂⠬⠞⠥⣦⠑⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡀⠀⠂⠀⠀⢀⠊⠀⠀⠀⠀⠀⠈⡐⠁⠀⠀⠀⠈⣟⠪⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⡄⢰⠀⠀⠀⢀⠁⠀⠀⠀⠂⠄⠤⠴⠁⠀⠀⠀⠀⠀⡿⠐⠨⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠤⠤⠁⠠⠠⡼⠀⠀⠀⠀⢸⠀⢀⠄⠈⠡⢀⢀⢀⠜⢨⠁⠀⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠆⢡⠀⠀⠀⠘⠀⠐⠒⠤⣀⠠⠞⠊⠀⢸⠐⣀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡰⠄⠀⠀⠉⠉⠀⠀⠀⠀⠃⡀⠀⢸⠀⢸⢲⢼⠃⠀⠄⠈⠀⠀⠀⠁⢢⠀
⠀⠀⠀⠀⠀⠄⠀⠢⠀⠀⠀⢀⠀⠀⠀⠀⠠⠉⠁⠀⠈⠪⣇⡎⡠⠁⠀⠀⣠⠤⣄⠀⠀⠆
⠀⠀⠀⠀⢠⠀⠀⠀⠑⢤⠀⠚⠠⢀⡀⠰⠁⠀⠀⠀⠀⠀⢻⠊⠀⠀⠀⡞⠀⠀⠀⠀⠀⡇
⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⡕⠂⠀⠤⠠⢽⡀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠂⠙⣄⡀⢀⢈⠔⠀
⠀⠀⠀⠐⣄⢠⠀⣀⠴⠐⠀⠀⠀⠀⠀⠀⠐⡀⠀⠀⠀⠀⢨⠁⠒⠂⠐⠀⠀⠙⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢃⠠⡀⢀⡡⢈⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
