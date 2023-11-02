from setuptools import find_packages,setup


setup(
    name='DimondPricePrediction',
    version='0.0.1',
    author='sunny savita',
    author_email='sunny.savita@ineuron.ai',
    install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages()
)