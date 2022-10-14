def main(a):
    """check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    x = pow(a,1/2)
    return x % 2 == 0
print(main(4))