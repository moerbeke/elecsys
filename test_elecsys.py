'''
Copyright (C) 2023 Antonio Ceballos Roa

elecsys - Apply electoral systems to compute seats from votes.
'''

from unittest import TestCase

from elecsys import sainte_lague_algorithm, modified_sainte_lague_algorithm, dhondt_algorithm, hare_algorithm, droop_algorithm

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

    def setUp(self):
        pass

    def tearDown(self):
        pass

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
