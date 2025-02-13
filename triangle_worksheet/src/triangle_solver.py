import random
import json
import math

def generate_random_angle(min_degrees, max_degrees, round_to_degrees=2):
    return round(random.uniform(min_degrees, max_degrees), round_to_degrees)

def law_of_cosines_for_side(side_A, side_B, angle_C):
    return math.sqrt(side_A**2 + side_B**2 - 2 * side_A * side_B * math.cos(math.radians(angle_C)))

def law_of_cosines_for_angle(side_A, side_B, side_C):
    return math.degrees(math.acos((side_A**2 + side_B**2 - side_C**2) / (2 * side_A * side_B)))

def law_of_sines_for_side(side_A, angle_A, angle_B):
    return side_A * math.sin(math.radians(angle_B)) / math.sin(math.radians(angle_A))

def law_of_sines_for_angle(side_A, angle_A, side_B):
    return math.degrees(math.asin(side_B * math.sin(math.radians(angle_A)) / side_A))

def generate_triangle():
    triangle_types = {
        "SSS": lambda: {"side_A": random.uniform(5, 20), "side_B": random.uniform(5, 20), "side_C": random.uniform(5, 20)},
        "SSA": lambda: {"side_A": random.uniform(5, 20), "side_B": random.uniform(5, 20), "angle_A": generate_random_angle(10, 80)},
        "SAS": lambda: {"side_A": random.uniform(5, 20), "side_B": random.uniform(5, 20), "angle_C": generate_random_angle(20, 140)},
        "ASA": lambda: {"angle_A": generate_random_angle(20, 80), "angle_B": generate_random_angle(20, 80), "side_C": random.uniform(5, 20)},
        "AAS": lambda: {"angle_A": generate_random_angle(10, 80), "angle_B": generate_random_angle(10, 80), "side_A": random.uniform(5, 20)},
        "AAA": lambda: (lambda angle_A, angle_B: {"angle_A": angle_A, "angle_B": angle_B, "angle_C": 180 - (angle_A + angle_B)}) (generate_random_angle(30, 60), generate_random_angle(30, 60))
    }
    triangle_type = random.choice(list(triangle_types.keys()))
    return {"type": triangle_type, "knowns": triangle_types[triangle_type](), "solved": {}}

def solve_triangle(triangle_data):
    knowns = triangle_data["knowns"]
    solved = {}
    
    match triangle_data["type"]:
        case "SSS":
            side_A, side_B, side_C = knowns["side_A"], knowns["side_B"], knowns["side_C"]
            angle_A, angle_B = law_of_cosines_for_angle(side_B, side_C, side_A), law_of_cosines_for_angle(side_A, side_C, side_B)
            solved = {"angle_A": angle_A, "angle_B": angle_B, "angle_C": 180 - (angle_A + angle_B)}
        case "SSA":
            side_A, side_B, angle_A = knowns["side_A"], knowns["side_B"], knowns["angle_A"]
            angle_B = law_of_sines_for_angle(side_A, angle_A, side_B)
            solved = {"angle_B": angle_B, "angle_C": 180 - (angle_A + angle_B), "side_C": law_of_sines_for_side(side_A, angle_A, 180 - (angle_A + angle_B))}
        case "SAS":
            side_A, side_B, angle_C = knowns["side_A"], knowns["side_B"], knowns["angle_C"]
            side_C = law_of_cosines_for_side(side_A, side_B, angle_C)
            solved = {"side_C": side_C, "angle_A": law_of_cosines_for_angle(side_B, side_C, side_A), "angle_B": 180 - (law_of_cosines_for_angle(side_B, side_C, side_A) + angle_C)}
        case "ASA":
            angle_A, angle_B, side_C = knowns["angle_A"], knowns["angle_B"], knowns["side_C"]
            angle_C = 180 - (angle_A + angle_B)
            solved = {"angle_C": angle_C, "side_A": law_of_sines_for_side(side_C, angle_C, angle_A), "side_B": law_of_sines_for_side(side_C, angle_C, angle_B)}
        case "AAS":
            angle_A, angle_B, side_A = knowns["angle_A"], knowns["angle_B"], knowns["side_A"]
            angle_C = 180 - (angle_A + angle_B)
            solved = {"angle_C": angle_C, "side_B": law_of_sines_for_side(side_A, angle_A, angle_B), "side_C": law_of_sines_for_side(side_A, angle_A, angle_C)}
        case "AAA":
            solved = {"Note": "AAA cannot determine side lengths."}
    
    triangle_data["solved"] = solved
    return triangle_data


if __name__ == "__main__":
    for _ in range(6):
        triangle = generate_triangle()
        solved_triangle = solve_triangle(triangle)
        print(json.dumps(solved_triangle, indent=4))
