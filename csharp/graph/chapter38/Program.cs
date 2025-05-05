
// 일정 재구성
using System.Text;

public class Program {


    public static void BookSolution((string from, string to)[] question) {

        var graph = new Dictionary<string, List<string>>();
        foreach(var element in question) {
            if( graph.ContainsKey(element.from) == false ) {
                graph.Add(element.from, new ());
            }

            graph[element.from].Add(element.to);
        }

        foreach( var entry in graph) {
            entry.Value.Sort();
        }

        var output = new List<string>();

        void Dfs(string depature) {
            output.Add(depature);

            if( graph.ContainsKey(depature) == false || graph[depature].Count == 0) {
                return;
            }

            var root = graph[depature];
            var to = root.First();
            graph[depature] = graph[depature][1..];
            Dfs(to);
        }

        Dfs("JFK");
        Console.WriteLine($"[{string.Join(",", output)}]");
    }

    public static void MySolution((string from, string to)[] question) {
        
        var output = new List<string>();

        void Dfs(string depature, (string from, string to)[] roots) {

            var root = roots
                .Where(e => e.from == depature )
                .OrderBy(e => e.to)
                .FirstOrDefault();
            
            if( root.from == null ) {
                output.Add(depature);
                return;
            }

            output.Add(root.from);
            Dfs(root.to, [.. roots.Where( e => e != root)]);
        }

        Dfs("JFK", question);

        Console.WriteLine($"[{string.Join(",", output)}]");
    }

    public static void Main(string[] args) {
        var questions = new List<(string from, string to)[]> {
            new (string from, string to)[]{
                (from: "MUC", to: "LHR"),
                (from: "JFK", to: "MUC"),
                (from: "SFO", to: "SJC"),
                (from: "LHR", to: "SFO")
            }, // ["JFK", "MUC", "LHR", "SFO", "SJC"]
            new (string from, string to)[]{
                (from: "JFK", to: "SFO"),
                (from: "JFK", to: "ATL"),
                (from: "SFO", to: "ATL"),
                (from: "ATL", to: "JFK"),
                (from: "ATL", to: "SFO")
            }, // ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
        };

        foreach(var question in questions) {
            var builder = new StringBuilder();
            builder.Append("[");
            builder.Append($"[{string.Join(",", question)}]");
            builder.Append("]");
            Console.WriteLine(builder.ToString());
            //MySolution(question);
            BookSolution(question);
        }

    }
}