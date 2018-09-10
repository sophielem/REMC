#! /usr/bin/env python3

import checkingArgument as cA
import random


def vshd_move(residu):
    if residu == 0 or residu == (cA.LEN_SEQ - 1):
        end_moves(residu)
    else:
        prob = random.random()
        if prob >= 0.8:
            crankshaft_moves(residu)
        else:
            corner_moves(residu)


def end_moves(residu):
    pass


def crankshaft_moves(residu):
    pass


def corner_moves(residu):
    pass


#PULLMOVE SET
def pullmoves_move(residu):
    pull_moves(residu)


def pull_moves(residu):
    pass


# MIXE SET
def mixe_move(residu):
    prob = random.random()
    if residu == 0 or residu == (cA.LEN_SEQ - 1):
        if prob <= 0.4:
            # pull movement
            endpull_moves(residu)
        else:
            # vshd movement
            end_moves(residu)
    else:
        if prob <= 0.4:
            # pull movement
            pull_moves(residu)
        else:
            # vshd movement
            prob = random.random()
            if prob >= 0.8:
                crankshaft_moves(residu)
            else:
                corner_moves(residu)
