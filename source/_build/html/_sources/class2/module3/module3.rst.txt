Step 5 - Check logs in Kibana
#############################

In this module, we will check the logs in ELK (Elastic, Logstash, Kibana)

**Check how logs are sent and how to set the destination syslog server**

Steps:

   #. SSH to Docker App-Protect VM
   #. In ``/home/ubuntu`` (the default home folder), list the files ``ls -al``
   #. You can see 2 files ``log-default.json`` and ``nginx.conf``
   #. Open log-default.json ``less log-default.json``. You will notice we log all requests.

      .. code-block:: JSON

         {
         "filter": {
            "request_type": "all"
               },
         "content": {
            "format": "default",
            "max_request_size": "any",
            "max_message_size": "5k"
               }
         }

   #. Open nginx.conf ``less nginx.conf``

      .. code-block:: bash

         user nginx;

         worker_processes 1;
         load_module modules/ngx_http_app_protect_module.so;

         error_log /var/log/nginx/error.log debug;

         events {
            worker_connections  1024;
         }

         http {
            include       /etc/nginx/mime.types;
            default_type  application/octet-stream;
            sendfile        on;
            keepalive_timeout  65;

            server {
               listen       80;
               server_name  localhost;
               proxy_http_version 1.1;

               app_protect_enable on;
               app_protect_security_log_enable on;
               app_protect_security_log "/etc/nginx/log-default.json" syslog:server=10.1.20.6:5144;

               location / {
                     resolver 10.1.1.9;
                     resolver_timeout 5s;
                     client_max_body_size 0;
                     default_type text/html;
                     proxy_pass http://k8s.arcadia-finance.io:30274$request_uri;
               }
            }
         }


.. note:: You will notice in the ``nginx.conf`` file the refererence to ``log-default.json`` and the remote syslog server (ELK) ``10.1.20.6:5144``


**Open Kibana in the Jumphost or via UDF access**

Steps:

   #. In UDF, search ELK VM and click Access > ELK

      .. image:: ../pictures/module3/ELK_access.png
         :align: center
         :scale: 50%

|

   #. In Kibana, click on ``Dashboard > Overview```

      .. image:: ../pictures/module3/ELK_dashboard.png
         :align: center
         :scale: 50%

|

   #. At the bottom of the dashboard, you can see the logs. Select one logs and check the content

.. note:: You may notice the log content is similar to ASM and Adv. WAF
