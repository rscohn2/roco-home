# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

from setuptools import setup

requirements = [
    'boto3',
    'Flask',
    'marshmallow',
    'pandas',
    'pyyaml',
]
extra_requirements = {
    'dev': ['pre-commit', 'pytest', 'reuse'],
    'docs': ['sphinx', 'sphinx-book-theme', 'sphinxcontrib-spelling'],
}

setup(
    name='signalpy',
    version='0.1',
    description='CLI for home',
    url='http://github.com/signalpy/signalpy',
    author='Robert Cohn',
    author_email='rscohn2@gmail.com',
    license='MIT',
    packages=['signalpy'],
    entry_points={
        'console_scripts': ['sensecli=signalpy.cli:main'],
    },
    install_requires=requirements,
    extras_require=extra_requirements,
    zip_safe=False,
)
