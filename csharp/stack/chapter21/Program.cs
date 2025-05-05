using System.Collections;
using System.Linq;

// 중복 문자 제거
public partial class Program {

    public static string StackSolution(string word) {

        var stack = new Stack<char>();
        var chCounter = word
            .GroupBy((e) => e)
            .Select((e) => new {ch = e.Key, count = e.Count()})
            .ToDictionary((e) => e.ch, (e) => e.count);

        var seen = new HashSet<char>();

        foreach(var ch in word) {
            chCounter[ch]--;

            if( seen.Contains(ch) == true ) {
                continue;
            }

            while(
                stack.TryPeek(out var checkCh) &&
                ch < checkCh && 
                chCounter[checkCh] > 0
            ) {
                seen.Remove(stack.Pop());
            }

            seen.Add(ch);
            stack.Push(ch);
        }

        return string.Join("", stack.Reverse());
    }

    public static string RecursiveSolution(string word) {

        string removeDuplicateLetters(string words) {

            var sorted = words.ToHashSet().ToList();
            sorted.Sort();

            foreach(var ch in sorted) {
                var suffix = words.Substring(words.IndexOf(ch));

                if( words.ToHashSet().SetEquals(suffix.ToHashSet()) == true ) {
                
                    var newWords = new string(suffix.Where((e) => e != ch).ToArray());
                    return ch + removeDuplicateLetters(newWords);
                }
            }

            return "";
        }

        return removeDuplicateLetters(word);
    }


    public static void Main(string[] args) {
        var questions = new string[] {
            "bcabc", // abc
            "cbacdcbc", // acdb
            "a", // a
            "ab", // ab
            "abc", // abc
            "abac", // abc
            "aaab", // ab
            "abab", // ab
            "cccc", // c
        };

        foreach(var question in questions) {
            //var result = RecursiveSolution(question);
            var result = StackSolution(question);
            Console.WriteLine($"{question} = {result}");
            break;
        }
    }
}