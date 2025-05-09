
public class Program {

    public record Question(string s, int k);

    public static void MySolution(Question question) {

        (var s, var k) = question;
        var chCount = new Dictionary<char, int>();
        var maxCharLength = 0;

        int left = 0, right = 0;
        for(right = 0 ; right < s.Length; right++) {
            var ch = s[right];
            if( chCount.ContainsKey(ch) == false ) {
                chCount[ch] = 0;
            }

            chCount[ch]++;
            maxCharLength = chCount.OrderByDescending(e => e.Value).First().Value;

            if( (right + 1) - left - maxCharLength > k ) {
                chCount[ch]--;
                left += 1;
            }
        }

        var result = right - left;
        Console.WriteLine(result);

    }

    public static void Main(string[] args) {
        
        var question = new Question(
            s: "AAABBCC",
            k: 2
        );

        MySolution(question);
    }
}