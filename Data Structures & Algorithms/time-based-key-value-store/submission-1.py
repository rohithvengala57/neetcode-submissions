class TimeMap:

    def __init__(self):
        self.ref = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ref[key].append((value, timestamp))
    def get(self, key: str, timestamp: int) -> str:
        i = 0
        j = len(self.ref[key]) - 1
        res = ""
        while i<=j:
            mid = (i+j)//2
            if (r:=self.ref[key][mid])[1] <= timestamp:
                res = r[0]
                i = mid + 1
            else:
                j =  mid -1
        return res
