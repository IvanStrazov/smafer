# utf-8
# Python 3.9
# 2021-05-03


import setuptools
import smafer


setuptools.setup(
    name="smafer",
    version=smafer.__version__,
    description="Pipeline for small time series forecasting.",
    long_description=open("README.md").read(),
    author="Ivan Strazov",
    author_email="ivanstrazov@gmail.com",
    url="https://github.com/IvanStrazov/smafer/",
    license=open("LICENSE").read(),
    keywords="ml timeseries forecast arima ets",
    packages=setuptools.find_packages()
)
