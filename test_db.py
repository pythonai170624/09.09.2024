import sqlite_lib

def test_get_years():
    # Arrange
    sqlite_lib.connect('hw.db')

    # Act
    result = sqlite_lib.run_query_select('''
        SELECT YEAR FROM eurovision_winners ew
        LIMIT 1
    ''')

    # Assert
    assert result == [(1956,)]

