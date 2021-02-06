# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

from setuptools import find_packages, setup

requirements = [
    'boto3',
    'Flask',
    'marshmallow',
    'pandas',
    'pymongo',
    'pyyaml',
]
extra_requirements = {
    'dev': ['pre-commit', 'pytest', 'reuse'],
    'docs': ['sphinx', 'sphinx-book-theme', 'sphinxcontrib-spelling'],
}

setup(
    name='zignalz',
    version='0.1',
    description='Manage IOT data collection of signals',
    url='http://github.com/zignalz/zignalz',
    author='Robert Cohn',
    author_email='rscohn2@gmail.com',
    license='MIT',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    entry_points={
        'console_scripts': ['zz=zignalz.cli:main'],
    },
    install_requires=requirements,
    extras_require=extra_requirements,
    zip_safe=False,
)
