import setuptools


setuptools.setup(
    name='aionova',
    version='0.0.1',
    author='Kenny Millington',
    author_email='kenny@kennynet.co.uk',
    description='A simple asyncio based library for communicating with Anova Precision Cookers',
    url='https://github.com/kmdm/aionova',
    packages=setuptools.find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)