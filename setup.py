from setuptools import setup, find_packages

setup(
    name="pyzoho-books",
    version="0.1.3.5",
    description="A Python package for interacting with the Zoho Books API.",
    author="Rahul Kumar",
    author_email="rahul.work.programming@gmail.com",
    url="https://github.com/rahul-08-11/pyzohobooks",
    packages=find_packages(),
    install_requires=[
        "requests"
        # List dependencies here (e.g., "numpy>=1.18.0")
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
