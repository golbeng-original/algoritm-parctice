

using utils;

// 이진 트리 반전
public class Program {

    public static void BookSolution1(int[] rawTree) {

        var root = TreeNode.createFromRaw(rawTree);

        void Dfs(TreeNode node) {
            
            if( node.Left == null || node.Right == null ) {
                return;
            }

            Dfs(node.Left);
            Dfs(node.Right);

            (node.Left, node.Right ) = (node.Right, node.Left);
        }

        Dfs(root);
        Console.WriteLine(root);
    }

    public static void BookSolution2(int[] rawTree) {
        var root = TreeNode.createFromRaw(rawTree);

        void Bfs(TreeNode node) {
            
            var queue = new Queue<TreeNode>();
            queue.Enqueue(node);

            while(queue.Count > 0) {
                
                var invertNode = queue.Dequeue();

                if( invertNode.Left == null || invertNode.Right == null) {
                    continue;
                }

                (invertNode.Left, invertNode.Right) = (invertNode.Right, invertNode.Left);

                queue.Enqueue(invertNode.Left);
                queue.Enqueue(invertNode.Right);
            }
        }

        Bfs(root);
        Console.WriteLine(root);
    }

    public static void MySolution(int[] rawTree) {
        var treeNode = TreeNode.createFromRaw(rawTree);

        var listPerDpeth = new SortedDictionary<int, List<int>>();

        var queue = new Queue<TreeNode>();
        queue.Enqueue(treeNode);

        var depth = 0 ;
        while( queue.Count > 0 ) {
            
            foreach(var _ in Enumerable.Range(0, queue.Count)) {

                var node = queue.Dequeue();
                if( listPerDpeth.ContainsKey(depth) == false ) {
                    listPerDpeth.Add(depth, []);
                }

                listPerDpeth[depth].Add(node.Value);

                if( node.Left != null) {
                    queue.Enqueue(node.Left);
                }

                if( node.Right != null ) {
                    queue.Enqueue(node.Right);
                }
            }

            depth++;
        }

        foreach(var value in listPerDpeth.Values) {
            value.Sort((lhs, rhs) => lhs > rhs ? -1 : 1);
        }

        var reverseRawTree = listPerDpeth.Aggregate(new List<int>(), (seed, e) => { seed.AddRange(e.Value); return seed; });

        var reverseTreeNode = TreeNode.createFromRaw(reverseRawTree.ToArray());
        Console.WriteLine(reverseTreeNode);
    }

    public static void Main(string[] args) {

        var questions = new int[][] {
            [4,2,7,1,3,6,9],
        };

        foreach(var question in questions) {
            //BookSolution1(question);
            BookSolution2(question);
            //MySolution(question);
        }
    }
}