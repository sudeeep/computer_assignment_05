import datetime
print(datetime.datetime.now())
# Store function
def store(storage, elm):
    storage.update(elm)
    return storage

# Immediate Load
def imm_load_ac(val):
    return val

# Direct Load
def dir_load_ac(storage, val):
    return storage.get(val, None)

# Indirect Load
def indir_load_ac(storage, val):
    address = storage.get(val, None)
    return storage.get(address, None) if address else None

# Indexed Load
def idx_load_ac(storage, idx, val):
    effective_address = val + idx
    return storage.get(effective_address, None)

# Initialize memory
init_mem = {}
mem = store(init_mem, {800: 123})  # mem = {800: 123}
mem = store(mem, {900: 1000})     # mem = {800: 123, 900: 1000}
mem = store(mem, {800: 900})      # mem = {800: 900, 900: 1000}
mem = store(mem, {1500: 700})     # mem = {800: 900, 900: 1000, 1500: 700}

# Test cases
ac = imm_load_ac(800)  # ac = 800
print(ac)
ac = dir_load_ac(mem, 800)  # ac = 900
print(ac)
ac = indir_load_ac(mem, 800)  # ac = 1000
print(ac)
idxreg = 700

ac = idx_load_ac(mem, idxreg, 800)
print(ac)  # ac should be the value at address 1500

print("Accumulator Value (Indexed Load):", ac)
