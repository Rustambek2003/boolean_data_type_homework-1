def main(a):
    """
    check the whole number. Integers are 0 and a positive number.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return a >= 0 and a % 2 == 0 or a % 2 ==1
print(main(5))