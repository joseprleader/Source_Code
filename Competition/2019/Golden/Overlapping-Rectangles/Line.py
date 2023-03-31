from Point import Point

class Line:

    def __init__(self, p1, p2, line_type):
        self.p1 = p1
        self.p2 = p2
        self.line_type = line_type
    
    def __str__(self):
        return f"Line: {self.line_type} [{self.p1}, {self.p2}]"
    
    def __repr__(self) -> str:
        return f"Line: {self.line_type} [{self.p1}, {self.p2}]"
    
    def intersection_point(self, other_line):

        # Make lists for horizontal points and vertical points
        hor_points = []
        ver_points = []

        inter_point = None
        point_found = False

        if self.line_type == "h" and other_line.line_type == "v":

            # Find minimum and maximum coordinates for this lines x coors
            min_self_x = min(self.p1.x, self.p2.x + 1)
            max_self_x = max(self.p1.x, self.p2.x + 1)

            # Find minimum and maximum coordinates for other line y coors
            min_other_y = min(other_line.p1.y, other_line.p2.y + 1)
            max_other_y = max(other_line.p1.y, other_line.p2.y + 1)

            for xcoor in range(min_self_x, max_self_x):
                hor_points.append(Point(xcoor, self.p2.y))
            
            for ycoor in range(min_other_y, max_other_y):
                ver_points.append(Point(other_line.p2.x, ycoor))
        
        elif self.line_type == "v" and other_line.line_type == "h":
             
             # Find minimum and maximum coordinates for this lines y coors
            min_self_y = min(self.p1.y, self.p2.y + 1)
            max_self_y = max(self.p1.x, self.p2.x + 1)

            # Find minimum and maximum coordinates for other line x coors
            min_other_x = min(other_line.p1.x, other_line.p2.x + 1)
            max_other_x = max(other_line.p1.x, other_line.p2.x + 1)

            for ycoor in range(min_self_y, max_self_y):
                ver_points.append(Point(self.p2.x, ycoor))
            
            for xcoor in range(min_other_x, max_other_x):
                hor_points.append(Point(xcoor, other_line.p2.y))
        
        else:
            inter_point = "Only vertical and horizontal lines allowed"

        # Loop through one of the lists and if one point is in the other list, then return that point
        for p in hor_points:

            if p in ver_points:
                inter_point = p
                point_found = True
                break
        
        if not point_found:  
            # If no equal point is found return no point found
            inter_point = "No point found"
        
        return inter_point

