from argparse import ArgumentParser
from collections import Counter



class General:
    def __init__(self, id, is_traitor=False):
        self.id = id
        self.other_generals = []
        self.orders = []
        self.is_traitor = is_traitor

    def __call__(self, m, order):
        """When a general is called, it acts as the commander,
        and begins the OM algorithm by passing its command to
        all the other generals.

        Args:
            m (int): The level of recursion.
            order (str): The order, such that order ∈ {"ATTACK","RETREAT"}.

        """
        self.om_algorithm(commander=self,
                          m=m,
                          order=order,
                          )

    def _next_order(self, is_traitor, order, i):
        """A helper function to determine what each commander
        should pass on as the next order. Traitors will pass-
        on the opposite command if the index of the general
        in their `other_generals` list is odd.

        Args:
            is_traitor (bool): True for traitors.
            order (str): The received order, such that
                order ∈ {"ATTACK","RETREAT"}.
            i(int): The index of the general in question.

        Returns:
            str: The resulting order ("ATTACK" or "RETREAT").

        """
        if is_traitor:
            if i % 2 == 0:
                return "ATTACK" if order == "RETREAT" else "RETREAT"
        return order

    def om_algorithm(self, commander, m, order):
        """The OM algorithm from Lamport's paper.

        Args:
            commander (General): A reference to the general
                who issued the previous command.
            m (int): The level of recursion .
            order (str): The received order, such that
                order ∈ {"ATTACK","RETREAT"}.

        """
        if m < 0:
            self.orders.append(order)
        elif m == 0:
            for i, l in enumerate(self.other_generals):
                l.om_algorithm(
                    commander=self,
                    m=(m - 1),
                    order=self._next_order(self.is_traitor, order, i)
                )
        else:
            for i, l in enumerate(self.other_generals):
                if l is not self and l is not commander:
                    l.om_algorithm(
                        commander=self,
                        m=(m - 1),
                        order=self._next_order(self.is_traitor, order, i)
                    )

    @property
    def decision(self):
        """Returns a tally of the General's received commands.

        """
        c = Counter(self.orders)
        return c.most_common()

