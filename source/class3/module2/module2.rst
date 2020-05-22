Step 9 - Deploy App Protect via CICD pipeline
#############################################

In this module, we will install NGINX Plus and App Protect packages on CentOS with a CICD toolchain. NGINX teams created Ansible modules to deploy it easily in few seconds.

.. note:: The official Ansible NAP module is available here https://github.com/nginxinc/ansible-role-nginx-app-protect

Steps:

    #. Uninstall the NAP, in order to start from scratch

        .. code-block:: bash

            sudo cp -a /etc/nginx /etc/nginx-plus-backup
            sudo cp -a /var/log/nginx /var/log/nginx-plus-backup


