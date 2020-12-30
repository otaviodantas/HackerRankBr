# hackerrank.com/challenges/designer-pdf-viewer
# score: 20


def designerPdfViewer(h, word):
    p = [h[ord(str(i)) - ord('a')] for i in word]
    return max(p) * len(word)
