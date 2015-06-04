from setuptools import setup


def get_version(filename):
    """
    Parse the value of the __version__ var from a Python source file
    without running/importing the file.
    """
    import re
    version_pattern = r"^ *__version__ *= *['\"](\d+\.\d+\.\d+)['\"] *$"
    match = re.search(version_pattern, open(filename).read(), re.MULTILINE)

    assert match, ("No version found in file: {!r} matching pattern: {!r}"
                   .format(filename, version_pattern))

    return match.group(1)


setup(
    name="sublcmd",
    version=get_version("sublcmd.py"),
    py_modules=["sublcmd"],
    author="Hal Blackburn",
    author_email="hwtb2@cam.ac.uk",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "subl = sublcmd:main",
        ]
    }
)
