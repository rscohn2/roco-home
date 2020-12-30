.. SPDX-FileCopyrightText: 2020 Robert Cohn
..
.. SPDX-License-Identifier: MIT

=====================
Software Organization
=====================

Repository layout
=================

Starting from the top level:

Application code:

packages
  Python packages.

  signalpy
    Python code that runs on the server and workstation client

app
  An application usually has some main function, and the rest of the
  code is located in packages. These are the minimal main functions.

Support:

tests
  Scripts for pytest
docs
  Documentation
.reuse
  dep5 support with license info
LICENSES
  SPDX licenses

Configuration:

pyproject.toml
  Common configuration for applications. Today only used for black.
.github
  GitHub actions configurations
.gitignore
  project-specific git ignores
readthedocs.ytml
  Configuration for readthedocs_

.. _readthedocs: https://readthedocs.org/
