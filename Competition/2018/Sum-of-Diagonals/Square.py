class Square:

    def __init__(self, size, values):

        self.size = size
        self.values = values
    
    def __str__(self):
        
        desc = ""

        i = 1

        for row in self.rows:
            desc += f"Row {i}: {row}\n"
            i += 1
        
        return desc
    
    def __repr__(self):
        desc = ""
        i = 1
        for row in self.rows:
            desc += f"Row: {i}{row}\n"
            i += 1
        
        return desc
    
    @property
    def rows(self):

        grid = []
        row = []

        iter = 1
        for value in self.values:

            row.append(value)

            if iter % self.size == 0:
                grid.append(row)
                row = []
        
            iter += 1
        
        return grid
    
    @property
    def diagonals(self):

        diag_lb = []
        diag_rb = []

        # iterator to get diagonals from right to bottom
        rb_iter = self.size - 1

        # Diagonal left to bottom, diagonal values are equal to i and j iterators
        for i in range(len(self.rows)):

            for j in range(len(self.rows[i])):

                # Diagonals from left to bottom
                if i == j:
                    diag_lb.append(self.rows[i][j])
                
                # Diagonals from right to bottom
                if j == rb_iter:
                    diag_rb.append(self.rows[i][j])

            # Decrease the iterator per row    
            rb_iter -= 1

        
        return diag_lb, diag_rb
