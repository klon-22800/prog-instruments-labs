import pytest
import pandas as pd

from unittest.mock import patch

from main import text_update, add_word_count, stats_by_word_count, sort_by_word_count, sort_by_num, preprocess_text, preprocess_text_only_A, group_by_num, graph_build


@pytest.mark.parametrize("input_text, expected_result", [
    ("Обычный текст без всего", ['Обычный', 'текст', 'без', 'всего']),
    ("Текст, со знаками -- - - препинания!!",
     ['Текст', 'со', 'знаками', 'препинания']),
    ("", [])
])
def test_text_update(input_text, expected_result):
    result = text_update(input_text)
    assert result == expected_result


def test_add_word_count():
    data = {'num': ['1', '2'], 'text': ['Раз два', 'Раз два три']}
    df = pd.DataFrame(data)
    add_word_count(df)
    assert df['word_count'].iloc[0] == 2
    assert df['word_count'].iloc[1] == 3


def test_stats_by_word_count():
    data = {'num': ['1', '1', '2'], 'text': ['Раз два', 'Раз два три', 'Три']}
    df = pd.DataFrame(data)
    add_word_count(df)
    result = stats_by_word_count(df)
    assert result.loc['1', 'word_count'] == 2.5
    assert result.loc['2', 'word_count'] == 1


@pytest.mark.parametrize("max_count, expected_length", [
    (2, 2),
    (3, 3)
])
def test_sort_by_word_count(max_count, expected_length):
    data = {'num': ['1', '1', '2'], 'text': ['Раз два', 'Раз два три', 'Раз']}
    df = pd.DataFrame(data)
    add_word_count(df)
    result = sort_by_word_count(df, max_count)
    assert len(result) == expected_length


def test_sort_by_num():
    data = {'num': ['1', '1', '2'], 'text': ['Раз два', 'Раз два три', 'Раз']}
    df = pd.DataFrame(data)
    result = sort_by_num(df, '1')
    assert len(result) == 2


@pytest.mark.parametrize("text, expected_result", [
    ("красивая бегаю поле", ["красивый", "бегать", "поле"]),
    ("", []),
    ("not russian text", ["not", "russian",  "text"])
])
def test_preprocess_text(text, expected_result):
    result = preprocess_text(text)
    assert result == expected_result


@pytest.mark.parametrize("text, expected_result", [
    ("красивая бегаю поле", ["красивый"]),
    ("", []),
    ("not russian text", [])
])
def test_preprocess_text_only_A(text, expected_result):
    result = preprocess_text_only_A(text)
    assert result == expected_result


def test_group_by_num():
    data = {'num': ['1', '1', '2'], 'text': ['Раз два', 'Раз два три', 'Раз']}
    df = pd.DataFrame(data)
    add_word_count(df)
    result = group_by_num(df)
    assert result.loc[result['num'] == '1', 'mean'].iloc[0] == 2.5


@patch('matplotlib.pyplot.show')
def test_graph_build(mock_show):
    hist_list = [('Раз', 5), ('Два', 3), ('Три', 2)]
    graph_build(hist_list)
    mock_show.assert_called_once()
