import os

from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

version = os.getenv(
    "VERSION", "0.0.0"
)  # Fallback to '0.0.0'version = os.getenv('PACKAGE_VERSION', '0.0.0')  # Fallback to '0.0.0'



setup(
    name="ci",
    version=version,
    author="Julia Ciapała",
    author_email="ciapalajulka@gmail.com",
    description="Attendance management system for university",
    url="https://https://github.com/1wakos/ci",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": ["ci=src.cli.cli:main"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)