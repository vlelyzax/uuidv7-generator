import time, os
def generate_uuid7() -> str:
    ts = int(time.time() * 1000)
    rnd = os.urandom(10)
    return f'{ts:012x}-{rnd[:2].hex()}-7{rnd[2:4].hex()[1:]}-8{rnd[4:6].hex()[1:]}-{rnd[6:].hex()}'
