from enum import Enum


class Operation(Enum):
    """Operations"""

    DELETED = 1
    INSERTED = 2
    SUBSTITUTED = 3

    #def __str__(self):
    #    return str(self.name.lower())


def distances(a, b):
    """Calculate edit distance from a to b"""
    L = []
    L.append([(0, "None")])
    for i in range(1, len(b)+1):
        L[0].append((i, Operation.DELETED))    
    for i in range(1, len(a)+1):
        L.append([(i, Operation.DELETED)])
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1) :
            cost = min(L[i][j-1][0], L[i-1][j][0], L[i-1][j-1][0])
            if cost==L[i][j-1][0] :
                L[i].append((cost+1, Operation.INSERTED))
            elif cost==L[i-1][j][0] :
                L[i].append((cost+1, Operation.DELETED))
            elif cost==L[i-1][j-1][0] :
                if a[i-1]==b[j-1] :
                    L[i].append((cost, Operation.SUBSTITUTED))
                else :
                    L[i].append((cost+1, Operation.SUBSTITUTED))
    return L