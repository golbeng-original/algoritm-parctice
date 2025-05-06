using System.Collections.Generic;

namespace Chapter40;

using NextVertexInfos = List<(int vertex, int weight)>;

// 네트워크 딜레이 타임
public class Program {

    public static int MySolution(int[][] pathInfos, int k,int n) {
        
        var graph = new Dictionary<int, NextVertexInfos>();

        foreach(var pathInfo in pathInfos) {
            if( graph.ContainsKey(pathInfo[0]) == false) {
                graph.Add(pathInfo[0], new NextVertexInfos());
            }

            graph[pathInfo[0]].Add((pathInfo[1], pathInfo[2]));
        }
        
        // time, 최근 노드
        var dist = new Dictionary<int, int>();

        var priorityQueue = new PriorityQueue<int, int>();
        priorityQueue.Enqueue(k, 0);

        while( priorityQueue.Count > 0 ) {

            priorityQueue.TryDequeue(out var node, out var time);

            if( dist.ContainsKey(node) == true) {
                continue;
            }

            dist[node] = time;
            if( graph.ContainsKey(node) == false ) {
                continue;
            }

            foreach(var nextVertex in graph[node]) {
                var accTime = time + nextVertex.weight;
                priorityQueue.Enqueue(nextVertex.vertex, accTime);
            }
        }

        if( dist.Count != n ) {
            return -1;
        }

        return dist.Values.Max();
    }

    public static void Main(string[] args) {    
        var questions = new List<(int k, int n, int[][] pathInfos)>() {
            (
                k: 2,
                n: 4,
                pathInfos: new int[][] {
                    [2, 1, 1],
                    [2, 3, 1],
                    [3, 4, 1],
                }
            ), // 2
            (
                k: 1,
                n: 5,
                pathInfos: new int[][] {
                    [1, 2, 1],
                    [2, 3, 2],
                    [1, 3, 4],
                    [1, 4, 5],
                    [4, 5, 6],
                }
            ), // 11
        };
    
        foreach(var question in questions) {
            var result = MySolution(question.pathInfos, question.k, question.n);
            Console.WriteLine(result);
            break;
        }
    }
}