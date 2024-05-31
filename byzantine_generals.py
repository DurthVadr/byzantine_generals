from argparse import ArgumentParser
from collections import Counter

from general import General



    


def init_generals(generals_spec):
    
    generals = []
    for i, spec in enumerate(generals_spec):
        general = General(i)
        if spec == "l":  # Loyal
            pass
        elif spec == "t": # Traitor
            general.is_traitor = True
        else:
            print("Error, bad input in generals list: {}".format(generals_spec))
            exit(1)
        generals.append(general)
    # Add list of other generals to each general.
    for general in generals:
        general.other_generals = generals
    return generals


def print_decisions(generals):
    for i, l in enumerate(generals):
        print("General {}: {}".format(i, l.decision))


def main():
    parser = ArgumentParser()
    parser.add_argument("-m", type=int, dest="recursion",
                        help=" The level of recursion in the algorithm, where M > 0. This variable "
                             "will be used for om_algorithm. om_algorithm(M) means this algorithm solves "
                             "the problem if there are more than 3M generals while there are at most "
                             "M traitors amongst the generals")
    parser.add_argument("-G", type=str, dest="generals",
                        help=" A string of generals (ie 'l,t,l,l,l'...), where l is loyal and t is a traitor.  "
                             "The first general is the Commander.")
    parser.add_argument("-O", type=str, dest="order",
                        help=" The order the commander gives to the other generals (O ∈ {ATTACK,RETREAT})")
    args = parser.parse_args()

    generals_spec = [x.strip() for x in args.generals.split(',')]
    generals = init_generals(generals_spec=generals_spec)
    generals[0](m=args.recursion, order=args.order)
    print_decisions(generals)


if __name__ == "__main__":
    
    #usage: byzantine_generals.py [-h] [-m RECURSION] [-G GENERALS] [-O ORDER]
    #python3 byzantine_generals.py -m 4 -G l,t,l,l,l -O ATTACK -> this is for initial demonstration should give weird results
    #python3 byzantine_generals.py -m 3 -G l,l,l,t,t,l,l,t,l,l -O ATTACK ->this is for second condition holds because generals > 3m traitors
    #python3 byzantine_generals.py -m 3 -G l,l,l,t,t,l,l,t,l -O ATTACK  -> they should not reach consensus because generals < 3m traitors

    
    main()
