# coding: utf-8

"""
    Firefly III API v1.5.6

    This is the documentation of the Firefly III API. You can find accompanying documentation on the website of Firefly III itself (see below). Please report any bugs or issues. You may use the \"Authorize\" button to try the API below. This file was last generated on 2022-04-04T03:54:41+00:00   # noqa: E501

    The version of the OpenAPI document: 1.5.6
    Contact: james@firefly-iii.org
    Generated by: https://openapi-generator.tech
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "fireflyiii-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi >= 14.5.14",
    "frozendict ~= 2.3.4",
    "python-dateutil ~= 2.7.0",
    "setuptools >= 21.0.0",
    "typing_extensions ~= 4.3.0",
    "urllib3 ~= 1.26.7",
]

setup(
    name=NAME,
    version=VERSION,
    description="Firefly III API v1.5.6",
    author="James Cole",
    author_email="james@firefly-iii.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Firefly III API v1.5.6"],
    python_requires=">=3.7",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="AGPLv3",
    long_description="""\
    This is the documentation of the Firefly III API. You can find accompanying documentation on the website of Firefly III itself (see below). Please report any bugs or issues. You may use the \&quot;Authorize\&quot; button to try the API below. This file was last generated on 2022-04-04T03:54:41+00:00   # noqa: E501
    """
)
