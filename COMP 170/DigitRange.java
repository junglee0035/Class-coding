public class DigitRange {
    
    public static int digitRange(int number) {
        number = Math.abs(number);
        
        int maxValue = number % 10;
        int minValue = number % 10;
       
        number /= 10;
        
        while(number > 0) {
            int digit = number % 10;
            
            if(digit > maxValue) {
                maxValue = digit;
            } else if(digit < minValue) {
                minValue = digit;
            }
            
            number /= 10;
        }
        
        return maxValue - minValue + 1;
    }
    public static void main(String[] args) {
        int range = digitRange(6);
     System.out.println("the range of values of it's digits is: " +range);

    }

}

