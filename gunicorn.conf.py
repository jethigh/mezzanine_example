from __future__ import unicode_literals
import multiprocessing

bind = "unix:/home/vagrant/mezzanine/mezzanine_example/gunicorn.sock"
workers = multiprocessing.cpu_count() * 2 + 1
errorlog = "/home/vagrant/logs/mezzanine_example_error.log"
loglevel = "error"
proc_name = "mezzanine_example"
