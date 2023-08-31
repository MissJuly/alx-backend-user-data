#!/usr/bin/env python3
"""
Module for encrypted passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes the password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks hash password
    """
    return  bcrypt.checkpw(password.encode('utf-8'), hashed_password)
