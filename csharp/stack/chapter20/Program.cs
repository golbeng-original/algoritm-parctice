using System.Collections.Generic;
using System.Linq;

public partial class Program {


    public static bool MySolution(string input) {
        var table = new Dictionary<char, char>() {
            [')'] = '(',
            [']'] = '[',
            ['}'] = '{'
        };

        var stack = new Stack<char>();

        foreach(var element in input) {

            if( table.ContainsKey(element) == false) {
                stack.Push(element);
                continue;
            }

            if( stack.Any() == true && table[element] != stack.Pop() ) {
                return false;
            }
        }

        return stack.Any() == true ? false : true;
    }

    private static void Main(string[] args)
    {
        var questions = new string[] {
            "()[]{}", // true
            "(]", // false
            "([)]", // false
            "{[]}", // true
            "((()))", // true
        };

        foreach(var question in questions) {
            var result = MySolution(question);
            Console.WriteLine($"{question} = {result}");
        }
    }
}