Triangle Solver

Goal

The goal of this program is to generate and solve different types of triangles using trigonometric laws. The program randomly generates triangles of various types, computes missing values, and outputs the solved triangle.

Steps

Generate a Triangle

Randomly select a triangle type: SSS, SSA, SAS, ASA, AAS, or AAA.

Generate known values based on the triangle type (sides, angles).

Solve the Triangle

Apply the Law of Sines or Law of Cosines depending on the given information.

Compute missing sides and angles.

Ensure angle sum validation (sum of angles in a triangle is always 180°).

Handle special cases like AAA, where side lengths cannot be determined.

Run in a Loop

Execute the triangle generation and solving process six times.

Print the solved triangle in JSON format for readability.

Execution

The script follows the standard Python __main__ idiom, ensuring it only runs when executed directly from the command line:

if __name__ == "__main__":
    for _ in range(6):
        triangle = generate_triangle()
        solved_triangle = solve_triangle(triangle)
        print(json.dumps(solved_triangle, indent=4))

Output

Each iteration prints a solved triangle, displaying the known values and the computed missing values in JSON format.

This program provides a foundation for trigonometry practice by generating a variety of solvable triangle problems dynamically.

