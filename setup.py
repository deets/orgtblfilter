from setuptools import setup, find_packages


setup(
    name = "orgtblfilter",
    version = "0.1",
    packages = find_packages(),
    author = "Diez B. Roggisch",
    author_email = "deets@web.de",
    description = "A sphinx extension to pre-process orgtbl-mode tables to sphinx tables",
    license = "PSF",
    keywords = "sphinx extension",
    entry_points = {
        'console_scripts': [
        ],
    }    
)

