import argparse

class ARGHELP:
    """Helps with arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-l","--lang", help="allows you to change language")
    parser.parse_args()
