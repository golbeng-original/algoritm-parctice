namespace utils;

public class TreeNode {
    public int Value { get; set; }
    public TreeNode? Left { get; set; }
    public TreeNode? Right { get; set; }

    public TreeNode(int value) {
        this.Value = value;
    }

    public int?[] Serialize() {

        var serializeList = new List<int?>();

        var queue = new Queue<TreeNode?>();
        queue.Enqueue(this);

        while( queue.Count > 0 ) {

            if( queue.Any((e) => e != null) == false ) {
                break;
            }

            var node = queue.Dequeue();

            serializeList.Add(node?.Value);

            queue.Enqueue(node?.Left);
            queue.Enqueue(node?.Right);
        }

        return serializeList.ToArray();

    }

    public static TreeNode createFromRaw(int?[] tree) {
        
        var root = new TreeNode(tree[0]!.Value);

        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);

        var idx = 1;
        while(idx < tree.Length) {

            var current = queue.Dequeue();

            var value = tree[idx++];
            if( value != null ) {
                var leftNode = new TreeNode(value.Value);
                current.Left = leftNode;
                queue.Enqueue(leftNode);
            }

            value = tree[idx++];
            if( value != null ) {
                var rightNode = new TreeNode(value.Value);
                current.Right = rightNode;
                queue.Enqueue(rightNode);
            }
        }

        return root;
    }

    public static TreeNode createFromRaw(int[] tree) {
        
        var root = new TreeNode(tree[0]);

        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);

        var idx = 1;
        while(idx < tree.Length) {

            var current = queue.Dequeue();

            if( idx < tree.Length) {
                var value = tree[idx++];
                var leftNode = new TreeNode(value);
                current.Left = leftNode;
                queue.Enqueue(leftNode);
            }

            if( idx < tree.Length) {
                var value = tree[idx++];
                var rightNode = new TreeNode(value);
                current.Right = rightNode;
                queue.Enqueue(rightNode);
            }

        }

        return root;
    }
}

