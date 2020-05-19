Lab 1.1 - Reviewing architecture network diagram
------------------------------------------------

.. note :: It is important to understand the full architecture and the network architecture, in order to use the right IP addresses and ports.

- The microservices are running in Kubernetes in 4 differents Pods
- Each microservice is published by a KubeProxy on 4 different ports
- NGNIX+ API Gateways are running in docker. External port 8443 and internal port 443

.. image:: ../pictures/module1/diagram.png
   :align: center
   :scale: 20%
