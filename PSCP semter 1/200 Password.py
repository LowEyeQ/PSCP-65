"""PASSWORD"""
import hashlib as h
def passes():
    """PASSWORD"""
    hashed = h.sha512(str(input()).encode("utf-8")).hexdigest().upper()
    print(hashed)
passes()
