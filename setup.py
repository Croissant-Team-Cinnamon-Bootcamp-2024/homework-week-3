from setuptools import find_packages, setup


def parse_requirements(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]


setup(
    name="image_search",
    version="0.0.1",
    description="A simple image search app using CLIP and FAISS",
    author="Croissant Team",
    packages=find_packages("app"),
    package_dir={"": "app"},
    install_requires=parse_requirements('requirements.txt'),
)
