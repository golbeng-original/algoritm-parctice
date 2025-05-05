
// 조합
public class Program {

    public static void MySolution(int n, int k) {
        var output = new List<int[]>();

        void Dfs(int[] elements, int start, int end, int k) {
            if( k == 0 ) {
                output.Add(elements);
                return;
            }

            for(var i = start ; i <= end ; i++) {
                
                elements = [.. elements, i];
                Dfs(elements, i + 1, end, k - 1);
                elements = elements[..^1];
            }
        }

        Dfs([], 1, n, k);

        foreach(var element in output) {
            Console.WriteLine($"[{string.Join(", ", element)}]");
        }
    }

    public static void Main(string[] args) {
        var questions = new List<(int n, int k)>() {
            (n: 4, k: 2)
        };

        foreach(var question in questions) {
            Console.WriteLine($"n : {question.n}, k : {question.k}");
            MySolution(question.n, question.k);
        }
    }
}
