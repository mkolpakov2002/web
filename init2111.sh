sudo ln -sf /home/box/web/etc/nginx2111.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn_conf_django.py /etc/gunicorn.d/gunicorn_conf
sudo /etc/init.d/gunicorn restart
cd /home/box/web/ask                                                            
gunicorn ask.wsgi:application --bind 0.0.0.0:8000 &
# gunicorn -b 0.0.0.0:8000 wsgi & 
