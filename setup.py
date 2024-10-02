import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__="0.0.0"

REPO_NAME = "End-to-end-ML-Project-Implementation"
AUTHOR_USER_NAME = "Haisam Abbas"
SRC_REPO = "Wine-Quality-Project"
AUTHOR_EMAIL = "imgujjar17@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small Python Project for ML app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{AUTHOR_EMAIL}/issue"
        
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where='src')
    
)