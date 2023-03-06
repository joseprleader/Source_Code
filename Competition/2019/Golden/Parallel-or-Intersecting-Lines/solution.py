from GraphLine import GraphLine

def main():
    
    line1, line2 = get_n_process_STDIN_data()
    
    oneVertical = line1.get_line_type() == "Vertical" or line2.get_line_type() == "Vertical"
    bothVertical = line1.get_line_type() == "Vertical" and line2.get_line_type() == "Vertical"

    if oneVertical and not bothVertical:
        print("intersecting - one vertical")

    elif oneVertical and bothVertical:
        print("parallel - both vertical")

    else:

        if line1.get_slope() != line2.get_slope():
            print("intersecting")
        
        else:
            print("parallel")


def get_n_process_STDIN_data():
    """Get and process data from STDIN"""

    print("Enter coordinates for first line (x1 y1 x2 y2)")
    first_line_coors = input().split()
    first_line_coors = [int(coor) for coor in first_line_coors]

    print("Enter coordinates for second line (x1 y1 x2 y2)")
    second_line_coors = input().split()
    second_line_coors = [int(coor) for coor in second_line_coors]

    graphlines = (GraphLine(first_line_coors[0], first_line_coors[1], first_line_coors[2], first_line_coors[3]),
                  GraphLine(second_line_coors[0], second_line_coors[1], second_line_coors[2], second_line_coors[3]))
    
    return graphlines

main()