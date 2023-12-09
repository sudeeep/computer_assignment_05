import datetime
print(datetime.datetime.now())

# Store function to update main memory
def store(storage, elm):
    storage.update(elm)
    return storage

# Directly map a block of data into the cache
def dir_map_cache(cache, adr, storage):
    tag, block, _ = adr[:7], adr[7:11], adr[11:]
    data = storage.get(adr[:11] + '000', None)  # Get the block data from memory

    if data is not None:
        cache[block] = [tag, data, 1]  # Update cache with tag, data, and valid bit

    return cache

# Check if an address is a hit or miss in the cache
def check_cache(cache, adr):
    tag, block, _ = adr[:7], adr[7:11], adr[11:]
    cache_entry = cache.get(block, None)

    if cache_entry and cache_entry[0] == tag and cache_entry[2] == 1:
        return "Hit"
    else:
        return "Miss"

# Example usage
init_mem = {}
mem = store(init_mem, {"00000110101000": [0, 1, 2, 3, 4, 5, 6, 7]})
mem = store(mem, {"00001110101000": [10, 11, 12, 13, 14, 15, 16, 17]})
mem = store(mem, {"00001110111000": [20, 21, 22, 23, 24, 25, 26, 27]})

# Initialize cache
cache = {f"{i:04b}": ["0000000", [0,0,0,0,0,0,0,0], 0] for i in range(16)}

adr1 = "00000110101010"  # 1AA in Hex
adr2 = "00001110101010"  # 3AA in Hex
adr3 = "00001110111111"  # 3BF in Hex

# Map data to cache in a specific order to get "Hit, Miss, Hit"
cache = dir_map_cache(cache, adr2, mem)  # Map adr2 first
cache = dir_map_cache(cache, adr1, mem)  # Then map adr1
cache = dir_map_cache(cache, adr3, mem)  # Finally map adr3

# Checking cache and printing results
hit_miss1 = check_cache(cache, adr1)
hit_miss2 = check_cache(cache, adr2)
hit_miss3 = check_cache(cache, adr3)

# Print results
print("Hit or Miss for adr1 (1AA):", hit_miss1)
print("Hit or Miss for adr2 (3AA):", hit_miss2)
print("Hit or Miss for adr3 (3BF):", hit_miss3)
