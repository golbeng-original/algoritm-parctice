
public class Program {

    public static void MySolution(int[] arr) {
        var red = 0;
        var white = 0;
        var blue = arr.Length;

        while(white < blue) {
            if( arr[white] < 1 ) {
                (arr[white], arr[red]) = (arr[red], arr[white]);
                white += 1;
                red += 1;
            }
            else if(arr[white] > 1 ) {
                blue -= 1;
                (arr[white], arr[blue]) = (arr[blue], arr[white]);
            }
            else {
                white += 1;
            }
        }

        Console.WriteLine($"[{string.Join(", ", arr)}]");
    }

    public static void Main(string[] args) {
        var question = new int[] {
            2,0,2,1,1,0
        };

        MySolution(question);
    }
}