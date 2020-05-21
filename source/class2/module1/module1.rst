Step 3 - Build your first NAP (NGINX App Protect) Docker image
##############################################################

In this module, we will build manually our first NAP Docker image via command line.

**Follow the step below to build the Docker image:**

   #. SSH to Docker App Protect VM
   #. Run the command ``docker build -t app-protect:nosig .`` <-- Be careful, there is a "." (dot) at the end of the command
   #. Wait ...... till you see ``Successfully tagged app-protect:nosig``

   .. note:: This command execute the Dockerfile below

   .. code-block:: bash

      FROM centos:7.4.1708

      COPY entrypoint.sh app-protect-20.zip /root/
      RUN chmod +x /root/entrypoint.sh \
      && yum install epel-release unzip -y \
      && cd /root/ \
      && unzip app-protect-20.zip -d r20 \
      && cd r20 \
      && yum install -y openssl \
      && yum install -y f5* \
      && yum install -y nginx-plus-20*.rpm \
      && yum install -y app-protect-plugin-* \
      && yum install -y app-protect-compiler-* \
      && yum install -y app-protect-engine-* \
      && yum install -y nginx-plus-module-appprotect-* \
      && yum install -y app-protect-20*.rpm

      COPY log-default.json nginx.conf /etc/nginx/

      CMD ["/root/entrypoint.sh"]



**When Docker image is built :**

   1. Check if the Docker image is available locally ``docker images``

   .. image:: ../pictures/module1/docker_images.png
      :align: center

|

   2. Run a container with this image ``docker run -dit --name app-protect -p 80:80 -v /home/ubuntu/nginx.conf:/etc/nginx/nginx.conf app-protect:nosig``
   3. Check that the Docker container is running ``docker ps``

   .. image:: ../pictures/module1/docker_run.png
      :align: center

|

   4. Check the signature package date included in this image (by default) ``docker exec -it app-protect more /var/log/nginx/error.log``


   .. code-block:: bash
      
      2020/05/19 16:59:29 [notice] 12#12: APP_PROTECT { "event": "configuration_load_success", "attack_signatures_package":{"revision_datetime":"2019-07-16T12:21:31Z"},"completed_successfully":true}


**It's time to test your lab**

   #. In Chrome, click on the bookmark ``Arcadia App Protect``
   #. Navigate in the app, and try some attacks like injections or XSS - I let you find the attacks :)
   #. You will be blocked and see the default Blocking page

.. code-block:: html

   The requested URL was rejected. Please consult with your administrator.

   Your support ID is: 14609283746114744748

   [Go Back]

.. note:: Did you notice the blocking page is similar to ASM and Adv. WAF ?

