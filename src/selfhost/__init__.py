import pathlib

def _get_version():
    version_file = pathlib.Path(__file__).parent.parent.parent / "VERSION"
    if version_file.exists():
        return version_file.read_text().strip()
    return "0.1.0"

__version__ = _get_version()
