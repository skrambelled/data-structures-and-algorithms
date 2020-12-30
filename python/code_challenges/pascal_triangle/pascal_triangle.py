def pascal(depth, base=1):
    count = 0

    triangle = []

    while count < depth:
        row = [base]
        if count:
            prev_row = triangle[count-1]
            for i in range(1, len(prev_row)):
                row.append(prev_row[i] + prev_row[i-1])
            row.append(base)

        triangle.append(row)

        print(triangle[count])
        count += 1

    return triangle


print("\n", pascal(6, base=-1))
