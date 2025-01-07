from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sales_tracker",
    version="1.0.0",
    author="",
    author_email="",
    description="A tool for tracking and analyzing company information for sales teams",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jakedh123/sales_tracker",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Sales Teams",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.31.0",
        "beautifulsoup4>=4.12.2",
        "selenium>=4.16.0",
        "python-dotenv>=1.0.0",
        "pandas>=2.1.4",
        "linkedin-api-client>=2.0.0",
        "twitter-api-client>=1.6.0",
        "google-search-results>=2.4.2"
    ],
    entry_points={
        "console_scripts": [
            "sales-tracker=sales_tracker:main",
        ],
    },
)