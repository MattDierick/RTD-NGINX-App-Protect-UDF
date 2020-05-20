Step 7 - Deploy NAP with a CICD toolchain
#########################################

In this module, we will deploy deploy NAP with a CICD pipeline. NAP is tied to the app, so when DevOps commit a new app (or a new version), the CICD pipeline has to deploy a new NAP in front. In order to avoid to repeat what we did previously, we will use a Signature package update as a trigger.

.. note:: When a new signature package is available, the CICD pipeline will build a new version of the image and run it in front of Arcadia Application

**This is the workflow we will run**

    #. Upload a new Signature Package in GitLab
    #. Commit this upload in GitLab
    #. This commit trigger a webhook with Jenkins
    #. Jenkins runs the pipeline
        #. Build a new docker NAP image with a new tag ``date of the signature package``
        #. Destroy the previous running NAP container
        #. Run a new NAP container with this new Signature Package

.. note:: Goal of this module is not to learn how to do it, but undersatnd how I did it.

**Check the Jenkins file**

.. code-block:: groovy

    node {
    def mvnHome
    stage('Preparation') {
        // Get some code from a GitHub repository
        git 'http://10.1.20.4/nginx-app-protect/signature-update.git'

    }
    stage('Build Docker') {
        withEnv(["MVN_HOME=$mvnHome"]) {
            // Define the remote docker registry
            registry = "10.1.20.7:5000/app-protect"
            // Extract the tag from the date of the Signature Package
            tag = sh (script: 'echo -n app-protect-attack-signatures-* | cut -c 31-38', returnStdout: true).trim()
            echo "${tag}"  
            script {
                // Build the docker image
                docker.build registry + ":${tag}"
            }
    
            
            }
    }
    stage('Push Docker') {
        withEnv(["MVN_HOME=$mvnHome"]) {
            // Push the image into the remote Docker registry
            sh "sudo docker push 10.1.20.7:5000/app-protect:${tag}"
            }
    }
    
        stage name: 'Run Docker', concurrency: 1
                withEnv(["MVN_HOME=$mvnHome"]) {
                    // Run the docker container
                    ansiblePlaybook inventory: 'hosts', 
                    playbook: 'playbook.yaml',
                    extraVars: [dockertag: "${tag}"]
                }
    }

.. note:: The challenge here was to retrieve the date of the package and tag the iamge with this date. In order to have one image per signature package date. Useful if you need to roll back.

**Upload a new signature package in Gitlab**

Steps:

    #. RDP to the Jumphos and open ``Chrome``
    #. Open 2 tabs ``Jenkins`` and ``Gitlab``
        #. If Jenkins is not available (502 error), restart the docker. SSH to Gitlab VM and run ``docker restart gitlab`` 
    #. In Jenkins, open ``Update_Docker_Signature`` pipeline

        .. image:: ../pictures/module5/jenkins_favorite.png
           :align: center
           :scale: 50%
    
    #. In Gitlab, open ``NGINX App Protect / signature-update`` project

        .. image:: ../pictures/module5/gitlab_project.png
           :align: center
           :scale: 50%

    #. In Gitlab project, click on the ``+`` icon and ``upload file``

        .. image:: ../pictures/module5/upload_file.png
           :align: center
           :scale: 50%

    #. Select Signature Package file from the Desktop > NGINX Signature Packages
        #. If you can't click on ``click to upload``, it is a bug Gitlab
        #. Workaround is to simulate the creation of a file. Close this upload windows, click on ``+`` icon ``new file``, enter anything in the name and click ``cancel``
        #. Try to upload file agin, it should work.

    #. Upload the file ``app-protect-attack-signatures-20200421-1.el7.centos.x86_64.rpm`` from date April 21th 2020. Date is in the name of the file


**Trigger the CICD pipeline**

Steps :

    #. In Gitlab, click on ``tags`` in the left menu
    #. Create a new tag and give a name ``Sig-20200421```
    #. Click ``create tag``
    #. At this moment, the Jenkins pipeline starts (thanks ot a webhook between Gitlab and Jenkins)
    #. In Jenkins, you should see a new ``RUN``, click on it

        .. image:: ../pictures/module5/jenkins_run.png
           :align: center   

    #. Wait the pipeline to finish. You can click on every task to check the steps

        .. image:: ../pictures/module5/jenkins_pipeline.png
           :align: center 

    #. Connect back in SSH to App Protect VM, and check the signature package date running ``docker exec -it app-protect more /var/log/nginx/error.log``


.. note:: Congratulations, you ran a CICD pipeline based on a Gitlab webhook. This webhook was based on a Signature Package update, but it can be tied to an application commit for instance.

