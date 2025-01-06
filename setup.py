from setuptools import setup, find_packages

setup(
    name="awesome_lists",
    version="1.0.0",
    author="Md Sulaiman",
    author_email="dev.sulaiman@icloud.com",
    description="A scraper for collecting all awesome projects on GitHub",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/khulnasoft-lab/awesome-lists",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests>=2.25.1",
        "beautifulsoup4>=4.9.3"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'awesome-scraper=main:main',
        ],
    },
)
