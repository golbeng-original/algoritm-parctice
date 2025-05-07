
// 균형 이진 트리
using utils;

public class Program {

    public static void MySolution(int?[] serializedTree) {
        var root = TreeNode.createFromRaw(serializedTree);

        int Dfs(TreeNode? node) {
            if( node == null ) {
                return 0;
            }

            var leftDepth = Dfs(node.Left);
            var rightDepth = Dfs(node.Right);

            if( leftDepth == -1 || rightDepth == -1 ) {
                return -1;
            }

            if( Math.Abs(rightDepth - leftDepth) > 1 ) {
                return -1;
            }

            return Math.Max(leftDepth, rightDepth) + 1;
        }

        var value = Dfs(root);
        Console.WriteLine(value);
    }

    public static void Main(string[] args) {
        var questions = new int?[][] {
            [3, 9, 20, null, null, 15, 7],
            [1, 2, 2, 3, 3, null, null, 4, 4]
        };
        
        foreach(var question in questions) {
            MySolution(question);
        }
    }
}