#! /usr/bin/env python3
"""
    Check if user enter all necessary arguments correctly.
    Otherwise, a message is sent to the user.
"""
import sys
import re


def check_int_type(rep):
    """ Check if the answer can be cast into int
    and return it
        @param rep: The answer given by the user in str
        Return the answer casted in int
    """
    try:
        rep = int(rep)
    except ValueError:
        print("Be carefull, a number is expected !")
        sys.exit(2)
    assert rep > 0, "The number must be positif"
    return rep


def check_arguments(argv):
    """ Assign options into variable and check if
    option are correct.
        @param argv: Arguments given by the user
    """
    global SEQUENCE
    global LEN_SEQ
    SEQUENCE = argv["--sequence"].upper()
    if(not bool(re.match("^[HP]+$", SEQUENCE))):
        print("Be carefull, use the hp model for the sequence !")
        sys.exit(2)
    LEN_SEQ = len(SEQUENCE)

    global NB_STEPS
    NB_STEPS = check_int_type(argv["--steps"])

    global MIN_ENERGY
    MIN_ENERGY = - check_int_type(argv["--energy"])

    global MOVE_SET
    MOVE_SET = argv["--movement"]
    if MOVE_SET not in ("VSHD", "PULLMOVES", "MIXE"):
        print("You can choose between VSHD, PULLMOVES and MIXE movement set.")
        sys.exit(2)

    global TEMPERATURE
    TEMPERATURE = check_int_type(argv["--temperature"])

    global REPLICA
    REPLICA = check_int_type(argv["--replica"])
