from datasette import hookimpl
import jellyfish

one_args = (
    # Phonetic
    # https://jellyfish.readthedocs.io/en/latest/phonetic.html
    "soundex",
    "metaphone",
    "nysiis",
    "match_rating_codex",
    # Stemming
    # https://jellyfish.readthedocs.io/en/latest/stemming.html
    # REMOVED: https://github.com/jamesturk/jellyfish/blob/d5ae6d4d2af5771bfd0b572456d42e48f8690b89/docs/changelog.md
    # OR PIN jellyfish==0.9.0
    #"porter_stem",
)
two_args = (
    # String Comparison
    # https://jellyfish.readthedocs.io/en/latest/comparison.html
    "levenshtein_distance",
    "damerau_levenshtein_distance",
    "hamming_distance",
    "jaro_similarity",
    "jaro_winkler_similarity",
    "match_rating_comparison",
)


@hookimpl
def prepare_connection(conn):
    for fn in one_args:
        conn.create_function(fn, 1, getattr(jellyfish, fn))
    for fn in two_args:
        conn.create_function(fn, 2, getattr(jellyfish, fn))
