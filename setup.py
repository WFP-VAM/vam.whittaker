# pylint: disable=invalid-name, line-too-long
"""setup.py for VAM whittaker core"""

from setuptools import setup, Extension

import numpy

USE_CYTHON = "auto"

if USE_CYTHON:
    try:
        from Cython.Distutils import build_ext

        if USE_CYTHON == "auto":
            USE_CYTHON = True
    except ImportError:
        if USE_CYTHON == "auto":
            USE_CYTHON = False
        else:
            raise

cmdclass = {}
ext_modules = []

if USE_CYTHON:
    ext_modules += [
        Extension(
            "vam.whittaker",
            ["vam/whittaker/_whittaker.pyx"],
            extra_compile_args=["-O3", "-ffast-math"],
        )
    ]
    cmdclass.update({"build_ext": build_ext})
else:
    ext_modules += [
        Extension(
            "vam.whittaker",
            ["vam/whittaker/_whittaker.c"],
            extra_compile_args=["-O3", "-ffast-math"],
        )
    ]

setup(
    include_dirs=[numpy.get_include()],
    cmdclass=cmdclass,
    ext_modules=ext_modules,
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    install_requires=["numpy>=1.15.1", 'mock;python_version<"3.0"'],
    python_requires=">=3, <4",
)
