import setuptools

setuptools.setup(
    name="web-crawler-dsmrt",
    version="0.0.1",
    author="Damien Smrt",
    author_email="me@dsmrt.com",
    description="A simple web crawler cli",
    url="https://github.com/dsmrt/web-crawler",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        'click',
        'requests',
        'bs4',
    ],
    entry_points={
        'console_scripts': [
            'web-crawler = src.app:cli',
        ],
    },
)