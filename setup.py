import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
setup(
  name="kbbi_scraper",
  version="0.0.2",
  description="https://kbbi.co.id/ scraper",
  long_description=README,
  long_description_content_type="text/markdown",
  author="Hariz Sufyan Munawar",
  author_email="munawarhariz@gmail.com",
  license="MIT",
  packages=["kbbi_scraper"],
  zip_safe=False,
  install_requires=["requests", "beautifulsoup4"]
)