from setuptools import setup, find_packages
from pathlib import Path

lines = Path("jupyter_http_server").joinpath("__init__.py")
for line in lines.read_text().split("\n"):
    if line.startswith("__version__ ="):
        version = line.split(" = ")[-1].strip('"')
        break

setup(
    name="jupyter-http-server",
    version=version,
    python_requires=">=3.6",
    author="Chris Holdgraf",
    author_email="choldgraf@berkeley.edu",
    project_urls={
        "Source": "https://github.com/choldgraf/jupyter-http-server/",
        "Tracker": "https://github.com/jupyter/jupyter-http-server/issues",
    },
    # this should be a whitespace separated string of keywords, not a list
    keywords="http-server jupyter",
    description="A simple HTTP server for Jupyter interfaces",
    long_description=Path("./README.md").read_text(),
    long_description_content_type="text/markdown",
    license="BSD",
    packages=find_packages(),
    install_requires=['jupyter-server-proxy'],
    py_modules=['jupyter_http_server'],
    entry_points={
        'jupyter_serverproxy_servers': [
            # name = packagename:function_name
            'http-server = jupyter_http_server:setup_http_server',
        ]
    },
    include_package_data=True,
)
