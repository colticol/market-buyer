"""Load Settings."""
import yaml


def load(filename):
    """Load yaml."""
    settings = {}
    with open(filename, 'r') as f:
        settings = yaml.load(f, Loader=yaml.FullLoader)
    return settings
