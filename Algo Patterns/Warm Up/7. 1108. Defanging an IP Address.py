class Solution:
    def defangIPaddr(self, address: str) -> str:
        newAddress = address.replace('.','[.]')
        return newAddress