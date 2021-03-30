def range(a, b=None, c=None):
    '''
    This function should behave exactly like the built-in range function.
    For example:

    >>> list(range(5))
    [0, 1, 2, 3, 4]
    >>> list(range(1, 5))
    [1, 2, 3, 4]
    >>> list(range(1, 5, 2))
    [1, 3]

    HINT:
    If you can figure out how to use the
    built-in range function (without modifying
    the test cases!),
    then feel free to do so.
    That's fairly difficult to do, however,
    and it's much easier to just implement this
    function normally using the yield syntax.

    NOTE:
    For efficiency reasons, Python's built-in
    range object is written in the C programming
    language rather than natively in python.
    You can find the source code online at
    https://hg.python.org/cpython/file/ee7b713fec71/Objects
    /rangeobject.c
    The link takes you to a file that is 1445 lines long,
    and all it does is implement this simple functionality.
    My easy to read Python implementation of this
    function is just 15 lines long.
    (And with some code golf I also wrote a less readable
    version that is only 4 lines.)
    It is very common for C programs to be 100x longer
    than their corresponding python programs.
    C code must manage lots of details about the computer
    manually that python code automates for you.
    Carefully written C code can be faster than the
    corresponding python code because it can remove some
    of the overhead of this automation process,
    but the resulting code is much longer and harder to
    read/write.
    '''
    if b is None:
        v1 = 0
        v2 = a
        while v1 < v2:
            v1 += 1
            yield v1 - 1
    elif b is not None and c is None:
        v1 = a
        v2 = b
        while v1 < v2:
            v1 += 1
            yield v1 - 1
    elif b is not None and c is not None:
        v1 = a
        v2 = b
        if v1 > v2:
            if c > 0:
                return []
            elif c < 0:
                while v1 > v2:
                    v1 += c
                    yield v1 - c
        elif v2 > v1:
            while v1 < v2:
                if c < 0:
                    return []
                elif c > 0:
                    v1 += c
                    yield v1 - c
