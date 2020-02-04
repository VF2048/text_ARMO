Push-Location $PSScriptRoot
Start-Process py Server.py
Start-Process (npm start)
Pop-Location