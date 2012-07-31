import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "urls",
    version = "0.1",
    author = "Jonathan Wight",
    author_email = "jwight@mac.com",
    description = ("Command to extract and process URLs found in text."),
    license = "BSD",
    keywords = "url",
#    url = "http://packages.python.org/an_example_pypi_project",
#    packages=['an_example_pypi_project', 'tests'],
    long_description=read('README.markdown'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    py_modules = ['urls'],
    scripts = ['urls']
)
