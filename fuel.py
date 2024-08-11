def main():
    while True:
        theFraction = input('Fraction: ').strip()


def convert(fraction):
    numerator, denominator = fraction.split('/')
    
    try:
        percentage = int(numerator)/int(denominator) * 100
    except (ValueError, ZeroDivisionError):
        return
    else:
        if percentage > 100:
            return
        else:
            return percentage


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()