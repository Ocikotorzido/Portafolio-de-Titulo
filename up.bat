rem run a python server typing 'up'.
set CURRDIR=%~dp0
explorer "http://localhost:8000/"
start "python" "%CURRDIR%\manage.py" "runserver"