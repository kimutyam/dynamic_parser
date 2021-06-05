from dynamic_parser.tools.collection_ops import head_option


def test_head_option():
    assert head_option({1, 2, 3}) == 1
    assert head_option(frozenset({1, 2, 3})) == 1
    assert head_option([1, 2, 3]) == 1

