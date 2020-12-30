.. SPDX-FileCopyrightText: 2020 Robert Cohn
..
.. SPDX-License-Identifier: MIT

.. _development-workflows:

=======================
 Development Workflows
=======================

Tools
=====

======================  ====
Function                Tool
======================  ====
Continuous integration  `GitHub actions`_
Testing                 pytest_
Documentation           sphinx_ & plugins
Commit test management  `pre-commit`_
Python code formatting  black_
License compliance      reuse_
Documentation hosting   readthedocs_
Drawings                `draw.io`_
======================  ====

.. _`draw.io`: https://draw.io
.. _`GitHub actions`: https://docs.github.com/en/free-pro-team@latest/actions
.. _pytest: https://docs.pytest.org/en/stable/
.. _sphinx: https://www.sphinx-doc.org/en/master/
.. _`pre-commit`: https://www.sphinx-doc.org/en/master/
.. _black: https://github.com/psf/black
.. _reuse: https://reuse.software/dev/#tool
.. _readthedocs: https://readthedocs.org/

Python setup
============

Create a virtual environment::

  python -m venv signalpy-venv
  source signalpy-venv/bin/activate

Install editable signalpy into the environment with all tools needed
for development::

  pip install ./packages/.[dev,docs]

Testing
=======

Run all the tests::

  pytest tests

Run tests with maximum debug logging::

  pytest --log-cli-level=INFO tests

For selective testing specify a test, file, or directory::

  pytest tests/core/test_account.py:test_signal_lookup


Pre-commit testing
==================

Before commit, add all your files and run the same tests as CI::

  git status
  git add .
  pre-commit run --all

Some of the checks fix the problems. Add the fixes to the commit and
run that test selectively::

  git add .
  pre-commit run --all flake8

Run all tests again::

  pre-commit run --all

Next, manually fix the issues. Run the tests selectively to iterate
on fixes::

  pre-commit run --all doc8

When you think you are done, run everything one more time::

  pre-commit run --all

Documentation
=============

To build the documentation::

  cd docs
  make html

Webapp Deployment
=================

Deploy form CI
--------------

CI deploys the collector and analyzer webapp on commits to the
publish-collector and publish-analyzer branches, respectively. A
typical deployment starts with a commit to the main branch::

  git commit -m 'some webapp update'

When ready to deploy a new collector to production, merge all changes
from main::

  git checkout main
  git pull
  git checkout publish-collector
  git merge main
  git push

It is possible to skip committing to main to speed up making small
changes::

  git checkout publish-collector
  # edit some files
  git add .
  git commit -m 'update collector'
  git push

When you are done, merge back into main::

  git checkout main
  git merge publish-collector
  git push

Deploy local directories
------------------------

If you are debugging CI deployment issues, it can be faster to deploy
directly from the local file system. This procedure is not appropriate
for production because you will not have a record of the code you
deployed and therefore may not be able to reproduce it later.

For initial setup, copy the python packages so deployment includes
them, every time you update::

  cd app/backend/collector
  cp ../.././packages .

To see all the webbapps::

  az webapp list

Then look for ``"name":`` (always needed) and ``"resourceGroup":``
(sometimes needed). Then deploy from the current directory::

  az webapp up --runtime 'python|3.8' --name <name>

``az`` writes a ``.azure/config`` to the directory so future
deployments only need::

  az webapp up --runtime 'python|3.8'

Troubleshooting
---------------

In the Azure portal, select the web app that is failing and pick "Log
stream" in the column on the left. This will show you the URL that has
the log, and the tail of that log. When you see a problem, visit the
URL of the full log.
