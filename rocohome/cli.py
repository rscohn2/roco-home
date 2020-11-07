import argparse
import rocohome


def parse_args():
    parser = argparse.ArgumentParser(description='CLI for rocohome')
    parser.add_argument(
        'verbose', action='store_true', help='display log information'
    )


def main():
    print(rocohome.joke())
