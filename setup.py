import pathlib
from setuptools import setup, find_packages


HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

install_requires = [
            'pyparsing>=2.4.7'
        ]


from my_happy_graphviz import version

setup(
  name="my-happy-graphviz",
  version=version.get_current(),
  description="Python interface to Graphviz's Dot language",
  long_description=README,
  long_description_content_type="text/markdown",
  license="Apache 2",
  url="https://github.com/ggservice007/my-happy-graphviz",
  author="ggservice007",
  author_email="ggservice007@126.com",
  packages=find_packages(exclude=[""]),
  install_requires=install_requires,
  include_package_data=True,
  zip_safe=False,
  python_requires=">=3.7.7"
)
