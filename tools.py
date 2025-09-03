def calculate(operation):
    return eval(operation)

def get_planet_mass(planet) -> float:
    match planet.lower():
        case "mercury":
            return 3.3011e23
        case "venus":
            return 4.8675e24
        case "earth":
            return 5.97237e24
        case "mars":
            return 6.4171e23
        case "jupiter":
            return 1.8982e27
        case "saturn":
            return 5.6834e26
        case "uranus":
            return 8.6810e25
        case "neptune":
            return 1.02413e26



