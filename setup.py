from setuptools import setup, find_packages

setup(
    name="urusaiyatu",
    version="1.0.0",
    author="neko",
    packages=find_packages(),
    install_requires=["aiohttp"],
    include_package_data=True,
)