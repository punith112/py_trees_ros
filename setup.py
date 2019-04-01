#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

package_name = 'py_trees_ros'

setup(
    name=package_name,
    version='pre-1.0',
    packages=find_packages(exclude=['doc*', 'tests*', 'graveyard*']),
    install_requires = {},
    extras_require = {},
    author='Daniel Stonier, Naveed Usmani, Michal Staniaszek',
    maintainer='Daniel Stonier <d.stonier@gmail.com>',
    url='https://github.com/splintered-reality/py_trees_ros',
    keywords=['ROS', 'behaviour-trees'],
    zip_safe=True,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries'
    ],
    description=(
        "ROS extensions for py-trees, a pythonic implementation of "
        "behaviour trees."
    ),
    long_description=(
        "ROS extensions for py-trees, a pythonic implementation of "
        "behaviour trees. It includes ROS specific behaviours a tree"
        "manager with ROS communication handles for debugging and"
        "visualisation, logging and various tutorials."
    ),
    license='BSD',
)
