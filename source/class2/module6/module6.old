Step 8 - Deploy NAP with a CI/CD toolchain
##########################################

.. warning :: This module is not up to date, due to changes in signature udpate process in the GA release. In this lab, we will upload manually the signature package. Now, with the GA, this package is available in the public repo. I will update this lab soon accordingly.

In this module, we will deploy deploy NAP with a CI/CD pipeline. NAP is tied to the app, so when DevOps commits a new app (or a new version), the CI/CD pipeline has to deploy a new NAP component in front. In order to avoid repeating what we did previously, we will use a Signature package update as a trigger.

.. note:: When a new signature package is available, the CI/CD pipeline will build a new version of the Docker image and run it in front of Arcadia Application

**This is the workflow we will run**

    #. Upload a new Signature Package in GitLab
    #. Commit this upload in GitLab
    #. This commit triggers a webhook in Jenkins
    #. Jenkins runs the pipeline
        #. Build a new Docker NAP image with a new tag ``date of the signature package``
        #. Destroy the previous running NAP container
        #. Run a new NAP container with this new Signature Package

.. note:: Goal of this module is not to learn how to do it, but understand how I did it.

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

.. note:: The challenge here was to retrieve the date of the package and tag the image with this date in order to have one image per signature package date. This is useful if you need to roll back to a previous version of the signatures.

**Upload a new signature package in GitLab**

Steps:

    #. RDP to the Jumphost and open ``Chrome``
    #. Open 2 tabs ``Dashboard [Jenkins]`` and ``Gitlab``
        #. If Jenkins is not available (502 error), restart the GitLab Docker container. SSH to the GitLab VM and run ``docker restart gitlab`` 
    #. In Jenkins, open ``Update_Docker_Signatures`` pipeline

        .. image:: ../pictures/module6/jenkins_favorite.png
           :align: center
           :scale: 50%
    
    #. In GitLab, open ``NGINX App Protect / signature-update`` project

        .. image:: ../pictures/module6/gitlab_project.png
           :align: center
           :scale: 50%

    #. In the GitLab project, click on the ``+`` icon and ``upload file``

        .. image:: ../pictures/module6/upload_file.png
           :align: center
           :scale: 50%

    #. Select Signature Package file from the Desktop > NGINX Signatures Packages
        #. If you can't click on ``click to upload``, this is a bug in GitLab
        #. Workaround is to simulate the creation of a file. Close this upload window, click on ``+`` icon ``New file``, enter anything in the name and click ``Cancel``
        #. Try to upload the file again, it should work.

    #. Upload the file ``app-protect-attack-signatures-20200421-1.el7.centos.x86_64.rpm`` with the date of April 21st, 2020. Date is in the name of the file


**Trigger the CI/CD pipeline**

Steps :

    #. In GitLab, click on ``Tags`` in the left menu
    #. Create a new tag and give it the name ``Sig-20200421``
    #. Click ``Create tag``
    #. At this moment, the Jenkins pipeline starts (thanks to a webhook between GitLab and Jenkins)
    #. In Chrome on the Jenkins tab, you should see a new ``RUN``, click on it

        .. image:: ../pictures/module6/jenkins_run.png
           :align: center   

    #. Wait for the pipeline to finish. You can click on every task to check the steps

        .. image:: ../pictures/module6/jenkins_pipeline.png
           :align: center 
    
    #. Check if the new image created and pushed by the pipeline is available in the Docker Registry.
        #. In ``Chrome`` open bookmark ``Docker Registry UI``
        #. Click on ``App Protect`` Repository
        #. You can see your new image with the tag ``20200421``

        .. image:: ../pictures/module6/registry-ui.png
           :align: center 

    #. Connect in SSH to the Docker App Protect + Docker repo VM, and check the signature package date running ``docker exec -it app-protect more /var/log/nginx/error.log``.
    
    .. code-block:: bash
       
       2020/05/24 20:49:39 [notice] 12#12: APP_PROTECT { "event": "configuration_load_success", "attack_signatures_package":{"revision_datetime":"2020-04-21T10:43:02Z","version":"2020.04.21"},"completed_successfully":true}


.. note:: Congratulations, you ran a CI/CD pipeline based on a GitLab webhook. This webhook was based on a Signature Package update, but it could have also been associated with an application commit.

**Video of this module (force HD 1080p in the video settings)**

.. raw:: html

    <div style="text-align: center; margin-bottom: 2em;">
    <iframe width="1120" height="630" src="https://www.youtube.com/embed/BQTSf4-iqGo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
