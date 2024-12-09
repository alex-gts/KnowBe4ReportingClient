from setuptools import setup, find_packages


def parse_requirements(filename):
    """Load requirements from a pip requirements file."""
    with open(filename) as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]


requirements = parse_requirements("requirements.txt")

setup(
    name="KnowBe4Client",
    version="0.1.0",
    author="Alex Garrison",
    author_email="alex.garrison@discoverieplc.com",
    description="Python interface to interact with the KnowBe4 API",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    license_files=("LICENSE.md",),
    python_requires=">=3.6",
)
