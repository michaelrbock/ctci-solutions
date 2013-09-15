// Assumed to be implemented inside a LinkedList implementation
// i.e. a method of a LinkedList class
import java.util.HashMap;

public void deleteDuplicates(E item) {
	HashMap<String, Integer> counts = new HashMap<String, Integer>();
	Node<E> current = head;

	// count each item in hash table, then go
	// through and delete duplicates

	while (current != null) {
		if (counts.containsKey(current.element.toString())) {
			counts.put(current.element.toString(),
				counts.get(current.element.toString() + 1));
		}
		else {
			counts.put(current.element.toString(), 1);
		}
		current = current.next;
	}
	// now delete
	Node<E> prev = null;
	current = head;
	while (current != null) {
		if (counts.get(current.element.toString()) > 1) {
			if (current == head) {
				head = head.next;
			}
			else {
				current = current.next;
				prev.next = current;
			}
		}
		current = current.next;
		prev = prev.next;
	}
}