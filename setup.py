import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Regx-Dev",
    version="1.0.0",
    description="A useful tool for information scrapper's or Developers to minimize there time.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/mr-elliot/Regx-Dev",
    author="Sanjay Kumar J",
    author_email="sanjaykumarj222@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=["Regx-Dev"],
    include_package_data=True,
    install_requires=["re"],
    # entry_points={
    #     "console_scripts": [
    #         "Regx-Dev=Regx-Dev.Regx-Dev.__main__:main",
    #     ]
    # },
)
