Step 4 - Update this image with the latest WAF signature
########################################################

In this module, we will update the signature package in the docker image.

.. warning:: There are several ways to update the signatures. All of them have pro and cons. In this lab, I decided to create a new docker image with the new signature package. And then destroy and run a new docker container from this new image in front of Arcadia App.

The signatures are provided by F5 with an RPM package. The best way to update the image is to build a new image from a new Dockerfile refering to this signature package (and change the iamge tag). We will use the Dockerfile below:

.. code-block:: bash

   FROM centos:7.4.1708

   COPY entrypoint.sh app-protect-20.zip app-protect-attack-signatures-* /root/
   RUN chmod +x /root/entrypoint.sh \
   && yum install epel-release unzip -y \
   && cd /root/ \
   && unzip app-protect-20.zip \
   && yum install -y openssl \
   && yum install -y f5* \
   && yum install -y nginx-plus-20*.rpm \
   && yum install -y app-protect-plugin-* \
   && yum install -y app-protect-compiler-* \
   && yum install -y app-protect-engine-* \
   && yum install -y nginx-plus-module-appprotect-* \
   && yum install -y app-protect-20*.rpm \
   && yum install -y app-protect-attack-signatures-*.rpm

   COPY log-default.json nginx.conf /etc/nginx/

   CMD ["/root/entrypoint.sh"]


.. note:: You can notice one more line versus the previous Dockerfile in Step 3. I added the line ``yum install -y app-protect-attack-signatures-*.rpm``


**Follow the step below to build the new docker image:**

   #. SSH to Docker App Protect VM
   #. Run the command ``docker build -t app-protect:20200316 -f Dockerfile-sig .`` <-- Be careful, there is a "." (dot) at the end of the command
   #. Wait ...... till you see ``Successfully tagged app-protect:20200316``

.. note:: Please take a time to understand what we run. You can notice 2 changes. We ran the build with a new Dockerfile ``Dockerfile-sig`` and with a new tag ``20200316`` (date of the signature pacakge)


**Destroy the previous NAP running container and run a new one based on the new image (tag 20200316)**

   1. Check if the docker image is available locally ``docker images``. You can notice the new image with the new tag ``20200316``.

      .. image:: ../pictures/module2/docker_images.png
         :align: center

|

   2. Destroy the existing and runnin NAP container ``docker rm -f app-protect``
   3. Run a new container with this image ``docker run -dit --name app-protect -p 80:80 -v /home/ubuntu/nginx.conf:/etc/nginx/nginx.conf app-protect:20200316``
   4. Check docker is running ``docker ps``

      .. image:: ../pictures/module2/docker_run.png
         :align: center

|

   5. Check the signature package date included in the new docker container ``docker exec -it app-protect more /var/log/nginx/error.log``


   .. code-block:: bash
      
      2020/05/20 09:30:20 [notice] 12#12: APP_PROTECT { "event": "configuration_load_success", "attack_signatures_package":{"revision_datetime":"2020-03-16T14:11:52Z","version":"2020.03.16"},"completed_successfully":true}

.. note:: Congrats, you are running a new version of NAP with an updated signature package.