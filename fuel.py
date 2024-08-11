def main():
    while True:
        theFraction = input('Fraction: ').strip()
        percentage = convert(theFraction)
        if percentage == None:
            continue
        else:
            break


def convert(fraction):
    numerator, denominator = fraction.split('/')
    
    try:
        percentage = int(numerator)/int(denominator) * 100
    except (ValueError, ZeroDivisionError):
        return None
    else:
        if percentage > 100:
            return None
        else:
            return round(percentage)


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()