#!/usr/bin/python3
"""UTF-8 validator"""

def validUTF8(data):
    """fucntions checks if a list of integers are valid UTF-8 codepoints.
    See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    """
    skip = 0
    n = len(data)
    for i in range(n):
        if skip > 0:
            skip -= 1
            continue
        if type(data[i]) != int or data[i] < 0 or data[i] > 0x10ffff:
            return False
        elif data[i] <= 0x7f:
            skip = 0
        elif data[i] & 0b11111000 == 0b11110000:
            # 4-byte utf-8 character encoding
            span = 4
            if n - i >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        elif data[i] & 0b11110000 == 0b11100000:
            # 3-byte utf-8 character encoding
            span = 3
            if n - i >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        elif data[i] & 0b11100000 == 0b11000000:
            # 2-byte utf-8 character encoding
            span = 2
            if n - i >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        else:
            return False
    return True

    
# def validUTF8(data):
#     """
#         """

#     data = iter(data)
#     for leading_byte in data:
#         leading_ones = _count_leading_ones(leading_byte)
#         if leading_ones in [1, 7, 8]:
#             return False
#         for _ in range(leading_ones - 1):
#             trailing_byte = next(data, None)
#             if trailing_byte is None or trailing_byte >> 6 != 0b10:
#                 return False
#     return True


# def _count_leading_ones(byte):
#     """Counts the leading ones."""

#     for i in range(8):
#         if byte >> 7 - i == 0b11111111 >> 7 - i & ~1:
#             return i