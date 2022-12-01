"""BreakPassword"""
import hashlib as h
def passed(password):
    """BreakPassword"""
    for word in range(100000):
        hash_b = (h.sha512(str("%05d"%word).encode("utf-8")).hexdigest()).upper()
        if hash_b == password:
            print("%05d"%word)
            break
passed(input())
