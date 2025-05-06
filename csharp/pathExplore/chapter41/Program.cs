
// K 경유지 내 가장 저렴한 항공권
public class Program {

    public struct Question(int n, List<int[]> edges, int src, int dest, int k)
    {
        public int n = n;
        public List<int[]> edges = edges;
        public int src = src;
        public int dest = dest;
        public int k = k;
    }

    public record VertexInfo(int vertex, int price);

    public static int BookSolution(Question question) {
        var graph = new Dictionary<int, List<VertexInfo>>();
        foreach(var edge in question.edges) {
            if( graph.ContainsKey(edge[0]) == false ) {
                graph[edge[0]] = [];
            }

            graph[edge[0]].Add(new VertexInfo(edge[1], edge[2]));
        }

        var queue = new PriorityQueue<int, (int restTimes, int price)>();
        queue.Enqueue(question.src, (restTimes: question.k, price: 0));

        while( queue.Count > 0 ) {

            queue.TryDequeue(out var vertex, out var accValue);

            if( graph.ContainsKey(vertex) == false) {
                continue;
            }

            foreach(var nextVertex in graph[vertex]) {
                
                var restTimes = accValue.restTimes;
                var price = accValue.price + nextVertex.price;

                if( restTimes == 0 && nextVertex.vertex == question.dest) {
                    return price;
                }

                queue.Enqueue(nextVertex.vertex, (restTimes - 1, price));
            }
            
        }

        return -1;
    }

    public static int MySolution(Question question) {

        var graph = new Dictionary<int, List<VertexInfo>>();
        foreach(var edge in question.edges) {
            if( graph.ContainsKey(edge[0]) == false ) {
                graph[edge[0]] = [];
            }

            graph[edge[0]].Add(new VertexInfo(edge[1], edge[2]));
        }
        
        var queue = new PriorityQueue<int, int>();
        queue.Enqueue(question.src, -1);

        var cost = new Dictionary<(int vertex, int times), int>();
        
        while(queue.Count > 0) {
            
            queue.TryDequeue(out var vertex, out var times);

            if( graph.ContainsKey(vertex) == false ) {
                continue;
            }

            var prevKey = (vertex: vertex, times: times);
            if( cost.TryGetValue(prevKey, out var prevPrice) == false) {
                prevPrice = 0;
            }

            foreach(var nextVertex in graph[vertex]) {

                var key = (vertex: nextVertex.vertex, times: prevKey.times + 1);

                cost[key] = prevPrice + nextVertex.price;

                if( key.vertex == question.dest && key.times == question.k) {
                    return cost[key];
                }

                queue.Enqueue(nextVertex.vertex, key.times);
            }
        }

        return -1;
    }

    public static void Main(string[] args) {
        var questions = new List<Question>() {
            new Question(
                n: 3,
                edges: new List<int[]> {
                    new int[]{0, 1, 100},
                    new int[]{1, 2, 100},
                    new int[]{0, 2, 500},
                },
                src: 0,
                dest: 2,
                k: 0
            ), // 500
            new Question(
                n: 3,
                edges: new List<int[]> {
                    new int[]{0, 1, 100},
                    new int[]{1, 2, 100},
                    new int[]{0, 2, 500},
                },
                src: 0,
                dest: 2,
                k: 1
            ), // 200
            new Question(
                n: 3,
                edges: new List<int[]> {
                    new int[]{0, 1, 100},
                    new int[]{1, 2, 100},
                    new int[]{0, 2, 500},
                },
                src: 0,
                dest: 2,
                k: 2
            ), // -1
            new Question(
                n: 4,
                edges: new List<int[]> {
                    new int[]{0, 1, 100},
                    new int[]{1, 2, 100},
                    new int[]{0, 2, 500},
                    new int[]{2, 3, 100},
                },
                src: 0,
                dest: 3,
                k: 2
            ), // 600, //300
        };

        foreach(var question in questions) {
            //var result = MySolution(question);
            var result = BookSolution(question);
            Console.WriteLine(result);
        }
    }
}