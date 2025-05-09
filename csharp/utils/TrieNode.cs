
public class TrieNode {

    public bool IsWord { get; set; } = false;
    public Dictionary<char, TrieNode> Children { get; private set; }  = [];
}

public class Trie {

    public TrieNode Root { get; private set; } = new TrieNode();

    public void Add(string word) {
        var node = Root;

        foreach(var ch in word) {
            if( node.Children.TryGetValue(ch, out var childNode) == false) {
                childNode = new TrieNode();
                node.Children[ch] = childNode;
            }

            node = childNode;
        }

        node.IsWord = true;
    }

    public bool Search(string word) {
        var node = Root;

        foreach(var ch in word) {
            if( node.Children.TryGetValue(ch, out var childNode) == false ) {
                return false;
            }

            node = childNode;
        }

        return node.IsWord;
    }
}