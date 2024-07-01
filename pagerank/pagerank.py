import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    print(corpus)
    print(page)
    print(damping_factor)
    
    ans = {}
    length = len(corpus)
    p = corpus[page]
    
    if p == None:
        for i in corpus:
            ans[i] = 1 / length
    else:      
        for i in corpus:
            ans[i] = (1 - damping_factor) / length
            if i in p:
                ans[i] += damping_factor / len(p)
    
    return ans


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    print('corpus', corpus)
    
    corp = corpus
    ans = {}
    p = None
    for i in range(n):
        print('i', i, 'p: ', p)
        if i == 0:
            p = random.choice(list(corpus))
            ans[p] = 1 / n
        else:
            trans = transition_model(corpus, p, damping_factor)
            print('trans: ', trans)
            print('corp', list(corp))
            weights = [trans[x] for x in trans]
            print('weights', weights)
            print(sum(weights))
            p = random.choices(list(corp), weights=weights)[0]
            print('p: ', p)
            if p in ans:
                ans[p] += 1 / n
            else:
                ans[p] = 1 / n
    print('answer', ans)
    
    return ans


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    ans = {}
    N = len(corpus)
    PR = 1/N
    old_ans = {}
    for p in corpus:
        ans[p] = PR
    gtg = False
    while gtg == False:
        helper = 1
        for p in corpus:
            sum = 0 
            for i in corpus:
                num_links = len(corpus[i])
                if num_links == 0:
                    corpus[i] = {x for x in corpus}
                    num_links = len(corpus[i])
                if p in corpus[i]:
                    sum += ans[i] / num_links
            PRp = ((1 - damping_factor) / N) + (damping_factor * sum)
            old_ans[p] = ans[p]
            ans[p] = PRp
            if abs(old_ans[p] - ans[p]) > 0.001:
                helper = 0
                
        if helper != 0:
            gtg = True
            print(ans)
    return ans


if __name__ == "__main__":
    main()
