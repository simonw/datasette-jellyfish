# datasette-jellyfish

[![PyPI](https://img.shields.io/pypi/v/datasette-jellyfish.svg)](https://pypi.org/project/datasette-jellyfish/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/datasette-jellyfish/blob/master/LICENSE)

Datasette plugin that adds custom SQL functions for fuzzy string matching, built on top of the [Jellyfish](https://github.com/jamesturk/jellyfish) Python library by James Turk and Michael Stephens.

Try out [the live demo](https://datasette-jellyfish.now.sh/fixtures-21da8a4?sql=SELECT%0D%0A++++soundex%28%22hello%22%29%2C+%0D%0A++++metaphone%28%22hello%22%29%2C+%0D%0A++++nysiis%28%22hello%22%29%2C+%0D%0A++++match_rating_codex%28%22hello%22%29%2C+%0D%0A++++porter_stem%28%22running%22%29%2C+%0D%0A++++levenshtein_distance%28%22hello%22%2C+%22hello+world%22%29%2C+%0D%0A++++damerau_levenshtein_distance%28%22hello%22%2C+%22hello+world%22%29%2C+%0D%0A++++hamming_distance%28%22hello%22%2C+%22hello+world%22%29%2C+%0D%0A++++jaro_distance%28%22hello%22%2C+%22hello+world%22%29%2C+%0D%0A++++jaro_winkler%28%22hello%22%2C+%22hello+world%22%29%2C+%0D%0A++++match_rating_comparison%28%22hello%22%2C+%22helloo%22%29%3B).

Examples:

    SELECT soundex("hello");
        -- Outputs H400
    SELECT metaphone("hello");
        -- Outputs HL
    SELECT nysiis("hello");
        -- Outputs HAL
    SELECT match_rating_codex("hello");
        -- Outputs HLL
    SELECT porter_stem("running");
        -- Outputs run
    SELECT levenshtein_distance("hello", "hello world");
        -- Outputs 6
    SELECT damerau_levenshtein_distance("hello", "hello world");
        -- Outputs 6
    SELECT hamming_distance("hello", "hello world");
        -- Outputs 6
    SELECT jaro_distance("hello", "hello world");
        -- Outputs 0.8181818181818182
    SELECT jaro_winkler("hello", "hello world");
        -- Outputs 0.890909090909091
    SELECT match_rating_comparison("hello", "helloo");
        -- Outputs 1

See [the Jellyfish documentation](https://jellyfish.readthedocs.io/en/latest/) for an explanation of each of these functions.