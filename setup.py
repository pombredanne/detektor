from setuptools import setup, find_packages

setup(
    name='detektor',
    description='A library for finding similarities in code.',
    version='1.0.0-beta.001',
    url='https://github.com/appressoas/detektor',
    author='Magne Westlie',
    license='GPL',
    packages=find_packages(
        exclude=[
        ]),
    zip_safe=False,
    include_package_data=True,
    install_requires=['setuptools'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
