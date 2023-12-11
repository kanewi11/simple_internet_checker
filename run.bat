@echo off
set "venvDir=venv"
set "requirementsFile=requirements.txt"

if not exist "%venvDir%" (
    echo Creating a virtual environment...
    python -m venv %venvDir%
)

call %venvDir%\Scripts\activate

if exist "%requirementsFile%" (
    echo Installing dependencies...
    pip install -r %requirementsFile%
) else (
    echo requirements.txt file not found.
    exit /b 1
)

echo The program is running...
python internet_checker.py

deactivate
