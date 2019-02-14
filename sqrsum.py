def sqrsum(n):
    if n<=0 or n>50:
        return print('TRY BETWEEN 1 AND 50')
    DJ = {}
    squares = []
    results = []
    for i in range(1,n+1):
        DJ[i] = []
    for i in range (1,(n+n)):
        import math
        if math.sqrt(i)==int(math.sqrt(i)):
            squares.append(i)
    for i in DJ:
        for j in squares:
            if j-i in DJ:
                C = j-i
                if C!=i:
                    DJ[i].append(C)
    def paths(graph, v):
        path = [v]
        seen = {v}
        def search():
            dead_end = True
            for neighbour in graph[path[-1]]:
                if neighbour not in seen:
                    dead_end = False
                    seen.add(neighbour)
                    path.append(neighbour)
                    yield from search()
                    path.pop()
                    seen.remove(neighbour)
            if dead_end:
                yield list(path)
        yield from search()
    for i in range(1, n+1):
        if len(DJ[i])==1:
            for j in sorted(paths(DJ,i)):
                if len(j)==n:
                    results.append(j)
    if results==[]:
        return print ('NO RESULTS')
    for i in results:
        print(i)
