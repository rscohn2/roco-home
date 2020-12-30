# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

import logging

import yaml

import signalpy as sp

logger = logging.getLogger(__name__)


class Account(sp.Object):
    """Representation of an account.

    Account is modeled after GitHub account where projects are
    repositories.

    """

    def __init__(self, account_name, account_dict):
        """Construct an account."""
        self.name = account_name
        self.guid = account_dict['guid']
        self.projects = {}

    def load_project(self, file):
        """Load configuration data for a project."""
        try:
            logger.info('load project: %s' % file)
            with open(file, 'r') as stream:
                try:
                    project_dict = yaml.safe_load(stream)
                    project_name = project_dict['name']
                    logger.info(
                        'Loaded project %s: %s' % (project_name, project_dict)
                    )
                    self.projects[project_name] = sp.Project(
                        project_name, project_dict, self
                    )
                    return self.projects[project_name]
                except yaml.YAMLError as exc:
                    logger.error('parsing project file %s: %s' % (file, exc))
                    raise exc
        except OSError as exc:
            logger.error('opening project file: %s: %s' % (file, exc))
            raise exc
