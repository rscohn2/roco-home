.. SPDX-FileCopyrightText: 2020 Robert Cohn
..
.. SPDX-License-Identifier: MIT

=======
Sensepy
=======

.. image:: https://github.com/rscohn2/sensepy/workflows/.github/workflows/checks.yml/badge.svg
           :target: https://github.com/rscohn2/sensepy/actions

.. image:: https://readthedocs.org/projects/sensepy/badge/?version=latest
           :target: https://sensepy.readthedocs.io/en/latest/?badge=latest
           :alt: Documentation Status

.. image:: https://api.reuse.software/badge/github.com/rscohn2/sensepy
          :target: https://api.reuse.software/info/github.com/rscohn2/sensepy
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
