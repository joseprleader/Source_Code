class GraphLine(object):
    """Software class to represent graphical lines."""

    def __init__(self, x1, y1, x2, y2):
        """Initialize this graph line."""

        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

        self.slope = self.get_slope()
        self.line_type = self.get_line_type()
    
    def get_slope(self):
        """Get the slope of the line"""

        try:
            self.slope = (self.y2 - self.y1) / (self.x2 - self.x1)
        
        except ZeroDivisionError:
            self.slope = None
        
        return self.slope
    
    def get_line_type(self):
        """Get the line type"""

        slope = self.get_slope()

        if slope == None:
            self.line_type = "Vertical"
        
        elif slope == 0:
            self.line_type = "Horizontal"
        
        else:
            self.line_type = "Inclined"
        
        return self.line_type

