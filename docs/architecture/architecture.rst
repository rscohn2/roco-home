.. SPDX-FileCopyrightText: 2020 Robert Cohn
..
.. SPDX-License-Identifier: MIT

============
Architecture
============

Application Architecture
========================

.. figure:: /images/application-architecture.png

   Application Architecture

Common architecture
===================

.. toctree::
   :maxdepth: 1

   auth
   metadata

Collector
=========

The Collector receives events from a :term:`device` and saves it in
persistent storage for offline analysis and visualization. It is
implemented as a service with a REST API and connects to a database.

In a typical flow, a device performs a post operation to the collector
with the sensor event payload. The collector authenticates the device,
validates the payload, maps the sensor event to one or more signal
events, records the signal events in storage, and returns a status to
the device.

The device provides a :term:`token` in the payload for
authentication. Tokens are used as keys in a dictionary where the
value is the device.

A collector manages the requests for one or more projects. At startup,
the collector loads the configuration of all the projects it
manages. The configuration includes the signals, devices, and the
mapping from sensor events to signal events.


Analyzer
========

The Analyzer receives requests from a web application and provides
information about events derived from persistent storage. It is
implemented as a service with a REST API and connects to a database.


Storage
=======

Storage saves persistent data, including signal events and
projects. It is implemented with a network-connected database such as
MongoDB or in files.
