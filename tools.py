tools = [
    {
        "type": "function",
        "name": "calculate",
        "description": "Evaluate a mathematical expression and return the result.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "operation": {
                    "type": "string",
                    "description": "A valid Python expression, e.g., '2 * 5.972e24'."
                }
            },
            "required": ["operation"],
            "additionalProperties": False  # ✅ ensures no extra keys
        },
    },
    {
        "type": "function",
        "name": "get_planet_mass",
        "description": "Get the mass of a planet in kilograms.",
        "parameters": {
            "type": "object",
            "properties": {
                "planet": {
                    "type": "string",
                    "description": "The name of a planet, e.g., Earth, Mars, Jupiter."
                }
            },
            "required": ["planet"],
            "additionalProperties": False  # ✅ ensures no extra keys
        },
    },
]



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


tools_registry = {
    "calculate":calculate,
    "get_planet_mass":get_planet_mass
}
