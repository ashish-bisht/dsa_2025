# Reversing a Linked List: A Complete Guide

## Introduction

Imagine a train where each car is connected to the one in front of it. What if you wanted to make the last car become the first, and the first car become the last? You'd need to reverse the entire train! This is exactly what we do when we reverse a linked list.

Reversing a linked list is one of the most fundamental linked list operations and a very common interview question. In this article, I'll explain how to reverse a linked list in the simplest way possible, with step-by-step visuals and detailed explanations.

## What is a Linked List?

Before we dive in, let's make sure we understand what a linked list is:

A linked list is a chain of nodes, where each node contains:
1. A piece of data (a value)
2. A pointer to the next node in the chain

The first node is called the "head" and the last node points to "null" (indicating the end of the list).

Here's a simple linked list with 5 nodes:

```
head
 ↓
[1] → [2] → [3] → [4] → [5] → null
```

## The Problem: Reversing a Linked List

When we reverse a linked list, we want to flip all the pointers so that each node points to the previous node instead of the next node. The head becomes the tail, and the tail becomes the head.

We want to transform this:

```
head
 ↓
[1] → [2] → [3] → [4] → [5] → null
```

Into this:

```
                              head
                               ↓
null ← [1] ← [2] ← [3] ← [4] ← [5]
```

## The Challenge

The challenge when reversing a linked list is that once you change a node's next pointer, you lose access to the next node in the original list! So we need to be careful about the order in which we change things.

## The Solution: Three Pointers Technique

The most intuitive way to reverse a linked list is to use three pointers:

1. `previousNode`: Points to the node that will come after the current node in the reversed list
2. `currentNode`: Points to the node we're currently processing
3. `nextNode`: Temporarily stores the next node in the original list before we change the current node's pointer

Let's see how this works step by step.

## The Algorithm in Action

Let's start with this linked list:

```
head
 ↓
[1] → [2] → [3] → [4] → [5] → null
```

### Initialization

First, we initialize our three pointers:

```
previousNode = null
currentNode = head (which is node [1])
nextNode = not set yet
```

### Step 1: Save the Next Node

Before changing any pointers, we save the next node in the original list:

```
nextNode = currentNode.next  (which is node [2])
```

Our pointers now look like this:

```
previousNode   currentNode   nextNode
     ↓             ↓            ↓
    null          [1] → [2] → [3] → [4] → [5] → null
```

### Step 2: Reverse the Current Node's Pointer

Now we change the current node's next pointer to point to the previous node:

```
currentNode.next = previousNode
```

After this change:

```
previousNode   currentNode     nextNode
     ↓             ↓              ↓
    null  ←  [1]    [2] → [3] → [4] → [5] → null
```

Notice how node [1] now points to null instead of node [2].

### Step 3: Move Both Pointers Forward

Now we move both pointers one step forward to process the next node:

```
previousNode = currentNode  (previousNode becomes node [1])
currentNode = nextNode      (currentNode becomes node [2])
```

After moving the pointers:

```
              previousNode   currentNode
                   ↓             ↓
    null  ←  [1]    [2] → [3] → [4] → [5] → null
```

### Step 4: Repeat Until the End

We repeat steps 1-3 for each node in the list. Let's continue with the next iteration:

**Save the next node:**
```
nextNode = currentNode.next  (which is node [3])
```

**Reverse the pointer:**
```
currentNode.next = previousNode
```

After these changes:

```
              previousNode   currentNode     nextNode
                   ↓             ↓              ↓
    null  ←  [1]  ←  [2]    [3] → [4] → [5] → null
```

**Move the pointers forward:**
```
previousNode = currentNode  (previousNode becomes node [2])
currentNode = nextNode      (currentNode becomes node [3])
```

After moving the pointers:

```
                            previousNode   currentNode
                                 ↓             ↓
    null  ←  [1]  ←  [2]    [3] → [4] → [5] → null
```

