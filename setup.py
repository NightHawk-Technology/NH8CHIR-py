from setuptools import setup, find_packages

setup(
    name='nh8chir',
    version='0.1.0',
    packages=find_packages(),
    author='NightHawk Robotics',
    author_email='dev@nhshop.tech',
    description='This library made for NH8CHIR sensor from NightHawk Robotics',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/NightHawk-Technology/NH8CHIR-py',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    include_package_data=True,
)
