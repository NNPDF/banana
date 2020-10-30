# -*- coding: utf-8 -*-
# Installation script for python
from setuptools import setup, find_packages

setup(
    name="banana-hep",
    author="Felix Hekhorn, Alessandro Candido",
    version="0.1.0",
    description="mm yummy banana",
    package_data={
        "banana": [
            "data/templatePDF.dat",
            "data/templatePDF.info",
            "data/theory_template.yaml",
        ]
    },
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=[
        "ipython",
        "numpy",
        "pandas",
        "rich",
        "pyyaml",
        "tinydb~=4.1",
        "human_dates2",
    ],
    entry_points={
        "console_scripts": [
            "generate_pdf=banana.data.generate_pdf:generate_pdf",
            "install_pdf=banana.data.generate_pdf:install_pdf",
        ],
    },
    python_requires=">=3.7",
)
