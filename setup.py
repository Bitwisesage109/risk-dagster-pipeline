from setuptools import find_packages, setup

setup(
    name="Risk",
    packages=find_packages(exclude=["Risk_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
