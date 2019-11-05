# ~/iEx/nginx_gunicorn/configs$ gunicorn -c ethiopia_com_gunicorn_config.py public.run:app
#kill $(cat /home/kirub/iEx/nginx_gunicorn/ethiopia.com/logs/flask_pid.pid) #kill
#kill -HUP $(cat /home/kirub/iEx/nginx_gunicorn/ethiopia.com/logs/flask_pid.pid) #restart


workers = 1
#preload_app = True
bind = "localhost:8000"
errorlog = "/home/kirub/iEx/nginx_gunicorn/ethiopia.com/logs/flask_error.log"
accesslog = "/home/kirub/iEx/nginx_gunicorn/ethiopia.com/logs/flask_access.log"
loglevel = "debug"
#max_requests = 50
pidfile = "/home/kirub/iEx/nginx_gunicorn/ethiopia.com/logs/flask_pid.pid"
chdir = "/home/kirub/iEx/nginx_gunicorn/ethiopia.com"
timeout = 1900
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" "%(m)s" "%(U)s" "%(q)s" "%(H)s" %(B)s %(T)s %(p)s "%({Header}i)s" "%({Header}o)s" "%({Header}e)s"'
