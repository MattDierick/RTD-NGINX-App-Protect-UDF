Lab 3.3 - Attacks are being mitigated
-------------------------------------

.. note:: **Objective:** Validate Adv. WAF blocks attacks

1. Go to Postman console and open “Post Buy Stocks XSS Attack” in Arcadia collection

.. image:: ../pictures/module3/lab3/Picture1.png
   :align: center
   :scale: 80%

2. Validate the XSS attack in action parameter. Click Send.
Request gets rejected. **Note the Support ID in response**

.. image:: ../pictures/module3/lab3/Picture2.png
   :align: center
   :scale: 80%

.. image:: ../pictures/module3/lab3/Picture3.png
   :align: center
   :scale: 80%


.. warning :: This beta build 15.1 has an issue in UDF. The asmlogd daemon is failing due to lack of threads, hence you don't see any logs in the GUI. This only occurs in UDF at the moment. So you can use an irule to get the ASM logs, or use the REST API calls below.

3. Go to Postman Collection Arcadia-REST-WAF . Open GetEventLog

.. image:: ../pictures/module3/lab3/Picture9.png
   :align: center
   :scale: 80%

4. Replace the Support ID (by the one collected in step 2) in URL and Send Request. Details for blocking is available in the response.

.. image:: ../pictures/module3/lab3/Picture10.png
   :align: center
   :scale: 80%
