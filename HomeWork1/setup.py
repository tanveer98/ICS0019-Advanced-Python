import setuptools

with open("README.md", "r") as fp:
    desc = fp.read()

setuptools.setup(
    name="quadratic-equation-mhasan-v3", # Replace with your own username
    version="0.2",
    author="Tanveer Hasan",
    author_email="mhasan@ttu.ee",
    description="Exercise module, calculates solutions for quadratic equations",
    long_description=desc,
    long_description_content_type="text/markdown",
    url="https://github.com/tanveer98/ICS0019-Advanced-Python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    test_suite='quadratic-equation-mhasan-v3.test.test_quadratic'
)