Lab 3.2 - Declaratively create a WAF Policy using Swagger file
--------------------------------------------------------------

.. note:: **Objective:** Import Swagger file and Create Security Policies 

.. warning :: In this lab, you will **NOT** use the new "declarative WAF API". You will use the already existing capability to import a Swagger file (v3 in 15.1), and then create a policy, from an **API call** and **NOT** from a **declarative call**. TMOS binary and documentation of the declarative WAF API was not ready in time for ISC lab building.

1. Open Postman by clicking on shortcut or Clicking
the icon on Quick launch toolbar

.. image:: ../pictures/module3/lab2/Picture1.png
   :align: center
   :scale: 80%

2. Collection Name: Arcadia-REST-WAF. Double Click Upload Swagger

.. image:: ../pictures/module3/lab2/Picture2.png
   :align: center
   :scale: 50%

3. Ensure proper credentials
are provided

.. image:: ../pictures/module3/lab2/Picture3.png
   :align: center
   :scale: 80%

4. Ensure the following headers
are set

.. image:: ../pictures/module3/lab2/Picture4.png
   :align: center
   :scale: 80%

5. Ensure the following
body is set

.. image:: ../pictures/module3/lab2/Picture5.png
   :align: center
   :scale: 80%

6. Locate Swagger file (swagger_arcadia.yaml)
for Arcadia in Downloads folder

.. image:: ../pictures/module3/lab2/Picture6.png
   :align: center
   :scale: 80%

7. Click Send to upload
swagger file

.. image:: ../pictures/module3/lab2/Picture7.png
   :align: center
   :scale: 80%

8. Swagger file is
uploaded

.. image:: ../pictures/module3/lab2/Picture8.png
   :align: center
   :scale: 80%

9. Validate by checking the directory  /ts/var/rest.
There will be a file named admin~openapi_arcadia1.yaml

.. image:: ../pictures/module3/lab2/Picture9.png
   :align: center
   :scale: 80%

10. On the postman collection, open Postman call named “Import Swagger”.
Validate authentication credentials

.. image:: ../pictures/module3/lab2/Picture10.png
   :align: center
   :scale: 80%

11. Validate
Headers

.. image:: ../pictures/module3/lab2/Picture11.png
   :align: center
   :scale: 80%

12. Validate the Body has the following JSON.
Click Send

.. image:: ../pictures/module3/lab2/Picture12.png
   :align: center
   :scale: 80%

13. It should show the
following response.

.. image:: ../pictures/module3/lab2/Picture13.png
   :align: center
   :scale: 80%

14. Validate the status of policy creation,
by running CheckImportStatus REST call

.. image:: ../pictures/module3/lab2/Picture14.png
   :align: center
   :scale: 80%

15. On successful completion,
we should see status “ COMPLETED”

.. image:: ../pictures/module3/lab2/Picture15.png
   :align: center
   :scale: 80%

16. Open Postman REST call
RetrieveASMPolicies. Click Send

.. image:: ../pictures/module3/lab2/Picture16.png
   :align: center
   :scale: 80%

17. Find the policy from the list for arcadia_policy.
Check out the link for policy, to get policy hash.
This will be used in the next steps. The hash should be **OlIA0JHg0YuTH1LW4KgaSw**

.. image:: ../pictures/module3/lab2/Picture17.png
   :align: center
   :scale: 80%

18. Open postman REST call AttachPolicyToVS.
Ensure the URL has the correct Policy Hash. Click Send to submite Request

.. image:: ../pictures/module3/lab2/Picture18.png
   :align: center
   :scale: 80%

19. Server returns 200
and Policy is patched

.. image:: ../pictures/module3/lab2/Picture19.png
   :align: center
   :scale: 80%

20. Log in to BIGIP Application Security> Security Policy > Policy List.
There should be a policy name arcadia_policy

.. image:: ../pictures/module3/lab2/Picture20.png
   :align: center
   :scale: 60%

21. To block attacks, move the attack signatures from staging to blocking mode.
Click arcadia_policy

22. Click on
Attack Signatures

.. image:: ../pictures/module3/lab2/Picture22.png
   :align: center
   :scale: 80%

23. Click Enforce>
Enforce all Staged Signatures

.. image:: ../pictures/module3/lab2/Picture23.png
   :align: center
   :scale: 80%

24. Click
Apply Policy

.. image:: ../pictures/module3/lab2/Picture24.png
   :align: center
   :scale: 80%