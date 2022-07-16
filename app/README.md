docker-compose run web django-admin startproject django_main .

python manage.py startapp shop_scheduler

_  -p, --project-name

docker-compose -p shop_scheduler_prod -f docker-compose.prod.yml down -v
docker-compose -p shop_scheduler_prod -f docker-compose.prod.yml up -d --build 
docker-compose -p shop_scheduler_prod -f docker-compose.prod.yml exec web python manage.py migrate --noinput

python manage.py createsuperuser
