# -*-coding:utf-8-*-


from setuptools import setup

setup(
    name='validata',
    version='0.0.1',
    packages=[
        'validata',
    ],
    install_requires=[
        'mongoengine >= 0.8',
        'arrow',
        'etl_utils',
    ],
    zip_safe=False,
)
