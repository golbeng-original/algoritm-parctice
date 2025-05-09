
public class Program {

    public record Question(int K, int[][] points);

    public static void MySolution(Question question) {

        var nearByPoints = question.points.Select((e, idx) => {
            return (nomalize: Math.Sqrt(e[0] * e[0] + e[1] * e[1]), idx);
        })
        .OrderBy(e => e.nomalize)
        .Take(question.K);

        foreach(var nearByPoint in nearByPoints) {
            var point = question.points[nearByPoint.idx];
            Console.WriteLine($"[{point[0]}, {point[1]}]");
        }
    }

    public static void Main(string[] args) {

        var questions = new Question[] {
            new Question(
                K: 1, 
                points: [
                    [1, 3],
                    [-2, 2]
                ]
            ),
            new Question(
                K: 2,
                points: [
                    [3, 3],
                    [5, -1],
                    [-2, 4]
                ]
            )
        };

        foreach(var question in questions) {
            MySolution(question);
        }
    }
}