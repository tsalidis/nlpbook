# ngram_model.py
from collections import Counter, defaultdict
import math
import re
import random

def tokenize(text: str):
    # Απλή, unicode-friendly τοκενoποίηση: λέξεις, αριθμοί, και σημεία στίξης χωριστά
    # Για απλότητα κρατάμε μόνο λέξεις/αριθμούς. Προσαρμόστε αν θέλετε στίξη.
    return re.findall(r"\w+", text.lower(), flags=re.UNICODE)

def with_sentence_boundaries(tokens, n):
    # Προσθέτουμε (n-1) <s> στην αρχή και ένα </s> στο τέλος
    pad = ["<s>"] * (n - 1)
    return pad + tokens + ["</s>"]

def ngrams_from_tokens(tokens, n):
    return [tuple(tokens[i:i+n]) for i in range(len(tokens) - n + 1)]

def count_ngrams(corpus_texts, n):
    """Επιστρέφει: counts_n (n-grams) και counts_ctx ((n-1)-grams)."""
    counts_n = Counter()
    counts_ctx = Counter()
    for text in corpus_texts:
        toks = tokenize(text)
        padded = with_sentence_boundaries(toks, n)
        ngrams = ngrams_from_tokens(padded, n)
        counts_n.update(ngrams)
        if n > 1:
            contexts = [ng[:-1] for ng in ngrams]
            counts_ctx.update(contexts)
    return counts_n, counts_ctx

def mle_prob(ngram, counts_n, counts_ctx):
    """P(w_n | w_1..w_{n-1}) με MLE."""
    if len(ngram) == 1:
        total = sum(counts_n.values())
        return counts_n[ngram] / total if total else 0.0
    ctx = ngram[:-1]
    ctx_count = counts_ctx[ctx]
    return (counts_n[ngram] / ctx_count) if ctx_count else 0.0

def laplace_prob(ngram, counts_n, counts_ctx, vocabulary_size):
    """Add-1 (Laplace) smoothing."""
    if len(ngram) == 1:
        total = sum(counts_n.values())
        return (counts_n[ngram] + 1) / (total + vocabulary_size)
    ctx = ngram[:-1]
    ctx_count = counts_ctx[ctx]
    return (counts_n[ngram] + 1) / (ctx_count + vocabulary_size)

def next_word_distribution(context, counts_n, counts_ctx, vocab, smoothing=None):
    """
    Δίνει κατανομή επόμενης λέξης για το δοθέν context (tuple μήκους n-1).
    smoothing: None | "laplace"
    """
    n = len(context) + 1
    probs = {}
    V = len(vocab)
    for w in vocab:
        ng = context + (w,)
        if smoothing == "laplace":
            p = laplace_prob(ng, counts_n, counts_ctx, V)
        else:
            p = mle_prob(ng, counts_n, counts_ctx)
        if p > 0:
            probs[w] = p
    # Κανονικοποίηση (για αριθμ. σταθερότητα – χρήσιμο με smoothing)
    s = sum(probs.values())
    if s > 0:
        for w in probs:
            probs[w] /= s
    return probs

def sample_from_distribution(dist):
    """Δειγματοληψία επόμενης λέξης από κατανομή {λέξη: p}."""
    r = random.random()
    cum = 0.0
    for w, p in dist.items():
        cum += p
        if r <= cum:
            return w
    # fallback (λόγω πιθανών στρογγυλοποιήσεων)
    return next(iter(dist)) if dist else None

def generate_sentence(counts_n, counts_ctx, vocab, n=3, max_len=30, smoothing="laplace"):
    """Γεννά πρόταση με n-gram μοντέλο, ξεκινώντας από <s>..."""
    context = tuple(["<s>"] * (n - 1))
    sentence = []
    for _ in range(max_len):
        dist = next_word_distribution(context, counts_n, counts_ctx, vocab, smoothing=smoothing)
        if not dist:  # δεν ξέρουμε να συνεχίσουμε
            break
        w = sample_from_distribution(dist)
        if w == "</s>":
            break
        sentence.append(w)
        # κύλιση context
        context = (context + (w,))[-(n-1):]
    return " ".join(sentence)

if __name__ == "__main__":
    # Μικρό ελληνικό corpus (γραμμές = έγγραφα)
    corpus = [
        "Η Ευρώπη έχει πολλές χώρες και μεγάλες πόλεις.",
        "Οι πόλεις της Ευρώπης έχουν ιστορία και πολιτισμό.",
        "Η ιστορία της πόλης φαίνεται στα μνημεία.",
        "Ο πολιτισμός αναπτύσσεται στις μεγάλες πόλεις."
    ]

    # --- 1) Μετρήσεις για bigrams και trigrams
    for n in (2, 3):
        counts_n, counts_ctx = count_ngrams(corpus, n)
        print(f"\nTop {n}-grams:")
        for ng, c in counts_n.most_common(10):
            print(ng, "→", c)

        # Λεξιλόγιο (εξαιρούμε τα boundary tokens από τη λίστα εμφάνισης)
        vocab = sorted({tok for text in corpus for tok in tokenize(text)} | {"</s>"} | {"<s>"} )

        # --- 2) Παράδειγμα: πιθανότητες επόμενης λέξης για συγκεκριμένο context
        if n == 2:
            ctx = ("ευρώπης",)  # bigram context
        else:
            ctx = ("η", "ευρώπη")  # trigram context
        dist = next_word_distribution(ctx, counts_n, counts_ctx, vocab, smoothing="laplace")
        print(f"\nP(· | {ctx}):")
        for w, p in sorted(dist.items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"{w:<12} {p:.3f}")

    # --- 3) Παραγωγή πρότασης με trigram μοντέλο
    counts3, ctx3 = count_ngrams(corpus, 3)
    vocab_all = sorted({tok for text in corpus for tok in tokenize(text)} | {"</s>"} | {"<s>"} )
    print("\nΔημιουργία πρότασης (trigram + Laplace):")
    for _ in range(3):
        print("•", generate_sentence(counts3, ctx3, vocab_all, n=3, max_len=15, smoothing="laplace"))
