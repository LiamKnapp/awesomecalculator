import setuptools
import os
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
# small change
setuptools.setup(
    name="LiamKnapp-awesomecalculator", # Replace with your own username
    version= "1.0.0",
    author="Liam",
    author_email="lknapp1110@conestogac.on.ca",
    description="An awesome calculator package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LiamKnapp/awesomecalculator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)