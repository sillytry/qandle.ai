from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="qandle-ai",
    version="0.0.1",
    author="Qandle AI",
    author_email="try.silly@gmail.com",
    description="Python SDK for Qandle AI API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sillytry/doc.qandle.ai",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires='>=3.7',
    install_requires=[
        "requests>=2.25.0",
    ],
    keywords="qandle ai llm stock market technical fundamental analysis data finance api sdk",
) 