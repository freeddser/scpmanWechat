import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
        name="scpmanWechat",
        version="1.0.3",
        description="Send Message to Wechat Application",
        long_description=long_description,
        long_description_content_type="text/markdown",
        # long_description_context_type=readme,
        author="scpman",
        author_email="scpman@live.com",
        maintainer='scpman',
        maintainer_email='scpman@live.com',
        url="https://github.com/freeddser/scpmanWechat",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.0',
    )


