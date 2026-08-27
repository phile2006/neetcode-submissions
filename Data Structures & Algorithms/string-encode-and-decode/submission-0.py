class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded = []

        for s in strs:
            encoded.append(f"{len(s)}#{s}")

        return "".join(encoded)

    def decode(self, encoded: str) -> list[str]:
        decoded = []
        i = 0

        while i < len(encoded):
            j = i

            while encoded[j] != "#":
                j += 1

            length = int(encoded[i:j])

            start = j + 1
            end = start + length

            decoded.append(encoded[start:end])

            i = end

        return decoded