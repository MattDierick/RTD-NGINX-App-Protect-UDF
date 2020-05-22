Step 9 - Deploy App Protect via CI/CD pipeline
##############################################

In this module, we will install NGINX Plus and App Protect packages on CentOS with a CICD toolchain. NGINX teams created Ansible modules to deploy it easily in few seconds.

.. note:: The official Ansible NAP module is available here https://github.com/nginxinc/ansible-role-nginx-app-protect

**Uninstall the previous runnig NAP**

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

            sudo rm -rf /etc/nginx
            sudo rm -rf /var/log/nginx

**Run the CI/CD pipeline from Jenkins**

Steps:

    #. RDP to the Jumphost with credentials ``user:user``

    #. Open ``Chrome`` and open ``Jenkins`` (if not already opened)

    #. Select the pipeline ``deploy-nap-centos`` and run it


    .. image:: ../pictures/module2/pipeline.png
       :align: center
       :scale: 50%


The pipeline is as below:

.. code-block:: groovy

    node {
    stage 'Checkout'
         // // Get some code from a GitHub repository
        git url: 'http://10.1.20.4/nginx-app-protect/ansible_deploy.git'
        sh 'ansible-galaxy install -r requirements.yml'
   
    stage name: 'Deploy NGINX Plus', concurrency: 1
            dir("${env.WORKSPACE}"){
            ansiblePlaybook inventory: 'hosts', playbook: 'install-nginx-plus.yml'
            }

    stage name: 'Deploy NAP', concurrency: 1
            dir("${env.WORKSPACE}"){
            ansiblePlaybook inventory: 'hosts', playbook: 'app-protect.yml'
            }
            
    stage name: 'Workaround resolver', concurrency: 1
            dir("${env.WORKSPACE}"){
            ansiblePlaybook inventory: 'hosts', playbook: 'copy-nginx-conf.yml'
            }
    
}

.. note:: This pipeline executes 3 Ansible playbooks. 
    
    #. One playbook to install NGINX Plus
    #. one playbook to install NAP
    #. The last playbook is just there to fix an issue in UDF for the DNS resolver.


.. image:: ../pictures/module2/pipeline-ok.png
   :align: center


When pipeline is finished to execute, make a test with ``Chrome`` and the bookmark ``Arcadia NAP Docker``


.. note :: Congrats, you deployed NGINX Plus and NAP with a CI/CD pipeline. You can check the pipelines in the GitLab if you are interested to see what has been coded behind the scene. But it is straight forward as Ansible modules are provided by F5/NGINX.
