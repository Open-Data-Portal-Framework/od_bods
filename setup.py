from setuptools import setup, find_packages

setup(
    name = "open_data_project",
    version = "0.1",
    author = "Danail Dimov",
    author_email = "u05dd19@abdn.ac.uk",
    description = "A Python package to retrieve the data for your open data portal",
    packages = find_packages(),
    include_package_data = True,
    install_requires = ["beautifulsoup4",
                        "black",
                        "datefinder",
                        "Markdown",
                        "pandas==1.4.4",
                        "pytest==7.1.2",
                        "PyYAML==6.0",
                        "PyGithub",
                        "requests"],
    entry_points = {
        "console_scripts": [
        "odp=open_data_project.odp:main"
        ]
    }
)
