import math
import time


def even_fibonacci():
    nterms = int(input("How many terms? "))

    # first two terms
    n1, n2 = 0, 1
    count = 0
    number = 0
    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            if n1 < 4000000 and n1 % 2 == 0:
                number += n1
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1


def factors(n):
    # code made to find the largest prime factor of a number
    big = []
    l = set(x for tup in ([i, n//i]for i in range(1,
                                                  int(n**0.5)+1) if n % i == 0) for x in tup)
    for j in l:
        x = set(x for tup in ([i, j//i] for i in range(1,
                                                       int(n**0.5)+1) if j % i == 0) for x in tup)
        if len(x) == 2:
            big.append(max(x))
    return max(big)


def palindrome(start, finish):
    largest = 100
    for i in range(start, finish):
        for j in range(start, finish):
            x = i*j
            y = str(x)
            if y == ''.join(reversed(y)) and x > largest:
                largest = x
    return largest


def multiple(n):

    # Returns the lcm of first n numbers
    ans = 1
    for i in range(1, n + 1):
        ans = int((ans * i)/math.gcd(ans, i))
    end_time = time.time()
    print(f'done in {end_time-start_time}seconds')
    return ans

    # divs = [x for x in range(1, 20) if n % x == 0]
    # return divs


def squares(n):
    count = 0
    big = 0
    for i in range(1, n+1):
        big += i
        print(count)
        count += i**2
    big = big**2
    print(big)
    return big-count


def adjacent(num, adj):
    # checks a int passed in
    # goes through it by adj
    # and multplies all the adj together
    # returns highest
    nums = list(map(int, list(str(num))))
    arr = []
    for i in range(len(nums)):
        x = nums[i:i+adj]
        if len(x) == adj:
            y = math.prod(x)
            arr.append(y)
    return max(arr)


def primes(n):
    num = 2
    arr = []
    while len(arr) < n:
        for i in range(2, num):
            if num % i == 0:
                num += 1
                break
        else:
            arr.append(num)
            num += 1
    return arr[n-1]


