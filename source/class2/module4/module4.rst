Step 6 - Customize the WAF policy
#################################

In this module, we will deploy a WAF policy to protect Arcadia Bank application and we will publish it.

.. note :: We use the new v15.1 Declarative WAF policy. You can retrieve the JSON Policy in the GitLab repo and below.

.. code-block:: json

    {
        "policy": {
            "name": "policy-fund-1",
            "description": "Policy Example - Rapid Deployment",
            "template": {
                "name": "POLICY_TEMPLATE_RAPID_DEPLOYMENT"
            },
            "enforcementMode": "blocking",
            "server-technologies": [
                {
                    "serverTechnologyName": "MySQL"
                },
                {
                    "serverTechnologyName": "Unix/Linux"
                },
                {
                    "serverTechnologyName": "MongoDB"
                }
            ],
            "signature-settings": {
                "signatureStaging": false
            },
            "policy-builder": {
                "learnOnlyFromNonBotTraffic": false
            }
        }
    }

|

Video of this module :

.. raw :: html

    <div style="text-align: center; margin-bottom: 2em;">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/vKCtsByE9G8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

