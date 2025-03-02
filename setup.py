import setuptools

with open("README.md","r", encoding="utf-8") as f:
    long_description = f.read()

__version__="0.0.0"

REPO_NAME="ML_XAI_DASHBOARD"
AUTHOR_USER_NAME="syedsajjadaskari"
SRC_REPO="ML_XAI_DASHBOARD"
AUTHOR_EMAIL="syedsajjad62@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    long_description=long_description,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Ml Expalinable AI Dashboard",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)

