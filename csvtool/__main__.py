import argparse,csv,os,sys

def main():
    # Interpret the command line.
    ap=argparse.ArgumentParser(
        description="""\
Read CSV data from standard output and write it to standard output, possibly changing the CSV dialect along the way.
"""
    )
    opt=ap.parse_args()
    return None

if __name__=='__main__':
    sys.exit(main())
