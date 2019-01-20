#!/usr/bin/bash

sudo /etc/init.d/gunicorn stop test
sudo /etc/init.d/gunicorn stop gunicorn-django.conf

sudo rm /etc/nginx/sites-enabled/test.conf
sudo rm /etc/gunicorn.d/test
sudo rm /etc/gunicorn.d/gunicorn-django.conf
sudo rm /etc/nginx/sites-enabled/default

# sudo pip3 uninstall gunicorn
# sudo pip3 uninstall django

if [ ! -d '/home/box/web/myenv' ]; then
  mkdir /home/box/myenv
else
  rm -rf /home/box/web/myenv/*
fi

virtualenv --python=python3.4 /home/box/web/myenv
source /home/box/web/myenv/bin/activate
pip3 install -r requirements.txt

# sudo pip3 install -r requirements.txt

# sudo vi /usr/sbin/gunicorn-debian
# sudo vi /usr/bin/gunicorn
# sudo vi /usr/bin/gunicorn_django
# sudo vi /usr/bin/gunicorn_paster

myenv/bin/gunicorn -b 0.0.0.0:8080 --pythonpath /home/box/web/ hello:hello &
myenv/bin/gunicorn -b 0.0.0.0:8000 --pythonpath /home/box/web/ask ask.wsgi:application &

sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
# sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
# sudo ln -s /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/gunicorn-django.conf
# sudo /etc/init.d/gunicorn restart test
sudo /etc/init.d/mysql start
# sudo /etc/init.d/gunicorn restart gunicorn-django.conf
