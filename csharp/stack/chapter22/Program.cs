

// 일일 온도
public partial class Program {

    public static int[] StackSolution(int[] question) {

        var answer = new int[question.Length];
        var stack = new Stack<int>();

        foreach(var idx in Enumerable.Range(0, question.Length)) {
            var current = question[idx];

            while(stack.Count > 0 && current > question[stack.Peek()]) {
                var last = stack.Pop();
                answer[last] = idx - last;
            }

            stack.Push(idx);
        }

        return answer;
    }

    public static void Main(string[] args) {
        var questions = new int[][] {
            [73, 74, 75, 71, 69, 72, 76, 73], // [1, 1, 4, 2, 1, 1, 0, 0]
            [30, 40, 50, 60], // [1, 1, 1, 0]
            [30, 60, 90], // [1, 1, 0]
            [30], // [0]
            [30, 20], // [0, 0]
        };

        foreach(var question in questions) {
            var result = StackSolution(question);
            Console.WriteLine($"[{string.Join(",", question)}] = [{string.Join(",", result)}]");
        }
    }
}