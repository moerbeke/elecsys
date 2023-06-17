'''
Copyright (C) 2023 Antonio Ceballos Roa

elecsys - Apply electoral systems to compute seats from votes.
'''

class BadSeats(Exception):
    pass

class BadVotes(Exception):
    pass

class BadMethod(Exception):
    pass

def sainte_lague_algorithm(n_seats, votes):
    divisors = [2*n-1 for n in range(1, n_seats + 1)]
    return highest_averages(divisors, votes)

def modified_sainte_lague_algorithm(n_seats, votes):
    divisors = [1.4] + [2*n-1 for n in range(2, n_seats + 1)]
    return highest_averages(divisors, votes)

def dhondt_algorithm(n_seats, votes):
    divisors = [n for n in range(1, n_seats + 1)]
    return highest_averages(divisors, votes)

def hare_algorithm(n_seats, votes):
    quota = sum(votes.values()) / n_seats
    return highest_reminder(n_seats, quota, votes)

def droop_algorithm(n_seats, votes):
    quota = 1 + sum(votes.values()) / (1 + n_seats)
    return highest_reminder(n_seats, quota, votes)

def highest_averages(divisors, votes):
    ratio = dict()
    for electoral_list in votes:
        list_votes = votes[electoral_list]
        for i in range(len(divisors)):
            divisor = divisors[i]
            ratio[(electoral_list, i)] = list_votes / divisor
    ratios = [r[0] for r in dict(sorted(ratio.items(), key = lambda x: x[1], reverse=True))]
    result = dict()
    for r in range(len(divisors)):
        electoral_list = ratios[r][0]
        try:
            result[electoral_list] += 1
        except KeyError:
            result[electoral_list] = 1
    result = complete_empty_lists(result, votes)
    return result

def highest_reminder(n_seats, quota, votes):
    result = dict()
    reminder = dict()
    for electoral_list in votes:
        list_votes = votes[electoral_list]
        ratio = int(list_votes / quota)
        result[electoral_list] = ratio
        reminder[electoral_list] = list_votes % quota
    n_spare = n_seats - sum(result.values())
    highest_reminders = [r[0] for r in dict(sorted(reminder.items(), key = lambda x: x[1], reverse=True))][:n_spare]
    for electoral_list in highest_reminders:
        result[electoral_list] += 1
    return result

def complete_empty_lists(result, votes):
    sorted_result = dict()
    for electoral_list in votes:
        try:
            sorted_result[electoral_list] = result[electoral_list]
        except KeyError:
            sorted_result[electoral_list] = 0
    return sorted_result

SL = 'sl'  # Sainte-Laguë
MS = 'ms'  # Modified Sainte-Laguë
DH = 'dh'  # D'Hondt
HA = 'ha'  # Hare
DR = 'dr'  # Droop

algorithm = {
        SL: sainte_lague_algorithm,
        MS: modified_sainte_lague_algorithm,
        DH: dhondt_algorithm,
        HA: hare_algorithm,
        DR: droop_algorithm,
        }

def compute_gallagher_index(votes, result):
    n_total_votes = sum(votes.values())
    n_total_seats = sum(result.values())
    s = 0
    for electoral_list in votes:
        vi = votes[electoral_list] / n_total_votes
        if vi > 0:
            si = result[electoral_list] / n_total_seats
            s += (vi - si) ** 2
    index = (s / 2) ** .5
    return index

def compseats(n_seats, votes, method, index):
    # Check input
    if n_seats < 1:
        raise BadSeats
    for electoral_list in votes:
        if votes[electoral_list] < 0:
            raise BadVotes
    if method not in algorithm:
        raise BadMethod
    result = dict()
    # Invoke algorithm
    result['seats'] = algorithm[method](n_seats, votes)
    # Compute index
    if index:
        result['gallagher_index'] = compute_gallagher_index(votes, result['seats'])
    return result