We repeat this process for each node until `currentNode` becomes null (meaning we've processed all nodes).

### Final State

After processing all nodes, our list will look like:

```
                                          previousNode   currentNode
                                               ↓             ↓
    null  ←  [1]  ←  [2]  ←  [3]  ←  [4]  ←  [5]          null
```

And `previousNode` now points to the new head of our reversed list (node [5])!

## Visual Step-by-Step Execution

Let's walk through the entire process with a visualization for our example list:

**Initial state:**
```
head = [1]
previousNode = null
currentNode = [1]
nextNode = not set yet

[1] → [2] → [3] → [4] → [5] → null
```

**Iteration 1:**
```
1. nextNode = [2]
2. [1].next = null
3. previousNode = [1]
4. currentNode = [2]

null ← [1]  [2] → [3] → [4] → [5] → null
```

**Iteration 2:**
```
1. nextNode = [3]
2. [2].next = [1]
3. previousNode = [2]
4. currentNode = [3]

null ← [1] ← [2]  [3] → [4] → [5] → null
```

**Iteration 3:**
```
1. nextNode = [4]
2. [3].next = [2]
3. previousNode = [3]
4. currentNode = [4]

null ← [1] ← [2] ← [3]  [4] → [5] → null
```

**Iteration 4:**
```
1. nextNode = [5]
2. [4].next = [3]
3. previousNode = [4]
4. currentNode = [5]

null ← [1] ← [2] ← [3] ← [4]  [5] → null
```

**Iteration 5:**
```
1. nextNode = null
2. [5].next = [4]
3. previousNode = [5]
4. currentNode = null

null ← [1] ← [2] ← [3] ← [4] ← [5]
```

**Final state:**
```
The loop terminates because currentNode is null.
New head = previousNode = [5]

null ← [1] ← [2] ← [3] ← [4] ← [5]
                               ↑
                              head
```

## The Code (Simple Version)

Here's the algorithm written in Python:

```python
def reverse_linked_list(head):
    previous_node = None
    current_node = head
    
    while current_node is not None:
        # Save the next node
        next_node = current_node.next
        
        # Reverse the pointer
        current_node.next = previous_node
        
        # Move pointers one step forward
        previous_node = current_node
        current_node = next_node
    
    # previousNode is now the new head
    new_head = previous_node
    return new_head
```

## Detailed Python Implementation

Here's a more complete version with a Node class and helper functions:

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.value))
            current = current.next
        return " → ".join(elements) + " → null"
    
    def reverse(self):
        previous_node = None
        current_node = self.head
        
        print("Starting to reverse the linked list...")
        print(f"Initial list: {self.print_list()}")
        
        step = 1
        while current_node:
            # Save next node
            next_node = current_node.next
            
            # Print the current state
            print(f"\nStep {step}:")
            print(f"  previousNode points to {previous_node.value if previous_node else 'null'}")
            print(f"  currentNode points to {current_node.value}")
            print(f"  nextNode points to {next_node.value if next_node else 'null'}")
            
            # Reverse the pointer
            current_node.next = previous_node
            print(f"  Reversed currentNode.next to point to previousNode")
            
            # Move pointers forward
            previous_node = current_node
            current_node = next_node
            print(f"  Moved previousNode to {previous_node.value}")
            print(f"  Moved currentNode to {next_node.value if next_node else 'null'}")
            
            # Show the partial reversal
            temp_list = LinkedList()
            temp_list.head = self.head
            
            # Create a temporary list to display the current state
            reversed_part = LinkedList()
            reversed_part.head = previous_node
            
            remaining_part = LinkedList()
            remaining_part.head = next_node
            
            if next_node:
                print(f"  Current state: null ← ... ← {previous_node.value} | {next_node.value} → ...")
            else:
                print(f"  Final state: null ← ... ← {previous_node.value} | null")
            
            step += 1
        
        # Update the head to the new start of the reversed list
        self.head = previous_node
        print(f"\nReversed list: {self.print_list()}")
```

## Testing Our Implementation

Let's test our reversal function with the example list:

```python
# Create and populate the linked list
my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

print("Original list:", my_list.print_list())
my_list.reverse()
print("Reversed list:", my_list.print_list())
```

Output:
```
Original list: 1 → 2 → 3 → 4 → 5 → null
Starting to reverse the linked list...
Initial list: 1 → 2 → 3 → 4 → 5 → null

Step 1:
  previousNode points to null
  currentNode points to 1
  nextNode points to 2
  Reversed currentNode.next to point to previousNode
  Moved previousNode to 1
  Moved currentNode to 2
  Current state: null ← 1 | 2 → ...

Step 2:
  previousNode points to 1
  currentNode points to 2
  nextNode points to 3
  Reversed currentNode.next to point to previousNode
  Moved previousNode to 2
  Moved currentNode to 3
  Current state: null ← ... ← 2 | 3 → ...

Step 3:
  previousNode points to 2
  currentNode points to 3
  nextNode points to 4
  Reversed currentNode.next to point to previousNode
  Moved previousNode to 3
  Moved currentNode to 4
  Current state: null ← ... ← 3 | 4 → ...

Step 4:
  previousNode points to 3
  currentNode points to 4
  nextNode points to 5
  Reversed currentNode.next to point to previousNode
  Moved previousNode to 4
  Moved currentNode to 5
  Current state: null ← ... ← 4 | 5 → ...

Step 5:
  previousNode points to 4
  currentNode points to 5
  nextNode points to null
  Reversed currentNode.next to point to previousNode
  Moved previousNode to 5
  Moved currentNode to null
  Final state: null ← ... ← 5 | null

