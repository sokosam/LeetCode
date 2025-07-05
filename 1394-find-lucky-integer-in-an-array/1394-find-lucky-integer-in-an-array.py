class Solution:
    findLucky = lambda self, arr : (lambda c: max([-1] + [c[k] for k in c if k == c[k]]))(Counter(arr))
