# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

from setuptools import setup

requirements = [
    'boto3',
    'pandas',
    'pyyaml',
]
extra_requirements = {
    'dev': ['pre-commit', 'pytest', 'reuse'],
    'docs': ['sphinx', 'sphinx-book-theme'],
}

setup(
    name='sensepy',
    version='0.1',
    description='CLI for home',
    url='http://github.com/rscohn2/sensepy',
    author='Robert Cohn',
    author_email='rscohn2@gmail.com',
    license='MIT',
    packages=['sensepy'],
    entry_points={
        'console_scripts': ['sensecli=sensepy.cli:main'],
    },
    install_requires=requirements,
    extras_require=extra_requirements,
    zip_safe=False,
)
