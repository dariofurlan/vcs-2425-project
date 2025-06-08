from setuptools import setup, find_packages

setup(
    name="vcs2425",
    version="0.1.0",
    author="Dario",
    description="A package for vision computer science 2024-2025 course",
    packages=find_packages(),
    package_dir={"vcs2425": "vcs2425"},
    python_requires=">=3.6",
    install_requires=[
        "numpy",
        "pillow",
        "torch",
        "matplotlib",
    ],
)
