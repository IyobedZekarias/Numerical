from http import server
import multiprocessing
# bind = "127.0.0.1:5000"
workers = multiprocessing.cpu_count() * 2 + 1
reload = True
threads = 3
max_requests = 1000
timeout = 3600
# certfile = '/Users/nbstr/ssl/certificate.pem'
# keyfile = '/Users/nbstr/ssl/key.pem'

# gunicorn -c gunicorn.conf.py wsgi:app