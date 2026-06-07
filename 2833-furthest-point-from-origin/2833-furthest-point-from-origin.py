from collections import Counter
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        moves = list(moves)
        moves_blank = [i for i in moves if i != "_"]
        
        if not moves_blank:
            x = "L"
        else:
            moves_counter = Counter(moves_blank)
            x = max(moves_counter, key=moves_counter.get)
        
        for i in range(len(moves)):
            if moves[i] == "_":
                moves[i] = x
        
        return abs(moves.count("L") - moves.count("R"))      