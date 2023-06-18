#!/usr/bin/env python3

'''
Copyright (C) 2023 Antonio Ceballos Roa

compute-seats - Apply electoral systems to compute seats from votes.
'''

import argparse
from elecsys import compseats

def parse_cmd_line_args():
    global args
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("nseats", nargs=1, type=int, action='store', help="number of seats")
    parser.add_argument("votes", nargs=1, type=str, action='store', help="number of votes obtained by each electoral list (e.g.: l1:5,l2:0,l3:12)")
    parser.add_argument("method", nargs=1, type=str, choices=["sl", "ms", "dh", "ha", "dr"], action='store', help="electoral method")
    parser.add_argument('-i', '--index', action='store_true', help="compute Gallagher index")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1.0')
    args = parser.parse_args()
    return args

def main():
    # Parse command-line arguments
    args = parse_cmd_line_args()
    n_seats = int(args.nseats[0])
    votes = dict()
    for electoral_list_votes in args.votes[0].split(','):
        electoral_list, n = electoral_list_votes.split(':')
        votes[electoral_list] = int(n)
    method = args.method[0]
    index = args.index
    # Compute seats
    seats = compseats(n_seats, votes, method, index)
    if index:
        seats['gallagher_index'] = round(seats['gallagher_index'], 2)
    print(seats)

if __name__ == '__main__':
    main()
