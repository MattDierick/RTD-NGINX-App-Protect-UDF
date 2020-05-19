Step 1 - DevOps deploy Arcadia Application
##########################################

In this module, we will deploy the 2 main containers for Arcadia Bank application and we will publish them.

.. note :: At the end of this module, Arcadia Bank application will look like this.


.. image:: ../pictures/MainApp.png
   :align: center
   :scale: 15%


.. warning :: Please keep case senstive for all objects below

#. Application name : app_webapp
#. Components:

   #. cp_mainapp:

      #. Ingress URI: http://www.arcadia-finance.io/
      #. Workload: wl_mainapp

         #. URI: http://mainapp.nginx-udf.internal:30511
   
   #. cp_back:

      #. Ingress URI: http://www.arcadia-finance.io/files/
      #. Workload: wl_backend
      
         #. URI: http://backend.nginx-udf.internal:31584  

|

Video of this module :

.. raw :: html

    <div style="text-align: center; margin-bottom: 2em;">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/GPqtasD4DBM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

.. toctree::
   :maxdepth: 1
   :glob:

   lab*
