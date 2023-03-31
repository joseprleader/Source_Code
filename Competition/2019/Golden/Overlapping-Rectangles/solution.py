from Point import Point
from Rectangle import Rectangle

# Get total area of two rectangles and the shared area between them
def main():

    # Get data from STDIN
    print("Enter corners of rectangle 1:")
    r1coors = input().strip().split() 
    
    print("Enter corners of rectangle 2:")
    r2coors = input().strip().split()
    
    # Create both rectangles
    r1 = Rectangle(Point(r1coors[0],r1coors[1]), Point(r1coors[2],r1coors[3]))
    r2 = Rectangle(Point(r2coors[0], r2coors[1]), Point(r2coors[2],r2coors[3]))

    # Get overlapping rectangle
    roverlap = r1.find_overlapping_rect(r2)

    # Get overlapping area
    area_overlap = roverlap.area

    # Get total area
    total_area = r1.area + r2.area - area_overlap

    # Show it to the console
    print(f"overlap area {area_overlap}")
    print(f"total area {total_area}")

main()