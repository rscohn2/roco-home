# SPDX-FileCopyrightText: 2020 Robert Cohn
#
# SPDX-License-Identifier: MIT

from setuptools import setup

requirements = [
    'boto3',
    'pyyaml',
]
extra_requirements = {
    'dev': ['pre-commit', 'pytest', 'reuse'],
    'docs': ['sphinx', 'sphinx-book-theme'],
}

setup(
    name='rocohome',
    version='0.1',
    description='CLI for home',
    url='http://github.com/rscohn2/rocohome',
    author='Robert Cohn',
    author_email='rscohn2@gmail.com',
    license='MIT',
    packages=['rocohome'],
    entry_points={
        'console_scripts': ['roco-home=rocohome.cli:main'],
    },
    install_requires=requirements,
    extras_require=extra_requirements,
    zip_safe=False,
)
