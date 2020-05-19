Lab 2.2 - Add a new microservice in the API definitions
-------------------------------------------------------


1. To verify Upstream configuration, click "Upstream Group",
and then click edit icon for app2

    .. image:: ../pictures/module2/api_lab-01-08.png
        :align: center
        :scale: 60%

.. note :: This App2 is a new app developed by DevOps and available on the FQDN app2.example.com and port 30362. This microservice is running in Kubernetes. Now we need to publish this new microservice on the API Gateway.

2. Add app2 to API definition. Click "API Definitions",
then click the edit icon under "Arcadia WebApp"

.. image:: ../pictures/module2/api_lab-01-09-1.png
    :align: center
    :scale: 40%

.. image:: ../pictures/module2/api_lab-01-09.png
    :align: center
    :scale: 60%

.. note :: You can notice only 2 microservices are published. The / (main App) and the /files (Back End DB)

3. Click "Add Resource", put /api into "Path", then click "Save"

    .. image:: ../pictures/module2/api_lab-01-10.png
        :align: center
        :scale: 60%

4. Click edit icon for "prod WebApp" in "Environment"

.. image:: ../pictures/module2/api_lab-01-11-1.png
    :align: center
    :scale: 40%

5. Click "Add Route". Select /api in "Resource", and app2 in "Upstream Group". Click SAVE.

.. image:: ../pictures/module2/api_lab-01-11.png
    :align: center
    :scale: 60%

6. Click "Publish". A publish successful message will appear at top,
once publish is completed.

    .. image:: ../pictures/module2/api_lab-01-12.png
        :align: center
        :scale: 60%

7. Verify app2 is running in the Web Application. RDP into Windows Jumphost,
and refresh the browser session for the application. The app2 (Quick Money Transfer) appears. Do a money transfer by
selecting an account in “From”, a person in “To”, fill a number in “Amount”, and click “Transfer Now”;
you will see a successful message, and the money transfer transaction will show in “Transfer history”

    .. image:: ../pictures/module2/api_lab-01-13.png

.. note :: You did you first API call from the Arcadia Web Application :) Behind the scene, when you click on Transfer Now, browser makes an API Call.

8. Repeat the same configuration
for Arcadia API

- Go back to API Definition and click on edit icon for "Arcadia API"

    .. image:: ../pictures/module2/api_lab-01-14.png
        :align: center
        :scale: 60%

.. note :: You can notice there is only one Resource at the moment, and this resource is "explicit" with the full URI.

- Click "Add Resource", and put /api in "Path", and click "Save"

    .. image:: ../pictures/module2/api_lab-01-15.png
        :align: center
        :scale: 60%

- Click edit button for "prod API" in Environment, click "Add Route", select /api for resource, select app2 for "Upsteam Group", and click "Save"

    .. image:: ../pictures/module2/api_lab-01-16.png
        :align: center
        :scale: 60%

- Click "Publish", and wait for publishing to complete

.. note :: With these steps, you added a new "route" for the API /api. The API and the Web Application are separated at the BIG-IP level. It is 2 different VS and 2 different Pool. That why you created 2 different API Definitions.

9. Verify API call via Postman. RDP into Windows Jumphost, launch Postman,
open "Arcadia" collection, select "POST Transfer Money". Review the body and click "Send". You should see successful message in response.

    .. image:: ../pictures/module2/api_lab-01-17.png
        :align: center

10. Go back to the Web Application, reload the page, and check if the transaction is shown in the Money Transfer app.

    .. image:: ../pictures/module2/api_lab-01-17-1.png
        :align: center
        :scale: 50%