Reversed list: 5 → 4 → 3 → 2 → 1 → null
```

## The Recursive Approach

There's also a recursive way to reverse a linked list. It's a bit more challenging to understand but very elegant:

```python
def reverse_linked_list_recursive(head):
    # Base case: empty list or list with only one node
    if head is None or head.next is None:
        return head
    
    # Recursive case: reverse the rest of the list
    new_head = reverse_linked_list_recursive(head.next)
    
    # Change the next node's pointer to point to the current node
    head.next.next = head
    
    # Set the current node's next to null (will be overwritten for all but the original head)
    head.next = None
    
    # Return the new head of the reversed list
    return new_head
```

### How the Recursive Approach Works

The recursive approach is a bit mind-bending at first. Let's break it down:

1. We keep going deeper in the recursion until we reach the last node.
2. The last node becomes our new head.
3. As we unwind the recursion, we make each node point to the previous node.

Let's visualize the recursion for our example list:

**Initial list:** `1 → 2 → 3 → 4 → 5 → null`

**Recursive calls:**
```
reverse_linked_list_recursive(1)
  reverse_linked_list_recursive(2)
    reverse_linked_list_recursive(3)
      reverse_linked_list_recursive(4)
        reverse_linked_list_recursive(5)
          Base case: 5.next is null, so return 5 as the new head
        4.next.next = 4  (makes 5 point to 4)
        4.next = null
        Return 5 as the new head
      3.next.next = 3  (makes 4 point to 3)
      3.next = null
      Return 5 as the new head
    2.next.next = 2  (makes 3 point to 2)
    2.next = null
    Return 5 as the new head
  1.next.next = 1  (makes 2 point to 1)
  1.next = null
  Return 5 as the new head
```

**Final reversed list:** `5 → 4 → 3 → 2 → 1 → null`

## Time and Space Complexity

For both the iterative and recursive approaches:

- **Time Complexity**: O(n) where n is the number of nodes in the linked list. We need to visit each node exactly once.
- **Space Complexity**: O(1) for the iterative approach as we only use a fixed number of pointers. O(n) for the recursive approach due to the call stack.

## Why This Operation Is Important

Reversing a linked list is important for several reasons:

1. It's a fundamental operation that tests your understanding of pointer manipulation.
2. Many complex linked list problems involve reversing parts of the list.
3. It's a common interview question because it tests your ability to think about data structures.
4. Real-world applications include implementing undo functionality or reversing the order of items in a system.

## Common Mistakes to Avoid

1. **Forgetting to save the next node**: If you change the current node's next pointer without saving the next node first, you'll lose access to the rest of the list.
2. **Not updating the head**: After reversing, you need to update the head to point to the new first node (which was the last node in the original list).
3. **Incorrect handling of null values**: Be careful about edge cases like empty lists or lists with only one node.

## Practice Variations

Once you understand the basic reversal, try these variations:

1. **Reverse a linked list between positions m and n**: Only reverse a specific section of the linked list.
2. **Reverse a linked list in groups of k**: Reverse every k nodes as a group.
3. **Reverse alternate k nodes**: Reverse k nodes, then leave k nodes, then reverse the next k, and so on.

## Real-world Applications

Reversing a linked list has applications in:

1. **Text editors**: Implementing undo/redo functionality
2. **Browser history**: Navigating back and forth
3. **Route planning algorithms**: Reversing paths for bidirectional routes
4. **Game development**: Reversing action sequences

## Summary

Reversing a linked list involves changing the direction of all the next pointers in the list. We can do this using:

1. **Iterative approach**: Using three pointers (previous, current, next) to carefully change each pointer without losing our place.
2. **Recursive approach**: Using the call stack to remember our position and working backward from the end of the list.

The key insight is to carefully save the next node before changing the current node's pointer to avoid losing access to parts of the list.

Practice this technique until you can reverse a linked list in your sleep - it's a fundamental skill for mastering linked list operations!

---

# Practice Problems

To solidify your understanding of linked list reversal, try these problems:

1. **Palindrome Linked List**: Check if a linked list is a palindrome. Hint: Reverse the second half and compare with the first half.

2. **Reorder List**: Reorder a linked list such that L₀ → L₁ → ... → Lₙ₋₁ → Lₙ becomes L₀ → Lₙ → L₁ → Lₙ₋₁ → .... Hint: Find the middle, reverse the second half, and merge.

3. **Reverse Nodes in k-Group**: Reverse the nodes of a linked list k at a time. Hint: Count k nodes, reverse them, connect with previous groups.

Remember, the best way to truly understand linked list operations is to implement them yourself and trace through examples on paper!