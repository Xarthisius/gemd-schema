#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ["jsonschema"]

test_requirements = ['pytest>=3', ]

setup(
    author="Kacper Kowalik",
    author_email='xarthisius.kk@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    description="JSON Schema for GEMD",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='gemd_schema',
    name='gemd_schema',
    packages=find_packages(include=['gemd_schema', 'gemd_schema.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Xarthisius/gemd_schema',
    version='0.1.0',
    zip_safe=False,
)
