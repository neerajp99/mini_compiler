from setuptools import setup, find_packages

setup(
    name="src", 
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]
    ),
    install_requires = [
        "asyncio",
        "aiohttp",
        "requests",
    ]   
)