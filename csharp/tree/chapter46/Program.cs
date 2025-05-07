
// 두 이진 트리 병합
using utils;

public class Program {

    public static void MySolution(int?[] rawTree1, int?[] rawTree2) {
        var leftNode = TreeNode.createFromRaw(rawTree1);
        var rightNode = TreeNode.createFromRaw(rawTree2);

        TreeNode? Dfs(TreeNode? lhsNode, TreeNode? rhsNode) {

            if( lhsNode == null && rhsNode == null ) {
                return null;
            }

            var sumLeftNode = Dfs(lhsNode?.Left, rhsNode?.Left);
            var sumRigtNode = Dfs(lhsNode?.Right, rhsNode?.Right);

            var leftValue = lhsNode?.Value ?? 0;
            var rightValue = rhsNode?.Value ?? 0;

            var sumNode = new TreeNode(leftValue + rightValue)
            {
                Left = sumLeftNode,
                Right = sumRigtNode
            };

            return sumNode;
        }

        var sumNode = Dfs(leftNode, rightNode);
        var serialize = sumNode.Serialize();
        Console.WriteLine(string.Join(", ", serialize));
    }

    public static void Main(string[] args) {

        var questions = new List<(int?[] tree1, int?[] tree2)>() {
            (
                tree1: [1, 3, 2, 5, null],
                tree2: [2, 1, 3, null, 4, null, 7]
            )
        };

        foreach(var question in questions) {
            MySolution(question.tree1, question.tree2);
        }
    }
}