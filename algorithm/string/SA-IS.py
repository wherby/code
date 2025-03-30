# https://live.bilibili.com/1315966?broadcast_type=0&is_room_feed=1&spm_id_from=333.999.live_users_card.0.click&live_from=86001


def SA_IS(s):
    """
    Construct the suffix array of a string using the SA-IS algorithm.
    
    Args:
        s (str): Input string
        
    Returns:
        list: Suffix array of the input string
    """
    if not s:
        return []
    
    # Add sentinel character if not present
    if s[-1] != chr(0):
        s += chr(0)
    
    # Classify each character as L-type or S-type
    typ = [None] * len(s)  # True for S-type, False for L-type
    typ[-1] = True  # The sentinel is S-type
    
    if len(s) > 1:
        typ[-2] = False  # The second last character is L-type
        
        # Classify from right to left
        for i in range(len(s)-3, -1, -1):
            if s[i] < s[i+1]:
                typ[i] = True
            elif s[i] > s[i+1]:
                typ[i] = False
            else:
                typ[i] = typ[i+1]
    
    # Find all LMS (Left-Most S-type) characters
    is_lms = [False] * len(s)
    for i in range(1, len(s)):
        if typ[i] and not typ[i-1]:
            is_lms[i] = True
    
    # Bucket sort all LMS substrings
    def induced_sort(lms):
        # Initialize suffix array
        sa = [-1] * len(s)
        
        # Count characters for bucket sizes
        bucket_sizes = [0] * 256
        for ch in s:
            bucket_sizes[ord(ch)] += 1
        
        # Find bucket ends
        bucket_ends = []
        for size in bucket_sizes:
            if bucket_ends:
                bucket_ends.append(bucket_ends[-1] + size)
            else:
                bucket_ends.append(size)
        
        # Place LMS suffixes in their buckets
        bucket = bucket_ends.copy()
        for i in reversed(lms):
            ch = ord(s[i])
            bucket[ch] -= 1
            sa[bucket[ch]] = i
        
        # Induce L-type suffixes
        bucket = bucket_ends.copy()
        for i in range(len(s)):
            if sa[i] == -1:
                continue
            if sa[i] > 0 and not typ[sa[i]-1]:
                ch = ord(s[sa[i]-1])
                sa[bucket[ch-1]] = sa[i]-1
                bucket[ch-1] += 1
        
        # Induce S-type suffixes
        bucket = bucket_ends.copy()
        for i in reversed(range(len(s))):
            if sa[i] == -1:
                continue
            if sa[i] > 0 and typ[sa[i]-1]:
                ch = ord(s[sa[i]-1])
                bucket[ch] -= 1
                sa[bucket[ch]] = sa[i]-1
        
        return sa
    
    # Get all LMS positions
    lms_positions = [i for i in range(len(s)) if is_lms[i]]
    
    # Perform initial induced sort
    sa = induced_sort(lms_positions)
    
    # Extract LMS substrings from SA
    lms_substrings = []
    for i in range(len(sa)):
        if is_lms[sa[i]]:
            lms_substrings.append(sa[i])
    
    # Assign names to LMS substrings
    name = 0
    prev = None
    names = [-1] * len(s)
    for pos in lms_substrings:
        # Check if current LMS substring is different from previous
        different = False
        if prev is None:
            different = True
        else:
            for i in range(len(s)):
                if s[pos+i] != s[prev+i] or is_lms[pos+i] != is_lms[prev+i]:
                    different = True
                    break
                if i > 0 and (is_lms[pos+i] or is_lms[prev+i]):
                    break
        
        if different:
            name += 1
            prev = pos
        
        names[pos] = name - 1
    
    # Build reduced string
    reduced_s = [names[i] for i in range(len(names)) if is_lms[i]]
    
    if name < len(reduced_s):
        # Recursively compute SA of reduced string
        reduced_sa = SA_IS(reduced_s)
    else:
        # Directly compute SA of reduced string
        reduced_sa = [-1] * len(reduced_s)
        for i in range(len(reduced_s)):
            reduced_sa[reduced_s[i]] = i
    
    # Get sorted LMS positions
    sorted_lms = [lms_positions[i] for i in reduced_sa]
    
    # Perform final induced sort
    sa = induced_sort(sorted_lms)
    
    # Remove sentinel if it was added
    if s[-1] == chr(0):
        sa = sa[1:]
    
    return sa

# Example usage
if __name__ == "__main__":
    text = "banana"
    sa = SA_IS(text)
    print("Suffix array for 'banana':", sa)
    
    # Verify with naive implementation
    def naive_suffix_array(s):
        return sorted(range(len(s)), key=lambda i: s[i:])
    
    naive_sa = naive_suffix_array(text)
    print("Naive suffix array:", naive_sa)
    print("Verification:", sa == naive_sa)