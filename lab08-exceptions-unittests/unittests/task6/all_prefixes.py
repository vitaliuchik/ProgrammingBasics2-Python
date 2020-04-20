def all_prefixes(s):
    """Returns set of all prefixes started with the first letter
    str -> set"""
    first_letter = s[0]
    sub_s = set()
    for i in range(len(s)):
        if s[i] == first_letter:
            for j in range(i+1, len(s) + 1):
                sub_s.add(s[i:j])
    return sub_s

