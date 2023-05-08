'''
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

'''

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
      
        '''
        So according to the question. The judge trusts nobody i.e., the number of outward egdes must be zero and everyone else trusts the judge i.e.,
        the number of inward egdes is n-1.
        So we can keep an array degree and calculate the absolute degree and figure out if there exist a judge.
        '''
        trust_to, trusted = defaultdict(int), defaultdict(int)

        for a, b in trust:
            trust_to[a] += 1
            trusted[b] += 1
        
        for i in range(1, n+1):
            if trust_to[i] == 0 and trusted[i] == n - 1:
                return i
        
        return -1
