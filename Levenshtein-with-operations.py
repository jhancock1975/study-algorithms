def levenshteinDistance(str1, str2):
    edits = [[0 for _ in range(len(str1)+1)] for __ in range(len(str2)+1)]
    for row in range(len(str2)+1):
        edits[row][0] = row
    for col in range(len(str1)+1):
        edits[0][col] = col
    for row in range(1, len(str2)+1):
        for col in range(1, len(str1)+1):
            if str1[col-1] == str2[row-1]:
                edits[row][col] = edits[row-1][col-1]
            else:
                edits[row][col] = 1 + min(edits[row-1][col-1], edits[row-1][col], edits[row][col-1])

      # 2) Back‑track to find which operations were used
    operations = []
    r, c = len(str2), len(str1)
    while r > 0 or c > 0:
        # If both chars match and cost came diagonally, it's a match
        if r > 0 and c > 0 and str1[c-1] == str2[r-1] and edits[r][c] == edits[r-1][c-1]:
            operations.append(f"Match '{str1[c-1]}'")
            r -= 1
            c -= 1
        # Substitution
        elif r > 0 and c > 0 and edits[r][c] == edits[r-1][c-1] + 1:
            operations.append(f"Substitute '{str1[c-1]}' → '{str2[r-1]}'")
            r -= 1
            c -= 1
        # Deletion (delete from str1)
        elif c > 0 and edits[r][c] == edits[r][c-1] + 1:
            operations.append(f"Delete '{str1[c-1]}'")
            c -= 1
        # Insertion (insert into str1)
        elif r > 0 and edits[r][c] == edits[r-1][c] + 1:
            operations.append(f"Insert '{str2[r-1]}'")
            r -= 1
        else:
            # Shouldn't happen
            raise RuntimeError("Backtrack error at edits[{},{}]=={}".format(r, c, edits[r][c]))

    # Operations were collected in reverse order
    operations.reverse()

    # Print them
    print("Operations to transform")
    print('"'+str1)
    print('"'+str2)
    for i, op in enumerate(operations, 1):
        print(f"{i}. {op}")
    return edits[-1][-1]
    
