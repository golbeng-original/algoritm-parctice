
// 이진 트리의 직경
using utils;

public class Program {

    public static void MySolution(int[] rawTree) {
        var tree = TreeNode.createFromRaw(rawTree);

        var longest = 0;

        int Dfs(TreeNode? node) {
            if( node == null ) {
                return -1;
            }

            var leftDepth = Dfs(node.Left);
            var rightDepth = Dfs(node.Right);

            var distance = leftDepth + rightDepth + 2; // 거리??
            longest = Math.Max(longest, distance);


            return Math.Max(leftDepth, rightDepth) + 1; 
        }

        var depth = Dfs(tree);
        Console.WriteLine(longest);
    }

    public static void Main(string[] args) {
        var questions = new int[][] {
            [0, 1, 2, 3, 4, 5]
        };

        foreach(var question in questions) {
            MySolution(question);
        }
    }
}