import heapq
# --- DATA STRUCTURE ---
class Node:
    def __init__(self, char, frequency):
        self.char = char  # Stores the letter (or None for combined nodes)
        self.frequency = frequency  # How many times the character appears (node weight)
        self.left = None  # Pointer to the left child (0)
        self.right = None  # Pointer to the right child (1)
    
    # So that the heapq algorithm (priority queue) knows how to sort our nodes,
    # we must define the "less than" operator (<). We sort by frequency!
    def __lt__(self, other):
        return self.frequency < other.frequency

# --- MAIN TREE BUILDING FUNCTION ---
def build_huffman_tree(frequencies):
    queue = []
    # STEP 1: Organizing characters.
    # We create nodes for each character and push them into the queue.
    for char, freq in frequencies.items():
        heapq.heappush(queue, Node(char, freq))

    # REDUCTION PHASE (combining the two least probable characters)
    # We repeat the step until only 1 element remains in the queue (tree root)
    while len(queue) > 1:
        # We get (and remove from queue) two elements with the LOWEST frequency
        left_node = heapq.heappop(queue)
        right_node = heapq.heappop(queue)

        # We create a new, combined parent node. It has no own character (None).
        # Its frequency is simply the sum of the children's frequencies.
        sum_freq = left_node.frequency + right_node.frequency
        parent = Node(None, sum_freq)

        # We attach the extracted nodes as children of the new parent
        parent.left = left_node
        parent.right = right_node

        # We push the newly created parent back into the priority queue
        heapq.heappush(queue, parent)
        
    # At the end of the loop, only one element remains in the queue - the entire connected root
    return queue[0]

# --- RECURSIVE FUNCTION GENERATING CODES (0 and 1) ---
# CODE CONSTRUCTION PHASE

def generate_huffman_codes(node, current_code, code_dict):
    if node is None:
        return

    # If the node has a character (meaning it's a "leaf" and not a helper node),
    # we save the sequence of zeros and ones generated so far.
    if node.char is not None:
        code_dict[node.char] = current_code
        return

    # STEPS 4, 5 and 6: Assigning zeros and ones.
    # Going down to the left, we append '0' to the code
    generate_huffman_codes(node.left, current_code + "0", code_dict)

    # Going down to the right, we append '1' to the code
    generate_huffman_codes(node.right, current_code + "1", code_dict)


# === TEST DATA FROM PRESENTATION (Slides 9 and 10) ===
if __name__ == "__main__":
    # Input data from presentation: 6 characters and their frequencies
    lecture_frequencies = {
        'x1': 20,
        'x2': 17,
        'x3': 10,
        'x4': 9,
        'x5': 3,
        'x6': 1
    }
    # We build the tree
    tree_root = build_huffman_tree(lecture_frequencies)
    # We generate dictionary codes from it
    result_codes = {}
    generate_huffman_codes(tree_root, "", result_codes)
    print("--- RECEIVED HUFFMAN CODES ---")
    for char, code in sorted(result_codes.items(), key=lambda x: len(x[1])):
        amount = lecture_frequencies[char]
        print(f"Character {char} (amount: {amount:2d}) -> Code: {code}")
