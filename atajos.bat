@echo off
doskey rs=python manage.py runserver
doskey ps=python manage.py shell
doskey mm=python manage.py makemigrations
doskey m=python manage.py migrate
doskey dbs=python manage.py dbshell
doskey idb=python manage.py inspectdb

echo Atajos agregados!
echo. 
echo rs == runserver
echo ps == shell
echo mm == makemigrations
echo m == migrate
echo dbs == dbshell
echo idb == inspectdb