
// 이진 탐색 트리 합의 범위
using utils;

public class Program {

    public record Question(int?[] serializedTree, int L, int R);

    public static void MySolution(Question question) {
        var root = TreeNode.createFromRaw(question.serializedTree);

        var total = 0;
        int Dfs(TreeNode? node) {
            if( node == null ) {
                return 0;
            }

            if( node.Value < question.L) {
                return Dfs(node.Right);
            }

            if( node.Value > question.R) {
                return Dfs(node.Left);
            }

            return node.Value + Dfs(node.Left) + Dfs(node.Right);
        }

        total = Dfs(root);
        Console.WriteLine(total);
    }

    public static void Main(string[] args) {

        var questions = new Question[] {
            new Question(
                serializedTree: [10, 5, 15, 3, 7, null, 18],
                L: 7,
                R: 15
            )
        };

        foreach(var question in questions) {
            MySolution(question);
        }
    }
}