class RubiksCube:
    def __init__(self, N):
        self.N = N  # Size of the cube (N x N)
        # Initialize the cube faces with their respective colors
        self.faces = self.initialize_faces()

    def initialize_faces(self):
        faces = ["U", "D", "F", "B", "L", "R"]
        return {
            face: [
                [self.initial_color(face) for _ in range(self.N)] for _ in range(self.N)
            ]
            for face in faces
        }

    def initial_color(self, face):
        # Define the initial color for each face
        colors = {
            "U": "W",  # White
            "D": "Y",  # Yellow
            "F": "G",  # Green
            "B": "B",  # Blue
            "L": "O",  # Orange
            "R": "R",  # Red
        }
        return colors[face]

    def rotate_face(self, face, direction="clockwise"):
        # Rotate a face 90 degrees in the specified direction
        self.faces[face] = rotate_matrix(self.faces[face], direction == "clockwise")

    def rotate_layer(self, axis, layer_index, direction="clockwise"):
        # Rotate a layer along the specified axis
        if axis not in ["x", "y", "z"]:
            raise ValueError("Invalid axis. Axis must be 'x', 'y', or 'z'.")
        if layer_index < 0 or layer_index >= self.N:
            raise ValueError(
                f"Invalid layer_index {layer_index} for axis '{axis}'. Must be between 0 and {self.N - 1}."
            )

        self.rotate_generic(axis, layer_index, direction)

    def rotate_generic(self, axis, k, direction):
        N = self.N
        clockwise = direction == "clockwise"

        axis_face_map = {
            "x": ["U", "F", "D", "B"],
            "y": ["F", "R", "B", "L"],
            "z": ["U", "R", "D", "L"],
        }
        faces = axis_face_map[axis]

        if axis == "x":
            if k == 0:
                self.rotate_face("L", "clockwise" if clockwise else "counterclockwise")
            elif k == N - 1:
                self.rotate_face("R", "counterclockwise" if clockwise else "clockwise")
        elif axis == "y":
            if k == 0:
                self.rotate_face("U", "clockwise" if clockwise else "counterclockwise")
            elif k == N - 1:
                self.rotate_face("D", "counterclockwise" if clockwise else "clockwise")
        elif axis == "z":
            if k == 0:
                self.rotate_face("F", "clockwise" if clockwise else "counterclockwise")
            elif k == N - 1:
                self.rotate_face("B", "counterclockwise" if clockwise else "clockwise")

        self.rotate_faces(faces, k, clockwise)

    def rotate_faces(self, faces, k, clockwise):
        N = self.N
        temp = [self.faces[faces[0]][i][k] for i in range(N)]
        if clockwise:
            for i in range(N):
                (
                    self.faces[faces[0]][i][k],
                    self.faces[faces[1]][i][k],
                    self.faces[faces[2]][i][k],
                    self.faces[faces[3]][N - 1 - i][N - 1 - k],
                ) = (
                    self.faces[faces[3]][N - 1 - i][N - 1 - k],
                    self.faces[faces[0]][i][k],
                    self.faces[faces[1]][i][k],
                    self.faces[faces[2]][i][k],
                )
        else:
            for i in range(N):
                (
                    self.faces[faces[0]][i][k],
                    self.faces[faces[3]][N - 1 - i][N - 1 - k],
                    self.faces[faces[2]][i][k],
                    self.faces[faces[1]][i][k],
                ) = (
                    self.faces[faces[1]][i][k],
                    self.faces[faces[0]][i][k],
                    self.faces[faces[3]][N - 1 - i][N - 1 - k],
                    self.faces[faces[2]][i][k],
                )

    # Optional method to print the cube's state
    def print_cube(self):
        for face in ["U", "D", "F", "B", "L", "R"]:
            print(f"Face {face}:")
            for row in self.faces[face]:
                print(" ".join(row))
            print()


# Helper function to rotate a matrix
def rotate_matrix(matrix, clockwise=True):
    if clockwise:
        return [list(row) for row in zip(*matrix[::-1])]
    else:
        return [list(row) for row in zip(*matrix)][::-1]


# Create a 3x3 Rubik's Cube
cube = RubiksCube(3)

# Print the initial state
print("Initial Cube State:")
cube.print_cube()

# Rotate the front face clockwise
cube.rotate_layer("z", 0, "clockwise")

# Rotate the middle layer along the y-axis counterclockwise
cube.rotate_layer("y", 1, "counterclockwise")

# Print the updated state
print("Updated Cube State:")
cube.print_cube()
