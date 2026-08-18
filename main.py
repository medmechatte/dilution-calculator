def dilution_concentration(c1, v1, v2):
    """Calculate final concentration after dilution (C1V1=C2V2)."""
    return (c1*v1)/v2

if __name__ == "__main__":
    c1 = float(input("initial concentration (C1): "))
    v1 = float(input("initial volume (V1): "))
    v2 = float(input("Final volume (V2)"))
    print(f"Final concentration: {dilution_concentration(c1, v1, v2):.4f}")
