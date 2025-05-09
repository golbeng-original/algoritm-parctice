
public class Program {

    public static void MySolution(List<int[]> question) {

        question.Sort((lhs, rhs) => lhs[0] < rhs[0] ? -1 : 1);

        var idx = 0;
        while( idx < question.Count - 1 ) {

            if( question[idx][0] < question[idx + 1][0] &&
                question[idx][1] > question[idx+ 1][0] ) {
                
                var left = question[idx];
                var right = question[idx + 1];

                question.RemoveAt(idx + 1);
                question[idx] = [ left[0], right[1] ];
            }
            else {
                idx++;
            }
        }
    }

    public static void Main(string[] args) {
        var question = new List<int[]> {
            new int[]{1, 3},
            new int[]{2, 6},
            new int[]{8, 10},
            new int[]{15, 18}
        };

        MySolution(question);
        var elemetStrings = question.Select(e => $"[{string.Join(", ", e)}]");
        Console.WriteLine($"[{string.Join(", ", elemetStrings)}]");

    }
}