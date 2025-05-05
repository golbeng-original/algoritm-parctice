
// 부분 집합
public class Program {

    public static void MySolution(int[] question) {

        var output = new List<int[]>();

        void Dfs(int[] elements, int[] values) {

            output.Add(values);

            for(var idx = 0 ; idx < elements.Length ; idx++) {
                Dfs(elements[(idx+1)..], [..values, elements[idx]]);
            }
        }

        Dfs(question, []);

        foreach(var element in output) {
            Console.WriteLine($"[{string.Join(",",element)}]");
        }
    }

    public static void Main(string[] args) {
        var questions = new int[][] {
            [1, 2, 3]
        };

        foreach(var question in questions) {
            Console.WriteLine($"qustion: [{string.Join(",", question)}]");
            MySolution(question);
        }
    }
}