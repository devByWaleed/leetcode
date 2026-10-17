class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        def get_prime(n):
            # boolean list tracking potential primes
            is_prime = [True] * (n + 1)

            # Mark 0 and 1 as non-prime
            is_prime[0] = is_prime[1] = False

            # Loop up to the square root of n
            for i in range(2, int(n**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False

            # Final list
            return [num for num, prime in enumerate(is_prime) if prime]

        prime_list = get_prime(n)

        # Get the prime number window
        total = 0
        count = 0
        for num in prime_list:
            # count sum
            total += num

            # If sum exceeded, break
            if total > s:
                break

            # If sum is in range, increase window
            count += 1

        # Return array of specific range
        return prime_list[0:count]
        

obj = Solution()
print(obj.maxPrimes(7))
print(obj.maxPrimes(20))
print(obj.maxPrimes(15))
print(obj.maxPrimes(15))
print(obj.maxPrimes(5))
print(obj.maxPrimes(1))

# T.C:  O(N)    --> checking for prime numbers + counting
# S.C:  O(N)    --> Array used for N numbers


# Brute-Force
'''
import math

class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        # Edge case
        # if n > s:
        #     return []

        # Function to check prime numbers
        def is_prime(n):
            if n == 2:
                return True
        
            if n % 2 == 0:
                return False
            
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                if n % i == 0:
                    return False
                    
            return True


        prime_list = [num for num in range(2, n + 1) if is_prime(num)]


        # Get the prime number window
        total = 0
        count = 0
        for num in prime_list:
            # count sum
            total += num

            # If sum exceeded, break
            if total > s:
                break

            # If sum is in range, increase window
            count += 1

        # Return array of specific range
        return prime_list[0:count]
        

obj = Solution()
print(obj.maxPrimes(675995, 320213177))
print(obj.maxPrimes(15, 15))
print(obj.maxPrimes(7, 20))
print(obj.maxPrimes(5,1))
print(obj.maxPrimes(3,2))
'''