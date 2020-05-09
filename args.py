""" 
Basic wrappers for ArgParser, didn't feel like remembering how to set it up every time.
"""
import argparse
parser = argparse.ArgumentParser()

def add_arg(shortform, longform, required=False):
    """use for adding single argument"""
    parser.add_argument(shortform, longform, required=required)

def add_args(*args):
    """use for adding multiple arguments, short form and long form need to be grouped together"""
    num_args = len(args)
    for i in range(0,num_args,2):
        add_arg(args[i], args[i+1])

def get_arg(arg_name):
    args = vars(parser.parse_args())
    return args[arg_name]

def get_args(*args):
    """Fetch multiple arguments"""
    all_args = []
    for arg in args:
        all_args.append(get_arg(arg))

    return (arg for arg in all_args)
