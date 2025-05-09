
using System.Text;

public class Program {

    public static void MySolution(int[] question) {

        bool IsNeedSwap(int lhs, int rhs) {
            var lhsStr = lhs.ToString() + rhs.ToString();
            var rhsStr = rhs.ToString() + lhs.ToString();

            return int.Parse(lhsStr) > int.Parse(rhsStr);
        }

        for(var i = 1 ; i < question.Length ; i ++) {

            var j = i;
            while( j > 0 && IsNeedSwap(question[j - 1], question[j]) == true ) {
                (question[j - 1], question[j]) = (question[j], question[j-1]);
                j--;
            }
        }

        var result = question.Aggregate("", (e, acc) => acc + e.ToString());
        Console.WriteLine(result);
    }

    public static void Main(string[] args) {
        var questions = new int[][] {
            [10, 2],
            [3, 30, 34, 5 , 9]
        };


        foreach(var question in questions) {
            MySolution(question);
        }
    }
}