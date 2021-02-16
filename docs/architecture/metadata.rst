.. SPDX-FileCopyrightText: 2020 Robert Cohn
..
.. SPDX-License-Identifier: MIT

===================
Persistent Metadata
===================

Persistent metadata is configuration information that is used in the
process of storing or analyzing signal data. It is saved in a database.

Describe hierarchy with {accounts/project/{signal,device/sensor}}

Account
=======

Interface: :ref:`account-api`.

Life Cycle
----------

Create
  Assigned a name

Delete
  Account is removed, including all projects.


Project
=======

Interface: :ref:`project-api`.

A project describes the instrumentation of a building or a system in
the building. It belongs to an Account_, and has a name that is unique
in the account.

Life Cycle
----------

Create
  Assigned a name and an account

Configure
  The mapping between sensor observations and signal data is
  described. Devices are listed. For each device, the sensors are
  listed and the mapping of a sensor to a signal.

Activate
  When a project is activated in a collector, the mappings between
  sensor and signal events are loaded. After activation, when the
  collector receives a sensor event it will store appropriate signal
  events. Sensor events from devices that are not part of an activated
  project return an error.

Deactivate
  Remove sensor/signal mappings in collector.

Move
  Assign a project to another account. All configuration and signal
  data is moved.

Delete
  Project is removed, including configuration and signal data.

Device
======

Interface: :ref:`device-api`.

Life Cycle
----------

Create
  Assigned an access token. Name must be unique in Project_.

Move
  Metadata and signal data is deleted.

Signal
======

Interface: :ref:`signal-api`.

Life Cycle
----------

Create
  Name must be unique in Project_.

Delete
  Metadata and signal data are deleted.
