==========
 ROCOHOME
==========

.. image:: https://github.com/rscohn2/roco-home/workflows/.github/workflows/checks.yml/badge.svg
   :target: https://github.com/rscohn2/roco-home/actions

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

Testing
=======

To test::

  pytest

  pytest --log-cli-level=INFO tests/test_observations.py
