@echo off
title Dashboard Launcher

cd /d "D:\Windrichting"

echo Starting the Tegenwind Dashboard server in a new window...

:: Start de python server in een nieuw venster. 
:: De /B vlag is optioneel en start het in hetzelfde venster, maar op de achtergrond.
:: Zonder /B is duidelijker voor de gebruiker.
start "Tegenwind Server" cmd /c "python app.py"

echo Waiting 2 seconds for the server to initialize...
timeout /t 2 /nobreak > NUL

echo Opening dashboard in your browser...
start http://127.0.0.1:5000

exit
