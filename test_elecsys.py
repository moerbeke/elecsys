'''
Copyright (C) 2023 Antonio Ceballos Roa

elecsys - Apply electoral systems to compute seats from votes.
'''

from unittest import TestCase

from elecsys import sainte_lague_algorithm, modified_sainte_lague_algorithm, dhondt_algorithm, hare_algorithm, droop_algorithm
from elecsys import compute_gallagher_index

# Test cases taken from Gallagher & Mitchel's book: "The Politics of Electoral Systems"

N_SEATS = 10
SP = 'Socialist Party'
CRP = 'Centre-right Party'
LP = 'Liberal Party'
GP = 'Green Party'
RRP = 'Radical Right Party'
RP = 'Regionalist Party'
votes = {
        SP: 34000,
        CRP: 25000,
        LP: 15000,
        GP: 12000,
        RRP: 10000,
        RP: 4000
        }

class TestAlgorithm(TestCase):

    def test_sainte_lague(self):
        expected = {
                SP: 3,
                CRP: 3,
                LP: 2,
                GP: 1,
                RRP: 1,
                RP: 0
                }
        result = sainte_lague_algorithm(N_SEATS, votes)
        self.assertEqual(result, expected)

    def test_modified_sainte_lague(self):
        expected = {
                SP: 3,
                CRP: 3,
                LP: 2,
                GP: 1,
                RRP: 1,
                RP: 0
                }
        result = modified_sainte_lague_algorithm(N_SEATS, votes)
        self.assertEqual(result, expected)

    def test_dhondt(self):
        expected = {
                SP: 4,
                CRP: 3,
                LP: 1,
                GP: 1,
                RRP: 1,
                RP: 0
                }
        result = dhondt_algorithm(N_SEATS, votes)
        self.assertEqual(result, expected)

    def test_hare(self):
        expected = {
                SP: 3,
                CRP: 3,
                LP: 2,
                GP: 1,
                RRP: 1,
                RP: 0
                }
        result = hare_algorithm(N_SEATS, votes)
        self.assertEqual(result, expected)

    def test_droop(self):
        expected = {
                SP: 4,
                CRP: 3,
                LP: 1,
                GP: 1,
                RRP: 1,
                RP: 0
                }
        result = droop_algorithm(N_SEATS, votes)
        self.assertEqual(result, expected)

class TestIndex(TestCase):

    def test_gallagher(self):
        v_s = {
                'Fianna Fáil': (703682, 77),
                'Fine Gael': (499936, 54),
                'Labour': (186044, 17),
                'PDs': (83765, 4),
                'Democratic Left': (44901, 4),
                'Green Party': (49323, 2),
                'Sinn Féin': (45614, 1),
                'National Party': (19077, 0),
                'Socialist Party': (12445, 1),
                'Christian Solidarity': (8357, 0),
                'Worker\'s Party': (7808, 0),
                'Others': (128033, 6)
                }
        votes = dict()
        seats = dict()
        for party in v_s:
            votes[party] = v_s[party][0]
            seats[party] = v_s[party][1]
        expected = 6.94
        self.assertEqual(round(compute_gallagher_index(votes, seats), 2), expected)
