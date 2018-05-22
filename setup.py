#!/usr/bin/env python
from setuptools import setup, find_packages

from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session=False)
testing_reqs = parse_requirements('test_requirements.txt', session=False)

reqs = [str(ir.req) for ir in install_reqs]
test_reqs = [str(ir.req) for ir in testing_reqs]


setup(name='hermes',
      version='1.0',
      description='Hermes provides an interface for interacting with GoDaddy messaging systems',
      author='DCU',
      author_email='dcueng@godaddy.com',
      url='https://github.secureserver.net/ITSecurity/hermes',
      packages=find_packages(),
      long_description=open('README.md').read(),
      install_requires=reqs,
      tests_require=test_reqs,
      test_suite="nose.collector"
      )
