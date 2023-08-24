from datasette import hookimpl
import jellyfish

one_args = (
    # Phonetic
    # https://jamesturk.github.io/jellyfish/functions/#phonetic-encoding
    "soundex",
    "metaphone",
    "nysiis",
    "match_rating_codex",
)
two_args = (
    # String Comparison
    # https://jamesturk.github.io/jellyfish/functions/#string-comparison
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
