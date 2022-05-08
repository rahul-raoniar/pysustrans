from setuptools import setup, find_packages


PACKAGE_NAME = 'pysustrans'
AUTHOR = 'Rahul Raoniar'
EMAIL = "rahul.raoniar@outlook.com"
URL = ''
DOWNLOAD_URL = ''
VERSION = '0.0.1'
DESCRIPTION = 'A transportation data analytics package'
LONG_DESCRIPTION = 'A package that allows performing common statitical analysis on transportation related data.'
LICENSE = 'MIT'
CLASSIFIERS = [
        'Programming Language :: Python :: 3'
]
LONG_DESC_TYPE = "text/markdown"


# Setting up
setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESC_TYPE,
    packages=find_packages(),
    install_requires=['dython', 'pandas', 'matplotlib', 'numpy'],
    keywords=['python', 'transportation', 'exporatory data analysis' 'statistics', 'modelling'],
    classifiers= CLASSIFIERS,
    license= LICENSE
)
