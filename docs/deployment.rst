.. SPDX-FileCopyrightText: 2020 Robert Cohn
..
.. SPDX-License-Identifier: MIT

============
 Deployment
============

The infrastructure consists of devices, web servers that implement the
collector and analytics services, a database to store signal data, and
a web server for static HTML that hosts the web app.

The web servers and database are hosted in Azure. They are configured
in the Azure portal. They are part of the signalpy resources group and
hosted in US East 2, using the free tier. Code is deployed to the web
servers by github actions. Commits to the publish-collector branch
trigger a deploy of the collector, commits to the publish-analytics
branch triggers a deploy of the analytics service. See
.github/workflows/ci.yml for details. Azure credentials are stored as
github secrets in the signalpy github organization settings. They come
from the overview page for each webapp.
