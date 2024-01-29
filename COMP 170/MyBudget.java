import java.util.Scanner;

public class MyBudget {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        char choice = ' ';
        
        while (choice != 'c') {
            System.out.println("Welcome to MyBudget!");
            System.out.println("-------------------------------");
            System.out.println("Disclaimer: These are only suggested budgets and estimated values that should only give an idea of such values and budgets");
            System.out.println("-------------------------------");
            System.out.println("Here are some keybinds to navigate this program!");
            System.out.println("-------------------------------");
            System.out.println("Calculate Suggested Monthly Budget based on income (b)");
            System.out.println("-------------------------------");
            System.out.println("Estimate depreciation of your car (a)");
            System.out.println("-------------------------------");
            System.out.println("Estimate real estate value (r)");
            System.out.println("-------------------------------");
            System.out.println("Close Program (c)");
            System.out.println("-------------------------------");
            System.out.print("Enter your choice: ");

            choice = scanner.next().charAt(0);
            switch(choice) {
                case 'b':
                    calculateMonthlyBudget(scanner);
                    break;
                case 'a':
                    estimateCarDepreciation(scanner);
                    break;
                case 'r':
                    estimateRealEstateValue(scanner);
                    break;
                case 'c':
                    System.exit(0);
                default:
                    System.out.println("Invalid choice!");
                    break;
            }
        }
        
        scanner.close();
    }
    
    public static void calculateMonthlyBudget(Scanner scanner) {
        System.out.print("Enter your monthly income: ");
        double income = scanner.nextDouble();
        
        double rent = income * 0.2;
        double groceries = income * 0.1;
        double utilities = income * 0.1;
        double transportation = income * 0.1;
        double savings = income * 0.2;
        double otherExpenses = income * 0.3;
        
        System.out.println("Suggested Monthly Budget");
        System.out.println("-----------------------------");
        System.out.printf("Rent: $%.2f\n", rent);
        System.out.printf("Groceries: $%.2f\n", groceries);
        System.out.printf("Utilities: $%.2f\n", utilities);
        System.out.printf("Transportation: $%.2f\n", transportation);
        System.out.printf("Savings: $%.2f\n", savings);
        System.out.printf("Other Expenses: $%.2f\n", otherExpenses);
    }
    
    public static void estimateCarDepreciation(Scanner scanner) {
        System.out.print("Enter the initial value of your car: ");
        double initialValue = scanner.nextDouble();
        
        double depreciation = initialValue * 0.15;
        double currentValue = initialValue - depreciation;
        
        System.out.println("Car Depreciation Estimate");
        System.out.println("-----------------------------");
        System.out.printf("Depreciation: $%.2f\n", depreciation);
        System.out.printf("Current Value: $%.2f\n", currentValue);
    }
    
    public static void estimateRealEstateValue(Scanner scanner) {
        System.out.print("Enter the current value of your real estate property: ");
        double value = scanner.nextDouble();
        
        double appreciation = value * 0.03;
        double newValue = value + appreciation;
        
        System.out.println("Real Estate Value Estimate");
        System.out.println("-----------------------------");
        System.out.printf("Appreciation: $%.2f\n", appreciation);
        System.out.printf("New Value: $%.2f\n", newValue);
    }
}
