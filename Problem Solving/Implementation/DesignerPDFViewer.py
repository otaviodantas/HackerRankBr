"""
HackerRank - Algorithms - Implemation
Designer PDF Viewer
"""

def designerPdfViewer(h, word):
    p = [h[ord(str(i)) - ord('a')] for i in word]
    return max(p) * len(word)
