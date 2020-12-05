.. SPDX-FileCopyrightText: 2020 Robert Cohn
..
.. SPDX-License-Identifier: MIT

==========
 ROCOHOME
==========

.. image:: https://github.com/rscohn2/roco-home/workflows/.github/workflows/checks.yml/badge.svg
           :target: https://github.com/rscohn2/roco-home/actions

.. image:: https://readthedocs.org/projects/roco-home/badge/?version=latest
           :target: https://roco-home.readthedocs.io/en/latest/?badge=latest
           :alt: Documentation Status

.. image:: https://api.reuse.software/badge/github.com/rscohn2/roco-home
          :target: https://api.reuse.software/info/github.com/rscohn2/roco-home
          :alt: REUSE status

Code for managing smart home.

CLI
===

roco-home is a CLI for managing the backend.

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
