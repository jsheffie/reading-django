Installing RabbitMQ 

Initiallly followed this guide:
http://mathematism.com/2010/02/16/message-queues-django-and-celery-quick-start/
-- Note: This guide was written with just plain celery, I am going to
convert this example to use the django-celery module with this

$ sudo rabbitmqctl add_user rm3 password
$ sudo rabbitmqctl list_users
$ sudo rabbitmqctl add_vhost rm3
$ sudo rabbitmqctl set_permissions -p rm3 rm3 password ".*"
$ sudo rabbitmqctl set_permissions -p rm3 rm3 "" ".*"
$ sudo rabbitmqctl set_permissions -p rm3 rm3 "" ".*" ".*"



Ubuntu:
Installed rabbitmq-server

RedHat:

