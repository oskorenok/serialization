:: This CMD script provides code validation.

@echo off
setlocal
:PROMPT
set /p AREYOUSURE=Are you running this cmd in the conda environment? (Y/[N])?
if /i "%AREYOUSURE%" neq "Y" EXIT

echo [Checking what the black can do...]

black --config pyproject.toml --check .

set /p AREYOUSURE=Proceed formating with the black? (Y/[N])?
if /i "%AREYOUSURE%" neq "N" call :FORMAT_CODE
echo [Done]

echo [Checking code with the flake8...]
echo [flake8 report (%date%-%time%)] >> validation_report.txt
flake8 . >> validation_report.txt
echo [Done]

echo [Checking code with the mypy...]
echo [mypy report (%date%-%time%)] >> validation_report.txt
mypy . >> validation_report.txt
echo [Done]

echo [Sorting imports with isort...]
echo [isort report (%date%-%time%)] >> validation_report.txt
isort . >> validation_report.txt
echo [Done]

echo [Validation completed]

EXIT /B 

:FORMAT_CODE
black --config pyproject.toml .
echo Code was formated with the black
EXIT /B 0