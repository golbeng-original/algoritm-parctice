
public class Program {
    
    public class Trie {
        
        public class TrieNode {
            public int WordIndex { get; set; } = -1;
            public Dictionary<char, TrieNode> Children { get; private set; } = [];

            public HashSet<int> PalindromeWordIds { get; private set; } = [];
        }

        public TrieNode Root { get; private set; } = new TrieNode();

        public bool IsPalindrome(string word) {
            var reverseWord = new string([..word.Reverse()]);
            return word == reverseWord;
        }

        public void Add(string word, int wordIndex) {
            
            var node = Root;

            var reverseWord = new string([.. word.Reverse()]);
            for(var idx = 0 ; idx < reverseWord.Length ; idx++) {
                var ch = reverseWord[idx];

                if( IsPalindrome(word[..(word.Length - idx)]) == true) {
                    node.PalindromeWordIds.Add(wordIndex);
                }

                if( node.Children.TryGetValue(ch, out var childNode) == false ) {
                    childNode = new TrieNode();
                    node.Children[ch] = childNode;
                }

                node = childNode;
            }

            node.WordIndex = wordIndex;
        }

        public List<int[]> Search(string word, int wordIndex) {
            var result = new List<int[]>();
            var node = Root;

            while( word.Length > 0 ) {
                if( node.WordIndex >= 0 ) {
                    if( IsPalindrome(word ) == true) {
                        result.Add([wordIndex, node.WordIndex]);
                    }
                }

                if( node.Children.TryGetValue(word[0], out var childNode) == false ) {
                    return result;
                }

                node = childNode;
                word = word[1..];
            }

            if( node.WordIndex >= 0 && node.WordIndex != wordIndex) {
                result.Add([wordIndex, node.WordIndex]);
            }

            foreach(var element in node.PalindromeWordIds) {
                result.Add([wordIndex, element]);
            }

            return result;
        }

    }

    public static void MySolution(string[] words) {

        var trie = new Trie();
        for(var idx = 0 ; idx < words.Length ; idx++) {
            trie.Add(words[idx], idx);
        }


        for(var idx = 0 ; idx < words.Length ; idx++) {
            var result = trie.Search(words[idx], idx);

            foreach(var findPair in result) {
                Console.WriteLine($"[{findPair[0]}, {findPair[1]}]");
            }
        }
    }

    public static void Main(string[] args) {
        
        var questions = new string[][] {
            [
                //"abcd",
                //"dcba",
                "lls",
                "s",
                "sssll"
            ],
            [
                "bat",
                "tab",
                "cat"
            ]
        };

        foreach(var question in questions) {
            MySolution(question);
            break;
        }
    }
}