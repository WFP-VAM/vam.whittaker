
vam.whittaker
-------------

|CI| |version| |downloads| |license|

.. |CI| image:: https://github.com/WFP-VAM/vam.whittaker/actions/workflows/ci.yml/badge.svg
             :target: https://github.com/WFP-VAM/vam.whittaker/actions/workflows/ci.yml

.. |version| image:: https://img.shields.io/pypi/v/vam.whittaker.svg
                  :target: https://pypi.org/project/vam.whittaker/

.. |downloads| image:: https://img.shields.io/pypi/dm/vam.whittaker.svg
                    :target: https://pypi.org/project/vam.whittaker/

.. |license| image:: https://img.shields.io/github/license/WFP-VAM/vam.whittaker.svg
                  :target: https://github.com/WFP-VAM/vam.whittaker/blob/master/LICENSE
|

Whittaker core functionality used in the `modape package <https://github.com/WFP-VAM/modape>`_

State-of-the art whittaker smoother, implemented as fast C-extension through Cython and including a V-curve optimization of the smoothing parameter.

Includes the following variations of the whittaker smoother with 2nd order differences:

- **ws2d**: Whittaker with fixed smoothing parameter (``s``)
- **ws2dp**: Whittaker with fixed smoothing parameter (``s``) and expectile smoothing using asymmetric weights
- **ws2doptv**: Whittaker with V-curve optimization of the smoothing parameter (``s``)
- **ws2doptvp**: Whittaker with V-curve optimization of the smoothing parameter (``s``) and expectile smoothing using asymmetric weights


Installation
------------
**Dependencies:**

vam.whittaker depends on `numpy`. For building the c-extension, `Cython` is required.


**Installation from PyPI:**

.. code:: bash

    $ pip install vam.whittaker

**Installation from github:**

.. code:: bash

    $ git clone https://github.com/WFP-VAM/vam.whittaker
    $ cd vam.whittaker
    $ pip install .


Usage
-----

.. code:: python

    import vam.whittaker

    # or

    from vam.whittaker import * # ws2d, ws2dp, ws2doptv, ws2optvp, lag1corr


For examples on the usage of the different functions, check out the `modape jupyter notebook <https://github.com/WFP-VAM/modape/blob/master/docs/examples/whittaker_core.ipynb>`_!

Bugs, typos & feature requests
-----

If you find a bug, see a typo, have some kind of troubles running the module or just simply want to have a feature added, please `submit an issue <https://github.com/WFP-VAM/vam.whittaker/issues/new>`_!


CHANGES
-----

- v1.0.0:
        - initial release
- v1.0.1:
        - minor version issue fix
- v2.0.0:
        - new function `wsdp` & fix for `ws2doptvp`
- v2.0.1:
        - minor bugfix in `wsdp`
- v2.0.2:
        - distribute built extension on pypi
- v2.0.3:
        - restructure and improve packaging

-----

References:

P. H. C. Eilers, V. Pesendorfer and R. Bonifacio, "Automatic smoothing of remote sensing data," 2017 9th International Workshop on the Analysis of Multitemporal Remote Sensing Images (MultiTemp), Brugge, 2017, pp. 1-3.
doi: 10.1109/Multi-Temp.2017.8076705
URL: http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8076705&isnumber=8035194

Core Whittaker function adapted from ``whit2`` function from `R` package `ptw <https://cran.r-project.org/package=ptw>`_:

Bloemberg, T. G. et al. (2010) "Improved Parametric Time Warping for Proteomics", Chemometrics and Intelligent Laboratory Systems, 104 (1), 65-74

Wehrens, R. et al. (2015) "Fast parametric warping of peak lists", Bioinformatics, in press.
