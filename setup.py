from setuptools import setup

setup(
    name="simplegeo", 
    version="0.0.1",
    description="Simple library that allows to geocode using Nominatim or Google V3 API",
    py_modules=["geocoder"],
    package_dir={"": "src"}
)