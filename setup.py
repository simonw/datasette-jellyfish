from setuptools import setup
import os

VERSION = "1.0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-jellyfish",
    description="Datasette plugin adding SQL functions for fuzzy text matching powered by Jellyfish",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://datasette.io/plugins/datasette-jellyfish",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-jellyfish/issues",
        "CI": "https://github.com/simonw/datasette-jellyfish/actions",
        "Changelog": "https://github.com/simonw/datasette-jellyfish/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_jellyfish"],
    entry_points={"datasette": ["jellyfish = datasette_jellyfish"]},
    install_requires=["datasette", "jellyfish>=0.8.2"],
    extras_require={"test": ["pytest"]},
    tests_require=["datasette-jellyfish[test]"],
)
