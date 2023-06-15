from codecs import open
from setuptools import setup, find_packages

VERSION = "0.0.1"

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'License :: OSI Approved :: MIT License',
]

DEPENDENCIES = []

setup(
    name='fabrictest',
    version=VERSION,
    description='Test extension for Fabric',
    long_description='Test extension for Fabric.',
    license='',
    author='',
    author_email='',
    url='',
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    install_requires=DEPENDENCIES
)