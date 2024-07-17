from setuptools import find_packages, setup

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="image_search",
    version="0.0.1",
    description="A simple image search app using CLIP and FAISS",
    author="Croissant Team",
    packages=find_packages("app"),
    package_dir={"": "app"},
    install_requires=required,
)
