# Encode and Decode Strings

Design an algorithm to encode a list of strings into a single string. The encoded string is sent over a network and then decoded back into the original list of strings.

* **Machine 1 (Sender)** executes:
`String encoded_string = encode(strs);`
* **Machine 2 (Receiver)** executes:
`List<String> decoded_strs = decode(encoded_string);`

The `decoded_strs` array on Machine 2 must match the original `strs` array from Machine 1.

---

### Examples

**Example 1:**

* **Input:** `strs = ["Hello", "World"]`
* **Output:** `["Hello", "World"]`
* **Explanation:** `encode(strs)` converts the list to a single serialized string, which is then passed to `decode()` to reconstruct `["Hello", "World"]`.

**Example 2:**

* **Input:** `strs = [""]`
* **Output:** `[""]`

**Example 3:**

* **Input:** `strs = ["neet", "co#de", "123"]`
* **Output:** `["neet", "co#de", "123"]`
* **Explanation:** The algorithm correctly handles strings that contain potential delimiter characters like `#`.

**Topics:** String, Array, Design

---

### Hints

1. **Hint 1:** A naive approach of using a simple delimiter (like `,` or `#`) fails because those characters might naturally appear inside the string content.
2. **Hint 2:** Think about how you can encode the length of each individual string before the string itself. How do you distinguish between digits representing length and digits inside the content?
3. **Hint 3:** Use a length-prefix format like `[Length]#[String]`. When decoding, read characters until you hit `#` to extract the integer length $L$, then read exactly $L$ characters to extract the original string.