def pyth(limits):
    c, m = 0, 2

    # Limiting c would limit
    # all a, b and c
    while c < limits:

        # Now loop on n from 1 to m-1
        for n in range(1, m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n

            # if c is greater than
            # limit then break it
            if c > limits:
                break
            if int(a)+int(b)+int(c) == 1000:
                print(a, b, c)

        m = m + 1


def primesum(n):
    num = 2
    arr = []
    while num < n:
        for i in range(2, num):
            if num % i == 0:
                num += 1
                break
        else:
            arr.append(num)
            num += 1
    return sum(arr)


def invert(dct):
    new = {}
    for k, v in dct.items():
        new.update({v: k})
    return new


# def triangle(num):
#     arr = [1]
# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


def remove_kth_from_end(head, k):
    current = head
    arr = []
    while current:
        arr.append(current.value)
        current = current.next
    if k == 0 or k > len(arr):
        return arr
    else:
        arr.pop(len(arr)-k)
        return arr


def first_not_repeating_character(s):
    # first we find all the characters
    # then we find out how many times they occur
    # then we fin the ones that only occur once
    # return the one whos index is lower
    x = list(s)
    y = set(x)
    once = []
    ind = []
    for i in y:
        counter = 0
        for j in x:
            if j == i:
                counter += 1
        if counter == 1:
            once.append(i)
    for l in once:
        ind.append(x.index(l))
    if len(ind) == 0:
        return '_'
    else:
        return x[min(ind)]


def uncover_spy(n, trust):
    x = []
    y = []
    for i in trust:
        y.append(i[1])
        x.append(i[0])
    z = [item for item in y if item not in x]
    if len(set(z)) > 1:
        return -1
    else:
        return z[-1]


def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            print(j)
            if nums[i]+nums[j] == target:
                return [i, j]


def sieve(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    # Print all prime numbers
    added = 0
    for p in range(n + 1):
        if prime[p]:
            added += p
    return added


def eratos(n):
    # put out prime @pos 10001
    # building list of primes
    # while loop based on len arr beign less
    prime = [True for i in range(1, n*n)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    # Print all prime numbers
    added = []
    for p in range(n*n-1):
        if prime[p]:
            added.append(p)
    print(added[n-1])


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.s
        """
        self.queue = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.queue.push(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.queue.pop(0)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.queue) == True


def duplicate(self, nums):
    arr = []
    for i in nums:
        if i in arr:
            return i
        else:
            arr.append(i)


class Solution(object):
    def findDuplicate(self, nums):
        arr = []
        for i in nums:
            if i in arr:
                return i
            else:
                arr.append(i)


def encode_morse(message):
    x = message.upper()
    arr = []
    for i in x:
        arr.append(char_to_dots.get(i))
    return ' '.join(arr)


def grid(n):
    x = n.split(' ')
    y = [[]for i in range(20)]
    for i in range(len(x)):
        y[i % 20].append(int(x[i]))
    return y


class Check:
    def __init__(self):
        self.grid = []
        self.big = 32719995
        self.set = []

    def adjacent(self, li, idx):
        # get all down,right diagonalup and down
        # create 4 lists
        ud = []
        dd = []
        do = []
        r = []
        for i in range(4):
            try:
                ud.append(self.grid[li+i][idx-i])
            except IndexError:
                ud.append(1)
            try:
                dd.append(self.grid[li+i][idx+i])
            except IndexError:
                dd.append(1)
            try:
                do.append(self.grid[li][idx+i])
            except IndexError:
                do.append(1)
            try:
                r.append(self.grid[li+i][idx])
            except IndexError:
                r.append(1)
        ra = [ud, dd, do, r]
        for i in ra:
            if math.prod(i) > self.big:
                self.set = i
                self.big = math.prod(i)
        # for loop 4 times
        # multiply lists together
        # put in one list
        # return max of list

    def solve(self):
        for i in range(len(self.grid)):
            for l in range(len(self.grid)):
                self.adjacent(i, l)

    def return_big(self):
        print(self.big)
        print(self.set)

    def add_grid(self, grid):
        self.grid = grid


def triangles(x):
    number = 0
    for l in range(30000):
        number += l
        z = set(x for tup in ([i, number//i]for i in range(1, int(number**0.5)+1) if number % i == 0) for x in tup)
        if len(z) >= x:
            return number

# Find all the pairs of two integers in an unsorted array that sum up to a given S. For example, if the array is [3, 5, 2, -4, 8, 11] and the sum is 7, your program should return [[11, -4], [2, 5]] because 11 + -4 = 7 and 2 + 5 = 7.


def pair(arr, s):
    # create a list
    # forloop
    # for loop
    # if arr both for loops equals s
    # append to created list a list of both
    ret = []
    for i in arr:
        for l in arr[:i]:
            if i+l == s:
                ret.append([i, l])
                arr.pop(arr.index(i))
                arr.pop(arr.index(l))
    return ret


if __name__ == "__main__":
    # print(factors(600851475143))
    # start_time = time.time()
    # x = multiple(20)
    # print(x)
    # end_time = time.time()
    # print(f'done in {end_time-start_time}seconds')
    # print(squares(100))
    # num = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    # print(adjacent(num, 13))
    # print(primes(10001))
    # pyth(1000)
    # print(primesum(2000000))
    # print(invert({"a": 1, "b": 2, "c": 3}))
    # print(first_not_repeating_character('cdohzvslmvruydjxaoubfdtlsrglnrbddrvfjgdvudkkyjlrxopdaeuljszxwxvrmshhhgvulafgtblghrmfptwbhhzndbskjbcmtukqeszkspmymfghntsxbfmzfwayhabrbcpnzpesqhqnmmujwnzvomomdrglnlqaszzkopbefvjsftpfrdfchzovytmhzleasxqgzhvcjmbunbtvscepuakwqpuwbfsdonubkkbnetbczunbyyucmewnyyvpgglegfhnzbllwdxkjsgfdglasgskrhjtglfrhrjbswymucenwerkrrjwmmbzowolwlwadwdksfubvljtttgwtywmqhftnelmeccmypwsafzqvjjrmnosezzgnaehtjgrcjkqmoxkosyhhmvrxjcahjfnjwhwltpkdggpexjjgffdzbhvvcxjobskwcaghfxzrssdnkjbqxztcpgarsytehzpkyoaatkjfuecobygafxvbywwhawubgrgcxkdlcedxwuhdgcvaelchgrtnvynrtywabgypzcluzctgtvhkmoaulvpqlunpnalguezpvlxtwqejdfacplxntakpmhvequphonbokfhrrbcpxuqxlsrtahbuycynampjgmamqdurvvqmkzrlcoacmgdaxqfxrebxoetzplomadhrpwjbvjzlmxogwsqpwrhgaqacprjwtwororcbcdesbqagrkaktleqjycyqazehncyjjrusynatqgadnhmgameosfaplttghsgqbgwxjkpcfrbtnqcrnxmwdqpoebzubpoxfckboaqzmkoxjweqgapxrazukgxxcxzwqncpwvdewgormmdwbheplssmwoenjceynyplmxddsedmluarrlydbtutoqeumlbaxwfjguojzabnghjsxsjwxpmsotlxkchapaakdvmnkcklerctkfpuqkrhbobaebtqhmejyngdyhbyouflfwlfuhxvfgsxtekmou'))
    # print(uncover_spy(4,
    #                   [[1, 3],
    #                    [2, 3]]))
    # print(twoSum([3, 3, 4], 6))
    # print(duplicate([1, 3, 4, 2, 2]))
    # print(encode_morse('HELP ME Sir'))
    # print(palindrome(900, 999))
    # print(sieve(2000000))
    # x = grid('08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48')
    # y = Check()
    # y.add_grid(x)
    # y.solve()
    # y.return_big()
    # print(triangles(500))
    #print(pair([3, 5, 2, -4, 8, 11], 7))
    eratos(10001)
