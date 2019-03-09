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
    "porter_stem",
)
two_args = (
    # String Comparison
    # https://jellyfish.readthedocs.io/en/latest/comparison.html
    "levenshtein_distance",
    "damerau_levenshtein_distance",
    "hamming_distance",
    "jaro_distance",
    "jaro_winkler",
    "match_rating_comparison",
)


@hookimpl
def prepare_connection(conn):
    for fn in one_args:
        conn.create_function(fn, 1, getattr(jellyfish, fn))
    for fn in two_args:
        conn.create_function(fn, 2, getattr(jellyfish, fn))
