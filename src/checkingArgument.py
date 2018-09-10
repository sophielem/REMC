#! /usr/bin/env python3

import sys
import getopt

def check_int_type(rep):
    try:
        assert int(rep)
        rep = int(rep)
        assert rep > 0
    except ValueError:
        print("Be carefull, a number is expected")
        usage()
        sys.exit(2)
    except AssertionError:
        print("The number must be positif")
        usage()
        sys.exit(2)
    return rep


def check_arguments(argv):
    try:
        opts, args = getopt.getopt(argv, "hs:t:e:m:",
                                   ["help", "sequence=", "steps=", "energy=",
                                    "movement="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print("ERROR : options are not recognized")
        usage()
        sys.exit(2)

#BUG checker le nombre d'argument ATTENTION à help qui sera le seul argument
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-s", "--sequence"):
            global SEQUENCE
            global LEN_SEQ
            SEQUENCE = arg.upper()
            LEN_SEQ = len(SEQUENCE)
        elif opt in ("-t", "--steps"):
            global NB_STEPS
            NB_STEPS = check_int_type(arg)
        elif opt in ("-e", "--energy"):
            global MIN_ENERGY
            MIN_ENERGY = - check_int_type(arg)
        elif opt in ("-m", "--movement"):
            global MOVE_SET
            MOVE_SET = arg
            if not(MOVE_SET in ("VSHD", "PULLMOVES", "MIXE")):
                print("PROBLEM MOVE SET")
                usage()
                sys.exit(2)


def usage():
    print("HELP")
