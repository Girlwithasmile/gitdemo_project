// Define a public class named Calculator
public class Calculator {

    // Method to add two numbers
    public static int add(int a, int b) {
        return a + b;
    }

    // Method to multiply two numbers
    public static int multiply(int a, int b) {
        return a * b;
    }

    // Main method to test the parameterized methods
    public static void main(String[] args) {
        // Define some numbers to operate on
        int num1 = 7;
        int num2 = 8;

        // Call the add method and print the result
        int sum = add(num1, num2);
        System.out.println("Sum: " + sum);

        // Call the multiply method and print the result
        int product = multiply(num1, num2);
        System.out.println("Product: " + product);
    }
}
