def main():
    while True:
        theFraction = input('Fraction: ').strip()
        percentage = convert(theFraction)
        if percentage == None:
            continue
        else:
            break

    gauge_output = gauge(percentage)
    if gauge_output.isalpha():
        print(gauge_output)
    else:
        print(f"{gauge_output}%")


def convert(fraction):
    try:
        numerator, denominator = fraction.split('/')
    except ValueError:
        return None
    
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
    if percentage > 98:
        return 'F'
    elif percentage < 2:
        return 'E'
    else:
        return percentage


if __name__ == "__main__":
    main()