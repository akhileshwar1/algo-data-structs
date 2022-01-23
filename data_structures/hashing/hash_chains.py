# python3
class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.chains = [[] for i in range(self.bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        if(len(chain) == 0):
            print()
        else:
            print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(self.chains[query.ind])

        else:
            try:
                pos = self._hash_func(query.s)
                # ind = self.elems.index(query.s)
            except ValueError:
                pos = -1
            if query.type == 'find':
                for elem in self.chains[pos]:
                    if elem == query.s:
                        return self.write_search_result(True)
                return self.write_search_result(False)
            elif query.type == 'add':
                if query.s not in self.chains[pos]:
                    self.chains[pos].insert(0, query.s)
            else:
                if query.s in self.chains[pos]:
                    self.chains[pos].remove(query.s)


    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
