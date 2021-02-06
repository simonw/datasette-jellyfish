from datasette_jellyfish import prepare_connection
import sqlite3
import pytest


@pytest.mark.parametrize(
    "sql,expected",
    (
        ('soundex("hello")', "H400"),
        ('metaphone("hello")', "HL"),
        ('nysiis("hello")', "HAL"),
        ('match_rating_codex("hello")', "HL"),
        ('porter_stem("running")', "run"),
        ('levenshtein_distance("hello", "hello world")', 6),
        ('damerau_levenshtein_distance("hello", "hello world")', 6),
        ('hamming_distance("hello", "hello world")', 6),
        ('jaro_similarity("hello", "hello world")', pytest.approx(0.8181818181818182)),
        ('jaro_winkler_similarity("hello", "hello world")', pytest.approx(0.890909090909091)),
        ('match_rating_comparison("hello", "helloo")', 1),
    ),
)
def test_jellyfish(sql, expected):
    conn = sqlite3.connect(":memory:")
    prepare_connection(conn)
    result = conn.execute("select " + sql).fetchone()[0]
    assert expected == result
