# joommfutil
Marijan Beg<sup>1,2</sup>, Ryan A. Pepper<sup>2</sup>, Thomas Kluyver<sup>1</sup>, and Hans Fangohr<sup>1,2</sup>

<sup>1</sup> *European XFEL GmbH, Holzkoppel 4, 22869 Schenefeld, Germany*  
<sup>2</sup> *Faculty of Engineering and the Environment, University of Southampton, Southampton SO17 1BJ, United Kingdom*  

| Description | Badge |
| --- | --- |
| Latest release | [![PyPI version](https://badge.fury.io/py/joommfutil.svg)](https://badge.fury.io/py/joommfutil) |
|                | [![Anaconda-Server Badge](https://anaconda.org/conda-forge/joommfutil/badges/version.svg)](https://anaconda.org/conda-forge/joommfutil) |
| Build | [![Build Status](https://travis-ci.org/joommf/joommfutil.svg?branch=master)](https://travis-ci.org/joommf/joommfutil) |
|       | [![Build status](https://ci.appveyor.com/api/projects/status/oukup0h6i6wxb3g1?svg=true)](https://ci.appveyor.com/project/marijanbeg/joommfutil) |
| Coverage | [![codecov](https://codecov.io/gh/joommf/joommfutil/branch/master/graph/badge.svg)](https://codecov.io/gh/joommf/joommfutil) |
| Documentation | [![Documentation Status](https://readthedocs.org/projects/joommfutil/badge/?version=latest)](http://joommfutil.readthedocs.io/en/latest/?badge=latest) |
| Binder | [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/joommf/joommfutil/master?filepath=index.ipynb) |
| Dependecies | [![Requirements Status](https://requires.io/github/joommf/joommfutil/requirements.svg?branch=master)](https://requires.io/github/joommf/joommfutil/requirements/?branch=master) |
| License | [![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause) |

## About

`joommfutil` is a Python package that provides:

- Typesystem for [JOOMMF](http://joommf.github.io) packages

It is available on all major operating systems (Windows, MacOS, Linux) and requires Python 3.5 or higher.

## Installation

We recommend installing `joommfutil` by using either of the `pip` or `conda` package managers.

#### Python requirements

Before installing `joommfutil` via `pip`, please make sure you have Python 3.5 or higher on your system. You can check that by running

    python3 --version

If you are on Linux, it is likely that you already have Python installed. However, on MacOS and Windows, this is usually not the case. If you do not have Python 3.5 or higher on your machine, we strongly recommend installing the [Anaconda](https://www.anaconda.com/) Python distribution. [Download Anaconda](https://www.anaconda.com/download) for your operating system and follow instructions on the download page. Further information about installing Anaconda can be found [here](https://conda.io/docs/user-guide/install/download.html).

#### `pip`

After installing Anaconda on MacOS or Windows, `pip` will also be installed. However, on Linux, if you do not already have `pip`, you can install it with

    sudo apt install python3-pip

To install the `joommfutil` version currently in the Python Package Index repository [PyPI](https://pypi.org/project/joommfutil/) on all operating systems run:

    python3 -m pip install joommfutil

#### `conda`

`joommfutil` is installed using `conda` by running

    conda install --channel conda-forge joommfutil

For further information on the `conda` package, dependency, and environment management, please have a look at its [documentation](https://conda.io/docs/). 

## Updating

If you used pip to install `joommfutil`, you can update to the latest released version in [PyPI](https://pypi.org/project/joommfutil/) by running

    python3 -m pip install --upgrade joommfutil

On the other hand, if you used `conda` for installation, update `joommfutil` with

    conda upgrade joommfutil

#### Development version

The most recent development version of `joommfutil` that is not yet released can be installed/updated with

    git clone https://github.com/joommf/joommfutil.git
    python3 -m pip install --upgrade joommfutil

**Note**: If you do not have `git` on your system, it can be installed by following the instructions [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Binder

`joommfutil` can be used in the cloud via Binder. This does not require you to have anything installed and no files will be created on your machine. To use `joommfutil` in the cloud, follow this [link](https://mybinder.org/v2/gh/joommf/joommfutil/master?filepath=index.ipynb).

## Documentation

Documentation for `joommfutil` is available [here](http://joommfutil.readthedocs.io/en/latest/?badge=latest), where APIs and tutorials (in the form of Jupyter notebooks) are available.

## Support

If you require support on installation or usage of `joommfutil` or if you want to report a problem, you are welcome to raise an issue in our [joommf/help](https://github.com/joommf/help) repository.

## License

Licensed under the BSD 3-Clause "New" or "Revised" License. For details, please refer to the [LICENSE](LICENSE) file.

## How to cite

If you use `joommfutil` in your research, please cite it as:

1. M. Beg, R. A. Pepper, and H. Fangohr. User interfaces for computational science: A domain specific language for OOMMF embedded in Python. [AIP Advances, 7, 56025](http://aip.scitation.org/doi/10.1063/1.4977225) (2017).

2. DOI will be available soon

## Acknowledgements

`joommfutil` was developed as a part of [OpenDreamKit](http://opendreamkit.org/) – Horizon 2020 European Research Infrastructure project (676541).
