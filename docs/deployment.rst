.. SPDX-FileCopyrightText: 2020 Robert Cohn
..
.. SPDX-License-Identifier: MIT

============
 Deployment
============

The infrastructure consists of devices, web servers that implement the
collector and analytics services, a database to store signal data, and
a web server for static HTML that hosts the web app.

Deployment is triggered by pushing commits to GitHub
repositories. After successful testing, new code and contents are
deployed. Local testing and manual deployment are covered in
:ref:`development-workflows`.

Providers
=========

We use the following providers and services.

===================  =================
Function             Service
===================  =================
Collector            Azure App Service
Analyzer             Azure App Service
Store                Azure Cosmos DB
Static HTML hosting  GitHub Pages
Deployment           GitHub Actions
===================  =================

We chose Azure because the combination of free services was the best
match for our application. GitHub Pages and Actions are also free and
integrate with the source code management.

Azure Setup
===========

Create an account in Azure. Pay as you go subscription. A subscription
determines how it is billed. Create a resource group called signalpy
to hold everything. A resource group is merely a grouping of Azure
resources (services).

GitHub Setup
============

We created a ``signalpy`` organization that hosts a ``signalpy``
repository. You currently only need a single repository.

Initial Creation of the App Services on Azure
=============================================

We describe the deployment of the collector and analyzer together
because they are very similar. The collector and analyzer are API
services, implemented as a Flask application. The are deployed using
GitHub Actions on Azure App Service.

In the Azure portal, create 2 App services, ``signalypy-collector``
and ``signalpy-analyzer``, with the following characteristics:

================  ==========
Option            Value
================  ==========
Resource Group    signalpy
Publish as        code
Runtime           python 3.8
Operating System  Linux
Region            East US 2
================  ==========

It should automatically select the Linux Plan, and the SKU (Free F1).

Open the newly created App Service. Under *Settings*, select
*Configuration*. Under *Application Settings*, add a new application
setting.

==============================  =====
Name                            Value
==============================  =====
SCM_DO_BUILD_DURING_DEPLOYMENT  true
WEBSITE_WEBDEPLOY_USE_SCM       true
==============================  =====

Do not check *Deployment slot setting*.

Initial Setup for App Service Code Deployment on GitHub
=======================================================

You have created the App Services, now you need to deploy code to
them.  Commits to the publish-collector branch trigger a deploy of the
collector, commits to the publish-analytics branch triggers a deploy
of the analytics service. See ``.github/workflows/ci.yml`` for
details. Azure credentials are stored as GitHub secrets in the
signalpy GitHub organization settings.

Visit *Settings* for the signalpy organization on GitHub. Select
*Secrets*, then *New organization secret*. Create 2 secrets with the
following names: ``AZURE_WEBAPP_PUBLISH_PROFILE_ANALYZER`` and
``AZURE_WEBAPP_PUBLISH_PROFILE_COLLECTOR``. These names must match the
names in ``.github/workflows/ci.yml``. For the values, visit the App
Service in Azure portal. Select *Overview* in the left hand column,
and then *Get publish profile*. After the file downloads, open and
copy the contents into the appropriate secret.

App Service deployment
======================

App Service deployment is automatic, here is what happens. The
`webapps-deploy`_ action in ``ci.yml`` uses the Azure CLI to create a
zip file of the service and copy it to Azure. Deployment builds the
application by doing a::

  pip install -r requirements.txt

And then it launches the service, expecting there is a Flask app with
the the name ``app`` in ``app.py``.

.. _`webapps-deploy`: https://github.com/Azure/webapps-deploy

We need the signalpy python packages included in the deployment, so
``ci.yml`` copies them to the root of the deployment directories.
