"""`BGSpace` provides a neat way of defining an anatomical space, and to operate
stacks and point transformations between anatomical spaces.
"""

from setuptools import setup, find_namespace_packages


with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="bgspace",
    version="version='0.1.0'",
    description="Anatomical space conventions made easy",
    install_requires=requirements,
    extras_require={
        "dev": [
            "black",
            "pytest-cov",
            "pytest",
            "gitpython",
            "coverage",
            "pre-commit",
            "nox",
        ]
    },
    project_description=__doc__,
    python_requires=">=3.6",
    packages=find_namespace_packages(exclude=("docs", "tests*")),
    include_package_data=True,
    url="https://github.com/brainglobe/bgspace",
    author="Luigi Petrucco @portugueslab",
    author_email="luigi.petrucco@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Science/Research",
    ],
    zip_safe=False,
)
