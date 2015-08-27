#!/usr/bin/env python

__author__ = 'Tudor'
import ez_setup

ez_setup.use_setuptools()
from setuptools import setup, find_packages, version

with open('README.rst') as file:
    long_description = file.read()

setup(name='sphere2cube',
      version='0.1.0',
      description='Python script to map an equirectangular (cylindrical projection; skysphere) map into 6 cube (cubemap; skybox) faces',
      long_description=long_description,
      author='Tudor Brindus',
      author_email='tbrindus@gmail.com',
      url='http://github.com/Xyene/sphere2cube',
      packages=find_packages(),
      data_files=[('', ['sphere2cube/projector.blend'])],
      entry_points={
          'console_scripts': ['sphere2cube=sphere2cube.sphere2cube:main'],
      },
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Artistic Software'
      ],
)