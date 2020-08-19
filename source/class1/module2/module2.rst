Workflow of this lab
####################

The demo is split into 3 classes and 9 steps :

    #. Deploy modern application with modern tools
        #. Deploy and publish Arcadia Finance application in Kubernetes
        #. Publish Arcadia app with an NGNIX Plus Ingress Controller 
    #. Protect Arcadia with NGINX App Protect in Docker
        #. Build your first NAP (NGINX App Protect) docker image
        #. Update this image with the latest WAF signatures
        #. Check logs in Kibana
        #. Customize the WAF policy
        #. Deploy NAP with a CI/CD a toolchain
    #. Protect Arcadia with NGINX App Protect in Linux host
        #. Install the NGINX Plus and App Protect packages manually
        #. Deploy App Protect via CI/CD pipeline

|

Step 1 - Deploy and publish Arcadia Finance application in Kubernetes
*********************************************************************

.. note :: Goal is to deploy Arcadia Application in Kubernetes

Tasks:

    #. Run a Kubernetes command (kubectl) that will download Arcadia containers from an external public repo (Gitlab.com), and run them
    #. Check in Kubernetes Dashboard if Arcadia is deployed and runnning

|

Step 2 - Publish Arcadia app with a NGINX Plus Ingress Controller
*****************************************************************

.. note :: Goal is to publish Arcadia application outside the Kubernetes cluster and use NGINX Plus Ingress Controller for that

Tasks:

    #. Run a Kubernetes command (kubectl) that will download and run an NGINX Plus Ingress Controller image from a private repo (Gitlab.com)
    #. Check how this NIC (NGINX Ingress Controller) is set in order to route packets to the right Arcadia container (pod)

|

Step 3 - Build your first NAP (NGINX App Protect) docker image
**************************************************************

.. note :: Goal is to build your first NAP docker image and run it

Tasks:

    #. Run a docker build command using a Dockerfile
    #. Run a docker run command to start this docker container in front of Arcadia application
    #. Check the signature package included in this image
    #. Check that Aracadia is protected

|

Step 4 - Update this image with the latest WAF signature
********************************************************

.. note :: Goal is to create a new NAP image with the latest Signature package.

Task:

    #. Run the same Docker build command but with a new Dockerfile containing the new repo with the signatures
    #. Destroy the previous NAP container and run a new one from this new image
    #. Check the signature date

|

Step 5 - Update the Docker image with the Threat Campaign package
*****************************************************************

.. note :: Goal is to create a new NAP image with the latest Threat Campaign package ruleset.

Task:

    #. Run the same Docker build command but with a new Dockerfile containing the new package to install
    #. Destroy the previous NAP container and run a new one from this new image
    #. Check the Threat Campaign ruleset date

|

Step 6 - Check logs in Kibana
*****************************

.. note :: Goal is to check logs in ELK (Elastic, Logstash, Kibana)

Task:

    #. Connect to Kibana and check logs

|

Step 7 - Customize the WAF policy
*********************************

.. note :: Goal is to customize the WAF policy in front of Arcadia application. By default, a base policy is deployed.

Task:

    #. Run NAP container with a new nginx.conf file refering to the new policies

|

Step 8 - Deploy NAP with a CI/CD toolchain
******************************************

.. note :: Goal is to deploy NAP in a real environment with a CI/CD toolchain in place.

Task:

    #. Upload a new signature package into the local repo (gitlab) 
    #. GitLab webhook to trigger a Jenkins Pipeline building a new version of the NAP image with this new signature package
    #. Deploy and run this new version of the NAP image in front of Arcadia
    #. Check the signature package date

|

Step 9 - Install the NGINX Plus and App Protect packages manually
*****************************************************************

.. note :: Goal is to deploy NAP and NGINX Plus in a CentOS linux host.

Task:

    #. Install NGINX Plus r20
    #. Install NGINX App Protect
    #. Install NGINX App Protect Signature Package

|

Step 10 - Deploy App Protect via CI/CD pipeline
***********************************************

.. note :: Goal is to deploy NAP by using a CI/CD pipeline with automation toolchain packages provided by F5.

Task:

    #. Use CI/CD toolchain in order to deploy NAP automatically with the latest signature package.

Step 11 - Deploy a new version of the NGINX Plus Ingress Controller
*******************************************************************

.. note :: Goal is to deploy NAP in the Kubernetes Ingress Controller. Since NAP v1.3, NAP can be deployed in a KIC with NGINX+

Task:

    #. Pull NGINX+ KIC image from my private Gitlab repo
    #. Deploy a new Ingress configuration with NAP annotations and configuration