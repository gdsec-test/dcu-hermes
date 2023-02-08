from setuptools import find_packages, setup

with open('requirements.txt') as f:
    install_reqs = f.read().splitlines()

with open('test_requirements.txt') as f:
    testing_reqs = f.read().splitlines()

with open('README.md') as f:
    long_description = f.read()


setup(
    name='hermes',
    version='1.2.0',
    author='DCU',
    author_email='dcueng@godaddy.com',
    description='Hermes provides an interface for interacting with GoDaddy messaging systems',
    long_description=long_description,
    url='https://github.com/gdcorp-infosec/dcu-hermes',
    packages=find_packages(exclude=['tests']),
    install_requires=install_reqs,
    tests_require=testing_reqs,
    test_suite='nose.collector',
    classifiers=[
        'Programming Language :: Python :: 3.11.1'
    ]
)
