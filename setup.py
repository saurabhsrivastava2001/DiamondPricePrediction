from setuptools import find_packages,setup


setup(
    name='DimondPricePrediction',
    version='0.0.1',
    author='Saurabh Srivastava',
    author_email='srisaurabh@gmail.com',
    install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages()
)