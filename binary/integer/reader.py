from struct import unpack_from


def read_bit8(data, offset=0):
    """Write a signed 8 bit integer

    Args:
        data (bytes)

    Returns:
        int
    """
    return unpack_from('c', data, offset)[1]


def read_bit16(data, offset=0):
    """Write a signed 16 bit integer

    Args:
        data (bytes)

    Returns:
        int
    """
    return unpack_from('s', data, offset)[1]


def read_bit32(data, offset=0):
    """Write a signed 32 bit integer

    Args:
        data (bytes)

    Returns:
        int
    """
    return unpack_from('l', data, offset)[1]


def read_bit64(data, offset=0):
    """Write a signed 64 bit integer

    Args:
        data (bytes)

    Returns:
        int
    """
    return unpack_from('q', data, offset)[1]
