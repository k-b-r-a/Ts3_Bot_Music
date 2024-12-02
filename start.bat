@echo off

rem Define the name of the virtual environment
set VENV_NAME=venv

rem Check if the virtual environment already exists
if not exist %VENV_NAME% (
    rem Create a Python virtual environment
    py -3.10 -m venv %VENV_NAME%
	
	rem Activate the virtual environment
	call %VENV_NAME%\Scripts\activate
	
	rem Upgrade pip 
	py -m pip install --upgrade pip
	
	rem Install packages from requirements.txt
	pip install -r requirements.txt
)

rem Activate the virtual environment
call %VENV_NAME%\Scripts\activate

rem Run script
start main.py

exit