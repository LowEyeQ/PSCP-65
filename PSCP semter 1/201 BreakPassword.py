"""BreakPassword"""
import hashlib as h
import sys
def passed(password):
    """BreakPassword"""
    for word in password:
        hash_b = h.sha512(password).hexdigest()


passed(input())
