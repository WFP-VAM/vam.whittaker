#!/usr/bin/env python
# pylint: disable=invalid-name, line-too-long
"""setup.py for VAM whittaker core"""

from setuptools import setup, Extension

import numpy
import _version
USE_CYTHON = 'auto'

if USE_CYTHON:
    try:
        from Cython.Distutils import build_ext
        if USE_CYTHON == 'auto':
            USE_CYTHON = True
    except ImportError:
        if USE_CYTHON == 'auto':
            USE_CYTHON = False
        else:
            raise

cmdclass = {}
ext_modules = []

if USE_CYTHON:
    ext_modules += [
        Extension("vam.whittaker",
                  ["src/_whittaker.pyx"], extra_compile_args=["-O3", "-ffast-math"])]
    cmdclass.update({'build_ext': build_ext})
else:
    ext_modules += [
        Extension("vam.whittaker",
                  ["src/_whittaker.c"], extra_compile_args=["-O3", "-ffast-math"])]

setup(
    name='vam.whittaker',
    description='VAM whittaker core',
    version=_version.__version__,
    author='Valentin Pesendorfer',
    author_email='valentin.pesendorfer@wfp.org',
    url='http://github.com/WFP-VAM/vam.whittaker',
    long_description='''State-of-the art whittaker smoother, implemented as fast C-extension through Cython and including a V-curve optimization of the smoothing parameter.

    For more information, please visit: http://github.com/WFP-VAM/vam.whittaker''',
    include_dirs=[numpy.get_include()],
    cmdclass=cmdclass,
    ext_modules=ext_modules,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    install_requires=[
        'numpy>=1.15.1',
        'mock;python_version<"3.0"'
    ],
    python_requires='>=2.7.11, <4',
)
