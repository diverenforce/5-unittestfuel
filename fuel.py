def main():
    theFraction = input('Fraction: ').strip()


def convert(fraction):
    numerator, denominator = fraction.split('/')
    return (numerator/denominator) * 100


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()