.. SPDX-FileCopyrightText: 2020 Robert Cohn
..
.. SPDX-License-Identifier: MIT

========
Signalpy
========

.. image:: https://github.com/signalpy/signalpy/workflows/.github/workflows/ci.yml/badge.svg
           :target: https://github.com/signalpy/signalpy/actions

.. image:: https://readthedocs.org/projects/signalpy/badge/?version=latest
           :target: https://signalpy.readthedocs.io/en/latest/?badge=latest
           :alt: Documentation Status

.. image:: https://api.reuse.software/badge/github.com/signalpy/signalpy
          :target: https://api.reuse.software/info/github.com/signalpy/signalpy
          :alt: REUSE status

Code for managing sensors

CLI
===

sensecli is a CLI for managing the backend.

Prerequisites
=============

To use the CLI::

  pip install -e .

For development::

  pip install -e .[dev]

For docs::

  pip install -e .[docs]

Testing
=======

To test::

  pytest

  pytest --log-cli-level=INFO tests/test_observations.py
