
from setuptools import setup, find_packages
import sys, os, multiprocessing

setup(
    name='GenerateRaid',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    dependency_links=[
        "git+https://github.com/mschober/exp-pcommon.git#egg=common"
    ],
    setup_requires=['nose>=1.0', 'pytest', 'common'],
    install_requires=['nose', 'pytest', 'common'],
    test_suite="nose.collector",
    tests_require=["nose"],
    entry_points={
        'console_scripts': [
            'new_raid = generate_raid.new_raid:NewRaidMain'
        ],
    }
)
