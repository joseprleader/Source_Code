from Point import Point
from Line import Line

class Rectangle:

    def __init__(self, pbr, ptl):
        # Get bottom right point and top left point
        self.pbr = pbr
        self.ptl = ptl

        # Get bottom left point from information from pbr and ptl
        self.pbl = Point(self.ptl.x, self.pbr.y)

        # Get top right point from information from pbr and ptl
        self.ptr = Point(self.pbr.x, self.ptl.y)

        # Set up lines that form this rectangle
        # Place vertical and horizontal lines in different lists

        self.hor_lines = [Line(self.pbl, self.pbr, "h"), Line(self.ptl, self.ptr, "h")]
        self.ver_lines = [Line(self.pbr, self.ptr, "v"), Line(self.pbl, self.ptl, "v")]
    
    def __str__(self):
        desc = "\nRectangle Object\n"
        desc += f"Width:  {self.width}\n"
        desc += f"Height: {self.height}\n"
        desc += f"Area:   {self.area}\n"
        desc += f"Points: [{self.pbr, self.ptr, self.ptl, self.pbl}]\n"
        return desc
    
    def __repr__(self):
        desc = "\nRectangle Object\n"
        desc += f"Width:  {self.width}\n"
        desc += f"Height: {self.height}\n"
        desc += f"Area:   {self.area}\n"
        desc += f"Points: [{self.pbr, self.ptr, self.ptl, self.pbl}]\n"
        return desc
    
    @property
    def width(self):
        # Get distance from pbr point to pbl point
        return self.pbr.get_distance_from(self.pbl)
    
    @property
    def height(self):
        # Get distance from pbl point to ptl point
        return self.pbl.get_distance_from(self.ptl)
    
    @property
    def area(self):
        return self.width * self.height
    
    def find_overlapping_rect(self, other_rect):

        # Find overlapping points by doing a nested loop between the horizontal lines of this rectangle
        # and the vertical lines of the other

        inter_points = []

        for hor_line in self.hor_lines:

            for ver_line in other_rect.ver_lines:

                inter_points.append(hor_line.intersection_point(ver_line))
        
        # Do the same with vertical lines of this rectangle and horizontal lines of the other rectangle
        for ver_line in self.ver_lines:

            for hor_line in other_rect.hor_lines:

                inter_points.append(ver_line.intersection_point(hor_line))
        
        # Make sure to only return points and not strings
        inter_points = [point for point in inter_points if isinstance(point, Point)]

        lowest_x = min(inter_points[0].x, inter_points[1].x)
        lowerst_y = min(inter_points[0].y, inter_points[1].y)

        highest_x = max(inter_points[0].x, inter_points[1].x)
        highest_y = max(inter_points[0].y, inter_points[1].y)

        # Build overlapping rectangle and return it
        return Rectangle(Point(lowest_x, lowerst_y), Point(highest_x, highest_y))