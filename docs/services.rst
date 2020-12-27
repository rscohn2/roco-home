.. SPDX-FileCopyrightText: 2020 Robert Cohn
..
.. SPDX-License-Identifier: MIT

==========
 Services
==========

The application has 2 services. The collector receives sensor data
from devices, translate it to signals, and stores it in a
database. The analytics service receives requests from the webapp,
retrieves signal data from the database, and responds.

.. toctree::
   :maxdepth: 1

   collector
   analytics
