package com.java;

public class FiguresArea {
    void calculateArea(float x)
    {
        System.out.println("Area of the square: "+x*x+" sq units");
    }
    void calculateArea(float x, float y)
    {
        System.out.println("Area of the rectangle: "+x*y+" sq units");
    }
    void calculateArea(double r)
    {
        double area = 3.14*r*r;
        System.out.println("Area of the circle: "+area+" sq units");
    }
    public static void main(String args[]){
        FiguresArea obj = new FiguresArea();

        /* This statement will call the first area() method
         * because we are passing only one argument with
         * the "f" suffix. f is used to denote the float numbers
         *
         */
        obj.calculateArea(6.1f);

        /* This will call the second method because we are passing
         * two arguments and only second method has two arguments
         */
        obj.calculateArea(10,22);

        /* This will call the second method because we have not suffixed
         * the value with "f" when we do not suffix a float value with f
         * then it is considered as type double.
         */
        obj.calculateArea(6.1);
    }
}
