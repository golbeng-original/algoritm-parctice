

public class Program {

    public static void MySolution(int n) {

        var memozation = new Dictionary<int, long>();

        long Fib(int n) {
            if( n < 2 ) {
                return 1;
            }

            if( memozation.ContainsKey(n) ) {
                return memozation[n];
            }

            var result = Fib(n - 1) + Fib(n - 2);
            
            memozation[n] = result;

            return result;
        }

        var result = Fib(n);

        Console.WriteLine(result);

    }

    public static void Main(string[] args) {
        MySolution(5);
    }
}