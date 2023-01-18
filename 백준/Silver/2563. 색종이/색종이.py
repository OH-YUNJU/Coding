n = int(input())
papers = []
for i in range(n):
    papers.append(map(int, input().split()))
def black_paper_area(num_papers, papers):
    # Initialize a 100x100 white paper
    white_paper = [[0 for _ in range(100)] for _ in range(100)]
    covered_area = 0

    for i in range(num_papers):
        x, y = papers[i]
        for row in range(x, x + 10):
            for col in range(y, y + 10):
                if white_paper[row][col] == 0:
                    white_paper[row][col] = 1
                    covered_area += 1
    return covered_area

num_papers = n
print(black_paper_area(num_papers, papers))