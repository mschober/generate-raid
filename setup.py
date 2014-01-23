from setuptools import setup, find_packages
import sys, os, multiprocessing

version = '0.1'

setup(
    name='GenerateRaid',
    version=version,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    dependency_links=[
        "file://localhost/Users/mschober/dev/lng/python/exp/common#egg=common-1.0"
    ],
    setup_requires=['nose>=1.0', 'pytest', 'common==0.1'],
    install_requires=['nose', 'pytest'],
    test_suite="nose.collector",
    tests_require=["nose"],
    entry_points={
    'console_scripts': [
        'new_raid = src.generate_raid:GenerateRaidMain',
        ],
    }
)
