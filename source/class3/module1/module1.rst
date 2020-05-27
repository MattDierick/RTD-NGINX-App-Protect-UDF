Step 8 - Install the NGINX Plus and App Protect packages manually
#################################################################

In this module, we will manually install the NGINX Plus and NGINX App Protect modules in CentOS from the official repository.

.. warning:: NGINX Plus private key and cert are already installed on the CentOS. Don't share them.

Steps:

    #. SSH to the App Protect in CentOS VM

    #. Add NGINX Plus repository by downloading the file ``nginx-plus-7.repo`` to ``/etc/yum.repos.d``:

        .. code-block:: bash

            sudo wget -P /etc/yum.repos.d https://cs.nginx.com/static/files/nginx-plus-7.repo

    #. Install the most recent version of the NGINX Plus App Protect package (which includes NGINX Plus):

        .. code-block:: bash

            sudo yum install -y app-protect

    #. Check the NGINX binary version to ensure that you have NGINX Plus installed correctly:

        .. code-block:: bash

            sudo nginx -v

    #. Configure the ``nginx.conf`` file. Rename the existing ``nginx.conf`` to ``nginx.conf.old`` and create a new one.

        .. code-block:: bash

            cd /etc/nginx/
            sudo mv nginx.conf nginx.conf.old
            sudo vi nginx.conf

        Paste the below configuration into ``nginx.conf`` and save it

        .. code-block:: bash

            user  nginx;
            worker_processes  auto;

            error_log  /var/log/nginx/error.log notice;
            pid        /var/run/nginx.pid;

            load_module modules/ngx_http_app_protect_module.so;

            events {
                worker_connections  1024;
            }

            http {
                include          /etc/nginx/mime.types;
                default_type  application/octet-stream;
                sendfile        on;
                keepalive_timeout  65;

                log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                                '$status $body_bytes_sent "$http_referer" '
                                '"$http_user_agent" "$http_x_forwarded_for"';

                access_log  /var/log/nginx/access.log  main;

                server {
                listen       80;
                    server_name  localhost;
                    proxy_http_version 1.1;

                    app_protect_enable on;
                    app_protect_policy_file "/etc/nginx/NginxDefaultPolicy.json";
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
        
    #. Create a log configuration file ``log_default.json`` (still in ``/etc/nginx/``)

        .. code-block:: bash

            sudo vi log-default.json

        Paste the configuration below into ``log-default.json`` and save it

        .. code-block:: json

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


    #.  Temporarily disable SELinux globally (https://www.nginx.com/blog/using-nginx-plus-with-selinux).

        .. code-block:: bash

            sudo setenforce 0

    #. Start the NGINX service:

        .. code-block:: bash

            sudo systemctl start nginx

    #. Check everything is running 

        .. code-block:: bash

            less /var/log/nginx/error.log

        .. code-block:: console

            2020/05/22 09:13:20 [notice] 6195#6195: APP_PROTECT { "event": "configuration_load_start", "configSetFile": "/opt/app_protect/config/config_set.json" }
            2020/05/22 09:13:20 [notice] 6195#6195: APP_PROTECT policy 'app_protect_default_policy' from: /etc/nginx/NginxDefaultPolicy.json compiled successfully
            2020/05/22 09:13:20 [notice] 6195#6195: APP_PROTECT { "event": "configuration_load_success", "software_version": "2.52.1", "attack_signatures_package":{"revision_datetime":"2019-07-16T12:21:31Z"},"completed_successfully":true}
            2020/05/22 09:13:20 [notice] 6195#6195: using the "epoll" event method
            2020/05/22 09:13:20 [notice] 6195#6195: nginx/1.17.9 (nginx-plus-r21)
            2020/05/22 09:13:20 [notice] 6195#6195: built by gcc 4.8.5 20150623 (Red Hat 4.8.5-39) (GCC)
            2020/05/22 09:13:20 [notice] 6195#6195: OS: Linux 3.10.0-1127.8.2.el7.x86_64
            2020/05/22 09:13:20 [notice] 6195#6195: getrlimit(RLIMIT_NOFILE): 1024:4096
            2020/05/22 09:13:20 [notice] 6203#6203: start worker processes
            2020/05/22 09:13:20 [notice] 6203#6203: start worker process 6205
            2020/05/22 09:13:26 [notice] 6205#6205: APP_PROTECT { "event": "waf_connected", "enforcer_thread_id": 0, "worker_pid": 6205, "mode": "operational", "mode_changed": false}


.. note:: Congrats, now your CentOS instance is protecting the Arcadia application

.. note:: You may notice we used exactly the same ``log-default.json`` and ``nginx.conf`` files as in the Docker lab.


**Now, try in the Jumphost**

Steps:

    #. RDP to the Jumphost with credentials ``user:user``

    #. Open Chrome and click ``Arcadia NAP CentOS``

    #. Run the same tests as the Docker lab and check the logs in Kibana


**Last step is to install the latest Signature Package**

Steps:

    #. To add NGINX Plus App Protect signatures repository, download the file app-protect-signatures-7.repo to /etc/yum.repos.d:

        .. code-block:: bash
            
            sudo wget -P /etc/yum.repos.d https://cs.nginx.com/static/files/app-protect-signatures-7.repo

    #. Update attack signatures:

        .. code-block:: bash

            sudo yum install -y app-protect-attack-signatures

        To install a specific version, list the available versions:

        .. code-block:: bash

            sudo yum --showduplicates list app-protect-attack-signatures

        To upgrade to a specific version:

        .. code-block:: bash

            sudo yum install -y app-protect-attack-signatures-2020.04.30

        To downgrade to a specific version:

        .. code-block:: bash

            sudo yum downgrade app-protect-attack-signatures-2019.07.16

    #. Restart NGINX process to apply the new signatures:

        .. code-block:: bash

            sudo systemctl restart nginx

    #. Check the **new** signatures package date:

        .. code-block:: bash

            less /var/log/nginx/error.log

.. note:: Upgrading App Protect does not install new Attack Signatures. You will get the same Attack Signature release after upgrading App Protect. If you want to also upgrade the Attack Signatures, you will have to explicitly update them by the respective command above.


.. raw:: html

    <div style="text-align: center; margin-bottom: 2em;">
    <iframe width="1120" height="630" src="https://www.youtube.com/embed/xVmxWOeJ5Cc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
