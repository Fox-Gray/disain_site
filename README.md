Доброго дня, 

перед запуском рекомендуется установить приложения проекта
pip install -r requirements.txt

после подготовить и выполнить миграцию
python manage.py makemigrations
python manage.py migrate

ну и запустить проект
python manage.py runserver
