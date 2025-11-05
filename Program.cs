public class SinglyLinkedList<T>
{
    public class Cell
    {
        public T Data;
        public Cell Next;
        public Cell(T data, Cell next = null)
        {
            Data = data;
            Next = next;
        }
    }

    private Cell first;
    public Cell Head => first;



    public void InsertNth(int index, T data)
    {
        if (index < 0 || index > Count())
            throw new ArgumentOutOfRangeException(nameof(index));

        if (index == 0)
        {
            AddF(data);
            return;
        }

        var current = first;
        for (int i = 0; i < index - 1; i++)
            current = current.Next;

        current.Next = new Cell(data, current.Next);
    }

    public void Reverse()
    {
        Cell prev = null, current = first, next = null;
        while (current != null)
        {
            next = current.Next;
            current.Next = prev;
            prev = current;
            current = next;
        }
        first = prev;
    }


    public (Cell Front, Cell Back) FrontBackSplit()
    {
        if (first == null)
            return (null, null);
        if (first.Next == null)
            return (first, null);

        Cell slow = first;
        Cell fast = first.Next;

        while (fast != null)
        {
            fast = fast.Next;
            if (fast != null)
            {
                slow = slow.Next;
                fast = fast.Next;
            }
        }

        Cell front = first;
        Cell back = slow.Next;
        slow.Next = null;

        return (front, back);
    }
}

class Program
{
    static void Print<T>(string label, SinglyLinkedList<T> list, SinglyLinkedList<T>.Cell headOverride = null)
    {
        var cur = headOverride ?? list.Head;
        var parts = new List<string>();
        while (cur != null)
        {
            parts.Add(cur.Data?.ToString());
            cur = cur.Next;
        }
        Console.WriteLine($"{label} [{string.Join(" -> ", parts)}]");
    }

    static void Main()
    {

        var ex1 = new SinglyLinkedList<int>();
        foreach (var v in new[] { 10, 20, 30, 40 }) ex1.AddL(v);
        Print("start", ex1);
        ex1.InsertNth(0, 5);
        ex1.InsertNth(3, 25);
        ex1.InsertNth(ex1.Count(), 50);
        Print("after ex1", ex1);

        Console.WriteLine();


        var ex2 = new SinglyLinkedList<int>();
        foreach (var v in new[] { 1, 2, 3, 4 }) ex2.AddL(v);
        Print("start", ex2);
        ex2.Reverse();
        Print("after reverse", ex2);

        Console.WriteLine();


        var ex3 = new SinglyLinkedList<int>();
        foreach (var v in new[] { 1, 2, 3, 4, 5 }) ex3.AddL(v);
        Print("start", ex3);
        var (front, back) = ex3.FrontBackSplit();
        Print("front", ex3, front);
        Print("back", ex3, back);
    }
}
