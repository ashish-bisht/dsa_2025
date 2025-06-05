
---

### quick.md

```markdown
# Rotate Array - Quick Recall

**Key Idea**: Rotate an array to the right by `k` steps in-place using a reverse-based approach. Reverse the entire array, then reverse the first `k` elements, and finally reverse the remaining `n-k` elements.

**Framework**:
1. Normalize `k` with `k = k % n` to handle `k > n`.
2. Reverse entire array: `reverse(0, n-1)`.
3. Reverse first `k` elements: `reverse(0, k-1)`.
4. Reverse remaining `n-k` elements: `reverse(k, n-1)`.

**Complexity**:
- Time: O(n)
- Space: O(1)

**Similar Problems**:
- Spiral Matrix (array manipulation)
- Rotate List (rotation in linked lists)
- Reverse Integer (reversal logic)
