# -*- coding: utf-8 -*-

# License: BSD 3-Clause

import os
import setuptools
import sys

if sys.version_info < (3, 5):
    raise ValueError(
        'Unsupported Python version {}.{}.{} found. OpenML requires Python 3.5 or higher.'
        .format(sys.version_info.major, sys.version_info.minor, sys.version_info.micro)
    )

with open(os.path.join("README.md")) as fid:
    README = fid.read()

setuptools.setup(name="openml-tensorflow",
                 version='1.0.0',
                 author="Prabhant Singh, Taniya Das",
                 author_email="prabhantsingh@gmail.com, taniyatd30@gmail.com",
                 maintainer="Taniya Das",
                 maintainer_email="taniyatd30@gmail.com",
                 description="Tensorflow extension for Openml python API",
                 long_description=README,
                 long_description_content_type='text/markdown',
                 license="BSD 3-clause",
                 url="http://openml.org/",
                 project_urls={
                     "Documentation": "https://openml.github.io/openml-tensorflow/",
                     "Source Code": "https://github.com/openml/openml-tensorflow"
                 },
                 # Make sure to remove stale files such as the egg-info before updating this:
                 # https://stackoverflow.com/a/26547314
                 packages=setuptools.find_packages(
                     include=['openml_tensorflow*', 'openml_tensorflow'],
                     exclude=["*.tests", "*.tests.*", "tests.*", "tests"],
                 ),
                 package_data={'': ['*.txt', '*.md', 'docker/*', 'docs/*']},
                 include_package_data=True,
                 python_requires=">=3.5",
                 install_requires=[
                     'openml',
                     'tensorflow>=2.0, <2.16.0',
                     'tf2onnx', 
                     'dill',
                     'pillow',
                 ],
                 classifiers=['Intended Audience :: Science/Research',
                              'Intended Audience :: Developers',
                              'License :: OSI Approved :: BSD License',
                              'Programming Language :: Python',
                              'Topic :: Software Development',
                              'Topic :: Scientific/Engineering',
                              'Operating System :: POSIX',
                              'Operating System :: Unix',
                              'Operating System :: MacOS',
                              'Programming Language :: Python :: 3',
                              'Programming Language :: Python :: 3.5',
                              'Programming Language :: Python :: 3.6',
                              'Programming Language :: Python :: 3.7',
                              'Programming Language :: Python :: 3.8',
                              'Programming Language :: Python :: 3.9',
                              'Programming Language :: Python :: 3.10',
                              'Programming Language :: Python :: 3.11',
                              'Programming Language :: Python :: 3.12'])