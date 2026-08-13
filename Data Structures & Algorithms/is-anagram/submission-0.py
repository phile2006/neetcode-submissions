class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Wenn die Länge ungleich ist, kann es kein Anagramm sein (Frühzeitiger Abbruch)
        if len(s) != len(t):
            return False
            
        counts_hashmap = {}
        
        # splitS und splitT werden hier gar nicht benötigt, da wir direkt über die Strings iterieren
        
        # Buchstaben von 's' hochzählen
        for x in s:
            counts_hashmap[x] = counts_hashmap.get(x, 0) + 1
        
        # Buchstaben von 't' wieder abziehen
        for x in t:
            counts_hashmap[x] = counts_hashmap.get(x, 0) - 1

        # Wenn alle Werte in der HashMap 0 sind, ist es ein Anagramm
        for count in counts_hashmap.values():
            if count != 0:
                return False
                
        return True
