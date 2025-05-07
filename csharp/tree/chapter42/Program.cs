

// 이진 트리의 최대 깊이
using utils;

public class Program {

    // BFS 로 문제 풀이
    public static int MySolution(int?[] tree) {
        var treeNode = TreeNode.createFromRaw(tree);

        var queue = new Queue<TreeNode>();
        queue.Enqueue(treeNode);

        var depth = 0;
        while( queue.Count > 0 ) {
            depth += 1;

            foreach(var _ in Enumerable.Range(0, queue.Count)) {
                var currNode = queue.Dequeue();

                if( currNode.Left != null ) {
                    queue.Enqueue(currNode.Left);
                }

                if( currNode.Right != null ) {
                    queue.Enqueue(currNode.Right);
                }
            }
        }

        return depth;
    }

    public static void Main(string[] args) {

        var questions = new int?[][] {
            [3,9,20, null, null, 15, 7]
        };

        foreach(var question in questions) {
            var result = MySolution(question);
            Console.WriteLine(result);
        }
    }
}