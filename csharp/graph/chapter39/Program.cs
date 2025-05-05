
// 코스 스케줄
// 0을 완료하기 위해서는 1을 끝내야 한다는 것을 [0, 1] 쌍으로 표현하는 n개의 코스가 있다.
// 코스 개수 n과 이 쌍들을 입력으로 받았을ㄷ 때 모든 코스가 완료 가능한지 판별하라.
using System.Text;

public class Program {

    public static void MySolution(int courseCount, List<int[]> sites) {
        
        var graph = new Dictionary<int, List<int>>();
        foreach(var site in sites) {
            if( graph.ContainsKey(site[0]) == false ) {
                graph.Add(site[0], new());
            }

            graph[site[0]].Add(site[1]);
        }

        var trace = new HashSet<int>();

        bool Dfs(int vertex) {

            if( trace.Contains(vertex) == true ) {
                return false;
            }

            trace.Add(vertex);
            if( graph.ContainsKey(vertex) == true ) {
                
                foreach(var nextVertex in graph[vertex]) {
                    if( Dfs(nextVertex) == false ) {
                        return false;
                    }
                }
            }

            trace.Remove(vertex);

            return true;
        }

        var isEnableFinish = true;
        foreach(var entry in graph) {
            if( Dfs(entry.Key) == false ) {
                isEnableFinish = false;
                break;
            }

            if( isEnableFinish == false) {
                break;
            }
        }

        Console.WriteLine(isEnableFinish);
    }

    public static void Main(string[] args) {
        var questions = new List<(int count, List<int[]> courses)>() {
            (
                count: 2,
                courses: new List<int[]> {
                    new int[] { 1, 0 }
                }
            ), // true
            (
                count: 2,
                courses: new List<int[]> {
                    new int[] { 1, 0 },
                    new int[] { 0, 1 }
                }
            ), // false
            (
                count: 3,
                courses: new List<int[]> {
                    new int[] { 0, 1 },
                    new int[] { 0, 2 },
                    new int[] { 1, 2 }
                }
            ), // true
            (
                count: 4,
                courses: new List<int[]> {
                    new int[] { 0, 1 },
                    new int[] { 0, 2 },
                    new int[] { 1, 2 },
                    new int[] { 3, 1 }
                }
            ), // true
            (
                count: 5,
                courses: new List<int[]> {
                    new int[] { 0, 1 },
                    new int[] { 0, 2 },
                    new int[] { 1, 2 },
                    new int[] { 3, 1 },
                    new int[] { 4, 3 }
                }
            ), // true
            (
                count: 5,
                courses: new List<int[]> {
                    new int[] { 0, 1 },
                    new int[] { 0, 2 },
                    new int[] { 1, 2 },
                    new int[] { 3, 1 },
                    new int[] { 4, 3 },
                    new int[] { 2, 4 }
                }
            ) // false
        };

        string BuildQuestionString(int count, List<int[]> sites) {
            var builder = new StringBuilder();
            builder.Append($"count : {count}, ");

            var siteStrings = sites.Select(e => $"[{string.Join(",", e)}]");
            builder.Append($"[{string.Join(", ", siteStrings)}]");

            return builder.ToString();
        }

        foreach(var question in questions) {
            Console.WriteLine(BuildQuestionString(question.count, question.courses));
            MySolution(question.count, question.courses);
        }
    }
}