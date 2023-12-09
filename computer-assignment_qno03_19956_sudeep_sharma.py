# Function to store data in memory
import datetime
print(datetime.datetime.now())
def store(storage, elm):
    storage.update(elm)
    return storage

# Function for fully associative cache mapping
def fully_ass_cache(cache, adr, storage):
    tag = adr[:11]  # 11-bit tag
    data = storage.get(adr[:11] + '000', None)  # Get the block data from memory

    if data is not None:
        # Find an available cache line or replace an existing one
        for cache_line_key in cache:
            cache_line = cache[cache_line_key]
            if cache_line[2] == 0:  # Check if the valid bit is 0 (available)
                cache_line[0] = tag  # Set the tag
                cache_line[1] = data  # Set the data
                cache_line[2] = 1  # Set the valid bit to 1 (occupied)
                return cache

        # If all cache lines are occupied, replace the first one (simple replacement policy)
        first_key = list(cache.keys())[0]
        cache[first_key] = [tag, data, 1]

    return cache

# Initialize memory and cache
init_mem = {}
cache = {"blk0": ["00000000000", [0,0,0,0,0,0,0,0], 0],
         "blk1": ["00000000000", [0,0,0,0,0,0,0,0], 0],
         "blk2": ["00000000000", [0,0,0,0,0,0,0,0], 0],
         "blk3": ["00000000000", [0,0,0,0,0,0,0,0], 0]}

# Store blocks in memory
a = {"00000110101000": [0, 1, 2, 3, 4, 5, 6, 7]}
b = {"00001110101000": [10, 11, 12, 13, 14, 15, 16, 17]}
c = {"00011110101000": [20, 21, 22, 23, 24, 25, 26, 27]}
d = {"00111110101000": [30, 31, 32, 33, 34, 35, 36, 37]}
e = {"01111110101000": [40, 41, 42, 43, 44, 45, 46, 47]}
mem = store(init_mem, a)
mem = store(mem, b)
mem = store(mem, c)
mem = store(mem, d)
mem = store(mem, e)

# Map addresses to cache
adr1 = "00000110101010"  # hex address: 1AA
adr2 = "00001110101010"  # hex address: 3AA
adr3 = "00011110101111"  # hex address: 7AF
adr4 = "00111110101101"  # hex address: FAD
adr5 = '01111110101110'  # hex address: 1FAE

cache = fully_ass_cache(cache, adr1, mem)
cache = fully_ass_cache(cache, adr2, mem)
cache = fully_ass_cache(cache, adr3, mem)
cache = fully_ass_cache(cache, adr4, mem)
cache = fully_ass_cache(cache, adr5, mem)

# Print the final state of the cache
print(cache)
