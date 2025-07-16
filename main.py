def generate_multi_diameter_cix(
    config: dict,
    start_x: float = 0.0,
    start_y: float = 0.0,
    x_spacing: float = 32.0,
    y_spacing: float = 50.0,
    depth: float = 15.0,
    output_file: str = "multi_diameter_drill_test.cix"
):
    """
    Generates a .CIX drill test program for a Biesse Rover B.

    Args:
        config: A dict mapping diameters (float) to lists of spindle IDs (int).
                e.g. {5.0: [1,2,3], 8.0: [4,5,6]}
        start_x: X coordinate of the first hole of the first row.
        start_y: Y coordinate of the first row.
        x_spacing: Distance between holes along X.
        y_spacing: Distance between rows along Y.
        depth: Drill depth for all holes.
        output_file: Filename for the generated CIX.
    """
    with open(output_file, "w") as f:
        f.write("BEGIN PROGRAM\n")
        f.write("    NAME=DrillTest\n")
        f.write("    UNITS=MM\n\n")

        current_y = start_y
        for diameter, spindle_list in config.items():
            current_x = start_x
            for spindle_id in spindle_list:
                f.write("BEGIN MACRO\n")
                f.write("    NAME=DRILL\n")
                f.write(f"    PARAM,NAME=SPINDLEID,VALUE={spindle_id}\n")
                f.write(f"    PARAM,NAME=X,VALUE={current_x}\n")
                f.write(f"    PARAM,NAME=Y,VALUE={current_y}\n")
                f.write("    PARAM,NAME=Z,VALUE=0\n")
                f.write(f"    PARAM,NAME=DPTH,VALUE={depth}\n")
                f.write(f"    PARAM,NAME=DIAMETER,VALUE={diameter}\n")
                f.write("END MACRO\n\n")
                current_x += x_spacing
            current_y += y_spacing

        f.write("END PROGRAM\n")

    print(f"✅ CIX drill test generated: {output_file}")


if __name__ == "__main__":
    # Example configuration:
    # - 5.0 mm holes using spindles 1–5
    # - 8.0 mm holes using spindles 6–8
    config = {
        5.0: [1, 2, 3, 4, 5],
        8.0: [6, 7, 8]
    }
    # Customize start positions, spacings, depth, and filename here:
    generate_multi_diameter_cix(
        config=config,
        start_x=0.0,
        start_y=0.0,
        x_spacing=32.0,
        y_spacing=50.0,
        depth=15.0,
        output_file="multi_diameter_drill_test.cix"
    )
