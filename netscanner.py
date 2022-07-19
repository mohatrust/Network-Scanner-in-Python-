#! /usr/bin/env/ python

import scapy.all as scapy
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target IP/ IP range.")
    (options, arguments) = parser.parse_args()
    return options


def scan(ip): ...


def print_result(results_list): ...


options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)
