public class GraphLine {

    private double slope;
    private String lineType;
    private double x1;
    private double x2;
    private double y1;
    private double y2;
    
    public GraphLine(double x1, double y1, double x2, double y2)
    {
        this.x1 = x1;
        this.x2 = x2;
        this.y1 = y1;
        this.y2 = y2;
    }

    public double getSlope()
    {
        double slope;
        
        try
        {
            slope = (this.y2 - this.y1) / (this.x2 - this.x1);
        }

        catch (Exception e)
        {
            slope = Double.MAX_VALUE;
        }

        this.slope = slope;

        return this.slope;
    }

    public String getLineType()
    {
        switch (this.getSlope())
        {
            case Double.MAX_VALUE:
                this.lineType = "Vertical";
            
            case 0.0:
                this.lineType = "Horizontal";
            
            default:
                this.lineType = "Inclined";
        }

        return this.lineType;

    }
}
