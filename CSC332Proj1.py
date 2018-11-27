#!/usr/bin/python
import argparse
import sys

def options():
    parser = argparse.ArgumentParser()
    parser.add_argument('-message', type = str, help = 'The Message to Encrpyt')

    args = parser.parse_args()
    return args

def main():
    options()
    message = options().message

    print message

if __name__ == "__main__":
    main()


