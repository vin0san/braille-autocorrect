'''#autocorrect code goes here

def autocorrect(seq1, seq2):
    
    m,n = len(seq1), len(seq2)
    dp = [[0]*(n+1) for i in range(m+1)]

    #Initialize the first row and column
    for i in range(m+1): dp[i][0] = i
    for j in range(n+1): dp[0][j] = j

    #Fill the dp table
    for i in range(1,m+1):
        for j in range(1,n+1):
            if sorted(seq1[i-1])== sorted(seq2[j-1]):
                if sorted(seq1[i - 1]) == sorted(seq2[j - 1]):
                    cost = 0
                else:
                    cost = 1
            else:
                dp[i][j] = min(
                    dp[i-1][j] + 1,    # Deletion
                    dp[i][j-1] + 1,    # Insertion
                    dp[i-1][j-1] + cost   # Substitution
                )
    return dp[m][n]

#suggestion function

def suggest_word(user_input_seq, braille_dict, max_suggestions=3):
    scored = []

    for word, braille_seq in braille_dict.items():
        distance = autocorrect(user_input_seq, braille_seq)
        scored.append((distance, word))

    # Sort by distance first, then alphabetically for tie-breakers
    scored = sorted(scored, key=lambda x: (x[0], x[1]))

    return [word for _, word in scored[:max_suggestions]]
'''



def autocorrect(seq1, seq2):
    m, n = len(seq1), len(seq2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if sorted(seq1[i - 1]) == sorted(seq2[j - 1]):
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,      # Deletion
                dp[i][j - 1] + 1,      # Insertion
                dp[i - 1][j - 1] + cost  # Substitution
            )
    return dp[m][n]

def suggest_word(user_input_seq, braille_dict, max_suggestions=3):
    scored = []

    for word, braille_seq in braille_dict.items():
        distance = autocorrect(user_input_seq, braille_seq)
        scored.append((distance, word))

    # Sort by distance first, then alphabetically for tie-breakers
    scored = sorted(scored, key=lambda x: (x[0], x[1]))

    return [word for _, word in scored[:max_suggestions]]