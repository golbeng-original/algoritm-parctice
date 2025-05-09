

public class ListNode<T> where T : struct {
    public T Value { get; private set; }

    public ListNode<T>? Next { get; set; } = null;

    public ListNode(T value) {
        this.Value = value;
    }

    public T[] Serialize() {

        var raw = new List<T>();
        var currNode = this;

        while( currNode != null ) {
            raw.Add(currNode.Value);
            currNode = currNode.Next;
        }

        return [..raw];
    }

    public static ListNode<T> CreateFromRaw(T[] values) {
        var root = new ListNode<T>(default);

        var currNode = root;
        foreach(var value in values) {
            currNode.Next = new ListNode<T>(value);
            currNode = currNode.Next;
        }

        return root.Next!;
    }
}