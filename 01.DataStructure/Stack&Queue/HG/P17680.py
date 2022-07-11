def solution(cacheSize, cities):
    answer = 0
    cache = {}
    for idx, city in enumerate(cities):
        city = city.lower()
        if city in cache:
            cache[city] = idx
            answer += 1
        else: # Not cache
            if len(cache) < cacheSize:
                cache[city] = idx
            elif cacheSize > 0:
                target = ''
                minValue = float('inf')
                for k,v in cache.items():
                    if minValue > v:
                        target = k
                        minValue = v
                # Change Caching
                del cache[target]
                cache[city] = idx
            answer += 5
        # print(answer, cache)


    return answer