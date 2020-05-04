import sys

arguments = sys.argv

if (len(arguments) != 2):
    print("usage: primes.py integer")

else:
    input_number = int(sys.argv[1])
    
    # make a list of known primes
    primes = [2]

    # get odd numbers starting from 3 and going up to input_number
    odd_candidates = [n for n in range(3, input_number + 1) if n % 2 == 1]

    # check whether each odd number is prime by comparing against known primes
    for candidate in odd_candidates:

        # assume is prime for now
        candidate_is_prime = True

        # check existing list of primes
        for prime in primes:

            # if the candidate has one of the primes as a factor, it cannot be prime
            if candidate % prime == 0:
                candidate_is_prime = False
                break
        
        # candidate is prime; add to list of known primes
        if candidate_is_prime:
            primes.append(candidate)
    
    # if input is the last number in the list of known primes, return a message saying so
    if primes[-1] == input_number:
        print(input_number, "is prime")
    else:
        print(input_number, "is not prime")