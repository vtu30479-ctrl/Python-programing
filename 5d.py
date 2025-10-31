def selection_sort(scores):
    n = len(scores)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if scores[j] < scores[min_index]:
                min_index = j
        scores[i], scores[min_index] = scores[min_index], scores[i]
        print("After iteration", i+1, ":", scores)

exam_scores = [87, 65, 92, 78, 55, 70, 82]
print("Initial exam scores:", exam_scores)
print("Sorting using Selection Sort:")
selection_sort(exam_scores)
print("Final sorted exam scores:", exam_scores)
