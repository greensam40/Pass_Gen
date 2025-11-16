# Password Generator GUI

A Python GUI application to generate secure passwords with customizable options. This project allows users to easily create strong passwords and copy them to the clipboard, packaged as a standalone Windows executable for convenience.

## Features
Set desired password length; choose character types: Uppercase letters (A-Z), Lowercase letters (a-z), Numbers (0-9), Special characters (!, @, #, etc.); copy password to clipboard with one click; clear password button; packaged as a standalone EXE for Windows.

## Technologies Used
Python 3.10+, Tkinter (GUI), pyperclip (clipboard functionality), PyInstaller (creating EXE).

## How to Run
1. Clone this repository: `git clone https://github.com/greensam40/Pass_Gen.git`  
2. Navigate to the project folder: `cd Pass_Gen`  
3. Install dependencies: `pip install pyperclip`  
4. Run the Python script: `python Pass_Gen.py`  
**OR** use the pre-built Windows executable in the `dist` folder.

## Usage
Enter the desired password length, select character types, click **Generate Password**, copy to clipboard with **Copy**, clear the field with **Clear**.

## Learning Points
Building GUI applications with Tkinter, handling input validation and user-friendly interfaces, using Python libraries like pyperclip, packaging Python scripts into standalone Windows executables.
