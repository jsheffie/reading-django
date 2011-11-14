Installing rabbitMQ
Installing Celery
Installing Django-celery

These examples (twitterfollow, and demoapp) came out of the git repository, 
https://github.com/ask/django-celery.git
twitterfollow is an incomplete example.


$ sudo rabbitmqctl add_user rm3 password
$ sudo rabbitmqctl list_users
$ sudo rabbitmqctl add_vhost rm3
$ sudo rabbitmqctl set_permissions -p rm3 rm3 ".*" ".*" ".*"


Creating table celery_taskmeta
Creating table celery_tasksetmeta
Creating table djcelery_intervalschedule
Creating table djcelery_crontabschedule
Creating table djcelery_periodictasks
Creating table djcelery_periodictask
Creating table djcelery_workerstate
Creating table djcelery_taskstate


./manage.py celeryd --loglevel=INFO
-E to enable events for celerycam
./manage.py celeryd -E --loglevel=INFO


$ sudo rabbitmqctl help
$ sudo rabbitmqctl status
$ sudo rabbitmqctl list_queues
$ sudo rabbitmqctl list_bindings
$ sudo rabbitmqctl list_connections


Celery Stuff: ( through django) 
$ ./manage.py help
$ ./manage.py celeryd
$ ./manage.py celerybeat
$ ./manage.py camqadm
$ ./manage.py celeryev
$ ./manage.py celeryctl status

$ ./manage.py celeryctl status
$ ./manage.py celeryctl inspect active
$ ./manage.py celeryctl inspect scheduled
$ ./manage.py celeryctl inspect reserved
$ ./manage.py celeryctl inspect revoked
$ ./manage.py celeryctl inspect stats
$ ./manage.py celeryctl inspect enable_events
$ ./manage.py celeryctl inspect disable_events

http://celery.readthedocs.org/en/latest/userguide/monitoring.html

Starting the monitor

The Celery section will already be present in your admin interface, but you won’t see any data appearing until you start the snapshot camera.

$ ./manage.py celeryctl inspect enable_events
$ ./manage.py celerycam
-- now the django "tasks" section will be populated --


RabbitMQ ships with the rabbitmqctl(1) command, with this you can list
queues, exchanges, bindings, queue lengths, the memory usage of each
queue, as well as manage users, virtual hosts and their permissions.

# ERROR: had a problem with my home setup... I had a celry queue/exchange on vhost "/" 
# instead of vhost "rm3"
$ sudo rabbitmqctl list_queues -p rm3


How do I create AMQP commands to the system? ( w/out writing code)
ampq-tools package
  - /usr/bin/amqp-consume
  - /usr/bin/amqp-declare-queue
  - /usr/bin/amqp-delete-queue
  - /usr/bin/amqp-get
  - /usr/bin/amqp-publish

$ amqp-delete-queue --vhost="/" --username="guest" --password="guest" -q=celery
# This worked...... deleted my celery queue.. ( for vhost "/") but did not resolve my
# situation...turns out I had a permissions problem all along... ( I did not get the ".*"
# correct in this statement... which caused my problems.
$ sudo rabbitmqctl set_permissions -p rm3 rm3 ".*" ".*" ".*"



 ./manage.py celeryd -E --loglevel INFO
./manage.py celerycam
./manage.py celerycam
