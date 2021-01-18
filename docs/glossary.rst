.. SPDX-FileCopyrightText: 2020 Robert Cohn
..
.. SPDX-License-Identifier: MIT

==========
 Glossary
==========

.. glossary::

   agent
     Client for a service. Examples include a :term:`device` or a web
     application.

   analyzer
     Service that receives requests from a web application and
     provides information about events.

   collector
     Service that receives events from a :term:`device` and saves it
     in persistent storage for offline analysis and visualization.

   device
     Network connected object that manages sensors.

   event
     Change in state of a :term:`signal`.

   GUID
     Globally unique identifier. Used internally to name
     :term:`resources`.

   project
     Collection of signals that are to be measured and devices that
     measure them.

   resources
     Persistent objects managed by ``signalpy``. Examples include:
     :term:`project` and :term:`device`.

   sensor
     Instrument that measures a :term:`signal`. Examples include:
     DS18B20, or GPIO.

   signal
     A time varying measurement of an object in the project. Examples
     include: oil burner activated, room temperature.

   token
     Random string used to authenticate an :term:`agent`.
