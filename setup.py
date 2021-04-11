from setuptools import setup, find_packages
from pathlib import Path

version = "0.0.1"
here = Path(__file__).parent.resolve()

with open(here.joinpath("README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(here.joinpath("requirements.txt"), encoding="utf-8") as f:
    requirements = f.readlines()

setup(
    name="TODO",
    version=version,
    description="TODO",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="TODO",
    author="TODO",
    author_email="TODO",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
    ],
    keywords=["TODO"],
    packages=find_packages(),
    python_requires="TODO",
    install_requires=[requirements],
    project_urls={
        "Bug Reports": "TODO",
        "Source": "TODO",
    }
)
