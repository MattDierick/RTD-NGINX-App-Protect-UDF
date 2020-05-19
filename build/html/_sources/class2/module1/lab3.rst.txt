Lab 1.3 - Reviewing Kubernetes deployments
------------------------------------------

1. Launch Kubernetes Dashboard from UDF

.. image:: ../pictures/module1/K8S_menu.png
   :align: center
   :scale: 40%

2. Review the deployments.
As you can see, the 4 microservices are up and running

.. image:: ../pictures/module1/K8S_microservices.png
   :align: center
   :scale: 20%


3. Review the Services. Each microservice is published through a KubeProxy. Note that the table is not a screen shot - use the table to verify the mappings in the screenshot below.

+------------------+------------+
| Microservice     | Port       |
+==================+============+
| Main App         |   30511    |
+------------------+------------+
| Back End         |   31584    |
+------------------+------------+
| App2             |   30362    | 
+------------------+------------+
| App3             |   31662    |
+------------------+------------+


.. image:: ../pictures/module1/K8S_services.png
   :align: center
   :scale: 30%

