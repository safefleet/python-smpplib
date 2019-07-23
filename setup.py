from setuptools import setup, find_packages
import sys

setup(
    name="aiosmpp",
    version='1.0.2',
    url='https://github.com/tpark-platform/aiosmpp',
    description='SMPP library for python based on asyncio',
    packages=find_packages(),
    install_requires=['six'],
    tests_require=['pytest', 'mock'],
    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Topic :: Communications :: Telephony',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved',
    ],
)
