
// 섬의 개수
using System.Runtime.CompilerServices;
using System.Text.RegularExpressions;

public partial class Program {

    public static void DfsSolution(string question) {
        var rawMaps = question.Split("\n");
        string[][] maps = new string[rawMaps.Length][];
        for(var rowIdx = 0 ; rowIdx < rawMaps.Length ; rowIdx++) {
            maps[rowIdx] = rawMaps[rowIdx].Select(e => e.ToString()).Where(e => Regex.IsMatch(e, @"\d+") ).ToArray();
        }

        bool dfs(int y, int x) {

            if( y < 0 || y >= maps.Length) {
                return false;
            }

            if( x < 0 || x >= maps.Length ) {
                return false;
            }

            if( maps[y][x] == "0" ) {
                return false;
            }

            maps[y][x] = "0";

            dfs(y, x + 1);
            dfs(y, x - 1);
            dfs(y - 1, x);
            dfs(y + 1, x);

            return true;
        }

        var islandCound = 0;
        for(var y = 0 ; y < maps.Length ; y++) {
            for(var x = 0 ; x < maps[y].Length ; x++) {

                if( dfs(y, x) ) {
                    islandCound++;
                }
            }
        }

        Console.WriteLine(islandCound);
    }

    public static void MySolution(string question) {

        var rawMaps = question.Split("\n");
        string[][] maps = new string[rawMaps.Length][];
        for(var rowIdx = 0 ; rowIdx < rawMaps.Length ; rowIdx++) {
            maps[rowIdx] = rawMaps[rowIdx].Select(e => e.ToString()).Where(e => Regex.IsMatch(e, @"\d+") ).ToArray();
        }
        
        var height = maps.Length;
        var width = maps[0].Length;
        var visited = new bool[height, width];

        bool isValidElement(int y, int x) {
            if( y >= height || x >= width ) {
                return false;
            }

            if( visited[y, x] == true ) {
                return false;
            }

            return maps[y][x].Equals("1");
        }

        bool findIsland(int startY, int startX) {

            if( isValidElement(startY, startX) == false ) {
                return false;
            }

            var queue = new Queue<(int y, int x)>();
            queue.Enqueue((startY, startX));

            while(queue.Count > 0) {
                var pivot = queue.Dequeue();
                visited[pivot.y, pivot.x] = true;

                var left = (y: pivot.y, x: pivot.x + 1);
                if( isValidElement(left.y, left.x) ) {
                    queue.Enqueue(left);
                }
                
                var bottom = (y: pivot.y + 1, x: pivot.x);
                if( isValidElement(bottom.y, bottom.x) ) {
                    queue.Enqueue(bottom);
                }
            }

            return true;
        }

        var islandCount = 0;
        for(var y = 0 ; y < height ; y++) {
            
             for(var x = 0 ; x < width; x++) {

                if( findIsland(y, x) == true) {
                    islandCount++;
                }
            }
        }

        Console.WriteLine(islandCount);
    }

    public static void Main(string[] args) {
        var questions = new string[] {
            @"11110
              11010
              11000
              00000", // 1
            @"11000
              11000
              00100
              00011", // 3
            @"11111
              10001
              10001
              10001
              11111", // 1
        };

        foreach(var question in questions) {
            var trimQuestion = string.Join("", question.Where(e => e != ' '));
            Console.WriteLine(trimQuestion);
            //MySolution(trimQuestion);
            DfsSolution(trimQuestion);
        }
    }
}