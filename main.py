def greetin():
    print("Hello, World!")


def calculate_pi(digits=5):
    """
    Calculate pi to the specified number of digits using the Machin formula.
    Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    
    Args:
        digits: Number of decimal digits to calculate (default: 5)
    
    Returns:
        float: Approximation of pi to the specified digits
    """
    from decimal import Decimal, getcontext
    
    # Set precision high enough to calculate the required digits
    getcontext().prec = digits + 10
    
    def arctan(x, num_terms=100):
        """Calculate arctan using Taylor series expansion"""
        x = Decimal(x)
        power = x
        result = power
        for n in range(1, num_terms):
            power *= -x * x
            result += power / (2 * n + 1)
        return result
    
    # Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    pi = 4 * (4 * arctan(Decimal(1)/Decimal(5), 150) - arctan(Decimal(1)/Decimal(239), 150))
    
    # Round to the specified number of digits
    return round(float(pi), digits)