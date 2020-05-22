Step 9 - Deploy App Protect via CI/CD pipeline
##############################################

In this module, we will install NGINX Plus and App Protect packages on CentOS with a CICD toolchain. NGINX teams created Ansible modules to deploy it easily in few seconds.

.. note:: The official Ansible NAP module is available here https://github.com/nginxinc/ansible-role-nginx-app-protect

Steps:

    #. Uninstall the NAP, in order to start from scratch

        .. code-block:: bash

            cd [Enter]
            sudo yum remove app-protect*

        .. image:: ../pictures/module2/yum-remove-app-protect.png
           :align: center

    #. Uninstall NGINX Plus packages


        .. code-block:: bash

            sudo yum remove nginx-plus*

        .. image:: ../pictures/module2/yum-remove-nginx-plus.png
           :align: center

    #. Delete/rename the last directories

        .. code-block:: bash

            sudo cp -a /etc/nginx /etc/nginx-plus-backup
            sudo cp -a /var/log/nginx /var/log/nginx-plus-backup

    