
partial class Program {

    public static void Merge(int[] arr, int left, int middle, int right) {

        var helper = new int[arr.Length];
        for( var i = left ; i <= right  ; i++ ) {
            helper[i] = arr[i];
        }

        int helperLeft = left;
        int helperRight = middle + 1;
        int current = left;

        while( helperLeft <= middle && helperRight <= right ) {
            if( helper[helperLeft] <= helper[helperRight] ) {
                arr[current] = helper[helperLeft];
                helperLeft++;
            }
            else {
                arr[current] = helper[helperRight];
                helperRight++;
            }

            current++;
        }

        while( helperLeft <= middle ) {
            arr[current++] = helper[helperLeft++];
        }
    }

    public static void MergeSort(int[] arr, int left, int right) {

        if( left < right ) {

            var middle = (left + right) / 2;
            MergeSort(arr, left, middle);
            MergeSort(arr, middle + 1, right);

            Merge(arr, left, middle, right);
        }
    }

    public static void MergeSortForListNode(int[] arr) {

        var root = ListNode<int>.CreateFromRaw(arr);

        ListNode<int>? MergeSort(ListNode<int>? head) {

            if( head?.Next == null) {
                return head;
            }

            ListNode<int>? half = null;
            ListNode<int> slow = head;
            ListNode<int> fast = head;

            while( fast != null && fast.Next != null ) {
                (half, slow, fast) = (slow, slow.Next, fast.Next.Next);
            }

            if( half?.Next != null ) {
                half.Next = null;
            }

            var l1 = MergeSort(head);
            var l2 = MergeSort(slow);

            var sortedList = Merge(l1, l2);

            return sortedList;

        }

        ListNode<int> Merge(ListNode<int> lhs, ListNode<int> rhs) {
            
            if( lhs != null && rhs != null) {
                if( lhs.Value > rhs.Value) {
                    (lhs, rhs) = (rhs, lhs);
                }

                lhs.Next = Merge(lhs.Next, rhs);
            }

            return lhs ?? rhs;
        }

        var sortedRoot = MergeSort(root);
        var serialized = sortedRoot.Serialize();

        Console.WriteLine($"[{string.Join(", ", serialized)}]");

    }

    public static void MergeSortForRaw(int[] arr) {
        
        void MergeSort(int[] arr, int left, int right) {

            if( left >= right ) {
                return;
            }

            var mid = (right + left) / 2;

            MergeSort(arr, left, mid);
            MergeSort(arr, mid + 1, right);

            Merge(arr, left, mid + 1, right);
        }

        void Merge(int[] arr, int left, int mid, int right) {
            
            var length = (right - left) + 1;
            if( length <= 1) {
                return;
            }

            var temp = new int[length];
            Array.Copy(arr, left, temp, 0, length);

            var count = 0;
            var lhsIdx = left;
            var rhsIdx = mid;
            while( lhsIdx < mid && rhsIdx <= right) {
                
                if( arr[lhsIdx] <= arr[rhsIdx] ) {
                    temp[count++] = arr[lhsIdx++];
                }
                else {
                    temp[count++] = arr[rhsIdx++];
                }
            }

            while( lhsIdx < mid ) {
                temp[count++] = arr[lhsIdx++];
            }

            Array.Copy(temp, 0, arr, left, length); 
        }

        MergeSort(arr, 0, arr.Length - 1);

        Console.WriteLine($"[{string.Join(", ", arr)}]");
    }

    public static void Main(string[] args) {

        var question = new int[] {5, 3, 1, 10, 15, 19, 34, 9, 7, 24, 23};

        //MergeSort(question, 0 , question.Length - 1);
        //MergeSortForListNode(question);
        MergeSortForRaw(question);
        //var result = String.Join(", ", question);
        //Console.WriteLine(result);
    }
}