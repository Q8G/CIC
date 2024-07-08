@echo off
for /f "tokens=* delims=" %%i in ('python CIC.py') do set result=%%i
if "%result%"=="Online" (
    color 0A
    echo %result%
) else (
    color 0C
    echo %result%
)
pause >nul
