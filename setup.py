from setuptools import setup, find_packages

setup(
    name="selflinkMarketing",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'instaloader',
        'google-api-python-client',
        'google-auth-oauthlib',
        'google-auth-httplib2',
        'PySocks'
    ]  
)
