from setuptools import setup, find_packages

setup(
    name="Risk",
    version="0.1.0",
    packages=find_packages(exclude=["Risk_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "pandas",
        "pyodbc",
        "paramiko",
        "cryptography",
    ],
    author="Bitwisesage109",
    description="Risk Pipeline Dagster Project",
    python_requires=">=3.8",
)

