
// 전화번호 문자 조합
public class Program {

    public static Dictionary<string, string> keyboard = new (){
        ["2"] = "abc",
        ["3"] = "def",
        ["4"] = "ghr",
        ["5"] = "jkl",
        ["6"] = "mno",
        ["7"] = "pqrs",
        ["8"] = "tuv",
        ["9"] = "wxyz",
    };

    public static void MySolution(string question) {
        var output = new List<string>();
    
        void BackTracking(string digits, string madeAlphabet) {
            if( digits.Length == 0 ) {
                output.Add(madeAlphabet);
                return;
            }

            var digit = digits[0].ToString();
            if( keyboard.TryGetValue(digit, out var alphabets) == false ) {
                return;
            }

            foreach (var alphabet in alphabets) {
                BackTracking(digits[1..], madeAlphabet + alphabet.ToString());
            }
        }

        BackTracking(question, "");

        Console.WriteLine($"[{string.Join(", ", output)}]");
    }

    public static void Main(string[] args) {

        var questions = new string[] {
            "23", // ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
            "2", // ["a", "b", "c"]
            "7", // ["p", "q", "r", "s"]
            "78", // ["pt", "pu", "pv", "qt", "qu", "qv", "rt", "ru", "rv", "st", "su", "sv"]
            "234", // ["adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi", "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi", "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"]
        };

        foreach(var question in questions) {
            Console.WriteLine($"question = {question}");
            MySolution(question);
        }
    }

}