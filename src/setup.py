import setuptools
import arcus
import sys

from setuptools.command.test import test as TestCommand

with open("src/package-description.md", "r") as fh:
    long_description = fh.read()

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setuptools.setup(
    name="arcus-azureml", # Replace with your own username
    version=arcus.__version__,
    author="Arcus",
    author_email="arcus-automation@codit.eu",
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    description="A Python library to improve MLOps methodology on Azure Machine Learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arcus-azure/arcus.azureml",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    extras_require={
        'testing': ['pytest'],
    }
)