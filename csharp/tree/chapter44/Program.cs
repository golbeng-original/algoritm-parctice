using utils;

// 가장 긴 동일 값 경로
public class Program {

    public static void MySolution(int?[] rawTree) {
        var treeNode = TreeNode.createFromRaw(rawTree);

        var longest = 0;
        int Dfs(TreeNode? node) {
            if( node == null) {
                return -1;
            }

            var leftDepth = Dfs(node.Left);
            if( node.Value != node.Left?.Value) {
                leftDepth = -1;
            }

            var rightDepth = Dfs(node.Right);
            if( node.Value != node.Right?.Value) {
                rightDepth = -1;
            }

            var distance = leftDepth + rightDepth + 2;
            longest = Math.Max(longest, distance);

            return Math.Max(leftDepth, rightDepth) + 1;
        }

        Dfs(treeNode);
        Console.WriteLine(longest);
    }

    public static void Main(string[] args) {

        var questions = new int?[][] {
            [5,4,5,1,1,null,5, null, null, null, null, 5, null],
            [1,4,5,4,4,null,5]
        };

        foreach(var question in questions) {
            MySolution(question);
        }
    }
}