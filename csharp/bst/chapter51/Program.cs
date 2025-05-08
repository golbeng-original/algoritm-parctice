

using utils;

public class Program {

    public static void MySolution(int?[] serializedTree) {
        var root = TreeNode.createFromRaw(serializedTree);

        var acc = 0;
        void Dfs(TreeNode? node) {
            if( node == null ) {
                return;
            }

            Dfs(node.Right);
            acc += node.Value;
            node.Value = acc;
            Dfs(node.Left);

        }

        Dfs(root);
        var serialized = root.Serialize();
        Console.WriteLine($"[{string.Join(", ", serialized)}]");
    }

    public static void Main(string[] args) {
        var questions = new int?[][] {
            [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
        };

        foreach(var question in questions) {
            MySolution(question);
        }
    }
}