

// 순열
public class Program {

    public static void MySolution(int[] question) {

        var output = new List<int[]>();
        var prevElements = new List<int>();

        void Dfs(List<int> elements) {

            if(elements.Count == 0) {
                output.Add(prevElements.ToArray());
                return;
            }

            foreach(var element in elements) {
                var nextElements = elements.Where(e => e != element).ToArray();

                prevElements.Add(element);
                Dfs([.. nextElements]);
                prevElements.RemoveAt(prevElements.Count - 1);
            }
        }

        Dfs(question.ToList());

        foreach(var element in output) {
            Console.WriteLine($"[{string.Join(", ", element)}]");
        }
    }

    public static void MySolutionReview(int[] question) {

        var output = new List<int[]>();

        void Dfs(int[] elements, int[] permutation) {

            if( elements.Length == 0 ) {
                output.Add(permutation);
                return;
            }

            foreach(var element in elements) {
                var nextElements = elements.Where(e => e != element).ToArray();

                Dfs(nextElements, [.. permutation, element]);
            }
        }

        Dfs(question, []);

        foreach(var element in output) {
            Console.WriteLine($"[{string.Join(", ", element)}]");
        }
    }

    public static void Main(string[] args) {
        var questions = new int[][] {
            [1, 2, 3]
        };

        foreach(var question in questions) {
            Console.WriteLine($"question : [{string.Join(", ", question)}]");
            //MySolution(question);
            MySolutionReview(question);
        }
    }
}