from setuptools import setup, find_packages

setup(
    name='jgtfxlive',
    version='1.0.0',
    author='Your Name',
    author_email='your@email.com',
    description='A Python module for live chart data export',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'jgtfxlive = jgtfxlive.LiveChartDataExport:main',
            'jgtfxliveconf = jgtfxlive.config_generator:main'
        ]
    },
    install_requires=[
        # Add any dependencies required by your module here
    ],
)