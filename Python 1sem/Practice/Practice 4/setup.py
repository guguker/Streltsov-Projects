import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="calculator-pkg-guguker",
    version="0.1.1",
    author="valerka",
    author_email="youremail@example.com",
    description="Простой калькулятор на Python",
    long_description="бу бу бу бу",
    long_description_content_type="text/markdown",
    url="https://github.com/guguker/practice-4",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
