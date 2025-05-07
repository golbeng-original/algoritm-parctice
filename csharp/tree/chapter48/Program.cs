
// 최소 높이 트리
public class Program {

    public record Question(int n, int[][] edges);

    public static void BookSolution(Question question) {

        var graph = new Dictionary<int, List<int>>();
        foreach(var edge in question.edges) {
            
            if(graph.TryGetValue(edge[0], out var list1) == false ) {
                list1 = [];
                graph[edge[0]] = list1;
            }
            list1.Add(edge[1]);

            if(graph.TryGetValue(edge[1], out var list2) == false ) {
                list2 = [];
                graph[edge[1]] = list2;
            }
            list2.Add(edge[0]);
        }

        var leaves = new List<int>();
        foreach(var i in Enumerable.Range(0, question.n)) {
            if( graph[i].Count == 1) {
                leaves.Add(i);
            }
        }

        var n = question.n;
        while(n > 2) {
            n -= leaves.Count;

            var newLeavse = new List<int>();

            foreach(var leaf in leaves) {
                var neighbor = graph[leaf].Last();
                graph[leaf] = graph[leaf][..^1];
                if( graph[leaf].Count == 0) {
                    graph.Remove(leaf);
                }

                graph[neighbor].Remove(leaf);

                if( graph[neighbor].Count == 1) {
                    newLeavse.Add(neighbor);
                }
            }

            leaves = newLeavse;
        }

        Console.WriteLine($"[{string.Join(", ", leaves)}]");
    }

    public static void MySolution(Question question) {

        int Dfs(int startVertex, int[][] edges) {
            var visited = new HashSet<int>();

            var stack = new Stack<int>();
            stack.Push(startVertex);

            var depth = 0;
            while( stack.Count > 0 ) {

                var vertex = stack.Pop();
                visited.Add(vertex);

                var nextVertices1 = edges
                    .Where(e => e[0] == vertex)
                    .Select(e => e[1])
                    .Where(e => visited.Contains(e) == false );
                
                var nextVertices2 = edges
                    .Where(e => e[1] == vertex)
                    .Select(e => e[0])
                    .Where(e => visited.Contains(e) == false );

                var nextVertices = nextVertices1.Concat(nextVertices2);

                if( nextVertices.Any() == false ) {
                    continue;
                }

                foreach(var nextVertex in nextVertices) {
                    stack.Push(nextVertex);
                }

                depth++;
            }

            return depth;
        }

        var depths = new SortedDictionary<int, List<int>>();
        foreach(var n in Enumerable.Range(0, question.n)) {
            
            var depth = Dfs(n, question.edges);

            if( depths.TryGetValue(depth, out var list) == false) {
                list = [];
                depths[depth] = list;
            }

            list.Add(n);
        }

        var minVertices = depths.First().Value;
        Console.WriteLine($"[{string.Join(", ", minVertices)}]");
    }

    public static void Main(string[] args) {
        var questions = new List<Question>() {
            new Question(
                n: 4,
                edges: new int[][] {
                    [1, 0],
                    [1, 2],
                    [1, 3],
                }
            ),
            new Question(
                n: 6,
                edges: new int[][] {
                    [0, 3],
                    [1, 3],
                    [2, 3],
                    [4, 3],
                    [5, 4],
                }
            ),
            new Question(
                n: 10,
                edges: new int[][] {
                    [0, 2],
                    [1, 2],
                    [2, 3],
                    [2, 4],
                    [3, 5],
                    [5, 9],
                    [4, 6],
                    [4, 7],
                    [7, 8],
                }
            ),
        };

        foreach(var question in questions) {
            //MySolution(question);
            BookSolution(question);
        }
    }
}