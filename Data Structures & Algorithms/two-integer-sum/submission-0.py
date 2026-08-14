class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Speichert bereits gesehene Zahlen und deren Indizes
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Prüfen, ob das Gegenstück bereits im Dictionary existiert
            if complement in seen:
                # Gibt den kleineren Index zuerst zurück
                return [seen[complement], i]
            
            # Aktuelle Zahl mit ihrem Index speichern
            seen[num] = i

        