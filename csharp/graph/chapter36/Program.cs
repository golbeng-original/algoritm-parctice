
// 조합의 합
public class Program {

    public static void MySolution(int[] candidates, int target) {

        var output = new List<int[]>();

        void Dfs(int[] elements, int[] restCandidate, int acc) {
            
            if( acc > target ) {
                return;
            }

            if( acc == target ) {
                output.Add(elements);
                return;
            }

            var nextCandidate = restCandidate[..];
            foreach(var candidate in restCandidate) {
                Dfs([..elements, candidate], nextCandidate, acc + candidate);
                nextCandidate = nextCandidate[1..];
            }

        }

        Dfs([], candidates, 0);

        foreach(var element in output) {
            Console.WriteLine($"[{string.Join(", ", element)}]");
        }
    }

    public static void Main(string[] args) {
        var questions = new List<(int[] candidates, int target)>() {
            (candidates: [2,3,6,7], target: 7),
            (candidates: [2,3,5], target: 8)
        };

        foreach(var question in questions) {
            Console.WriteLine($"candicate: [{string.Join(",", question.candidates)}], target = {question.target}");
            MySolution(question.candidates, question.target);
        }
    }
}