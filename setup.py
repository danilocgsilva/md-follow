from setuptools import setup

VERSION = "0.0.1"

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="md_follow",
    version=VERSION,
    description="Follows markdown links to create html from markdown",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="markdown html conveter",
    url="git@github.com:danilocgsilva/md-follow.git",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["md_follow"],
    entry_points={"console_scripts": ["mdfollow=md_follow.__main__:main"],},
    include_package_data=True
)

