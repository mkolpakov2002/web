sudo ln -sf /home/box/web/etc/nginx1911.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn_conf.py /etc/gunicorn.d/gunicorn_conf
sudo /etc/init.d/gunicorn restart
gunicorn -b 0.0.0.0:8080 hello:hello_func & 
