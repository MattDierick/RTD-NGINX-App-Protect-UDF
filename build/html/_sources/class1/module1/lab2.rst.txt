Lab 1.2 - Reviewing Arcadia application
---------------------------------------

1. Connect to Windows Jumpbox in RDP with the below credentials :

.. image:: ../pictures/module1/RDP.png
   :align: center
   :scale: 40%

.. note :: username is "user" and password is "user"

2. Launch **Chrome** and click on **Arcadia Finance** bookmark

.. image:: ../pictures/module1/Arcadia_homepage.png
   :align: center
   :scale: 40%

3. Click on **Login** button on the top right corner

.. note :: Login as admin / iloveblue

.. image:: ../pictures/module1/Arcadia_login.png
   :align: center
   :scale: 30%

4. Now, we are connected as an Arcadia customer

.. image:: ../pictures/module1/Arcadia_portal.png
   :align: center
   :scale: 20%

.. note :: As you can notice, the application is not fully deployed. 2 parts are missing : le Money Transfer at the bottom and the right banners, and the Refer Friend at the top.

5. The Arcadia App is spread between 4 microservices running in Kubernetes

* Main App
* Back End DB
* Money Transfer - Not yet deployed
* Refer Friend - Not yet deployed

.. image:: ../pictures/module1/microservices.png
   :align: center
   :scale: 25%
