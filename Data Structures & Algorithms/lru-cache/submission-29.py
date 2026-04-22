class LL:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.node = LL(-1, -1)
        self.length = capacity

    def get(self, key: int) -> int:
        print(key, "get")
        
        if r:=self.cache.get(key):
            print("found")
            r.left.right, r.right.left = r.right, r.left
            r.left = self.node
            r.right = self.node.right
            self.node.right.left = r
            self.node.right = r
            start = self.node.right
            while start:
                print(start.key, start.val)
                start=start.right
                if start == self.node.right:
                    break
            return r.val

        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        print(key, value, "put")
        start = self.node.right
        # while start:
        #     print(start.key, start.val)
        #     start=start.right
        #     if start == self.node.right:
        #         break
        # print("xxxxx")
        # start = self.node.left
        # while start:
        #     print(start.key, start.val)
        #     start=start.left
        #     if start == self.node.left:
        #         break
        if r:=self.cache.get(key):
            r.val = value
            r.left.right, r.right.left = r.right, r.left
            r.left = self.node
            r.right = self.node.right
            self.node.right.left = r
            self.node.right = r
            start = self.node.right
        else:
            r=LL(key, value)
            self.cache[key] = r
            r.left = self.node
            r.right = self.node.right
            if self.node.right and not self.node.right.left:
                self.node.right.left = r
            self.node.right = r
            if r.right:
                r.right.left = r
            if not self.node.left:
                print(key, value, "---")
                self.node.left = r
                r.right = self.node
            
            
            if self.length <= 0:
                deletednode = self.node.left
                del self.cache[deletednode.key]
                self.node.left = self.node.left.left
                self.node.left.right = self.node
                
            else:
                self.length -= 1
            start = self.node.right
            print(self.cache.keys())
            # while start:
            #     print(start.key, start.val)
            #     start=start.right
            #     if start == self.node.right:
            #         break
            # start = self.node.left
            # print("xxxxxx")
            # while start:
            #     print(start.key, start.val)
            #     start=start.left
            #     if start == self.node.left:
            #         break
            

