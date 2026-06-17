import pytest
from unittest.mock import patch, MagicMock

# Add your tests here

def test_get_enrollment_stats():
    # Mock the database connection and query results
    with patch('openedx_mcp_server.database.get_connection') as mock_get_connection:
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [(100, '2023-01-01', '2023-01-31')]
        with patch('openedx_mcp_server.database.execute_query', return_value=mock_cursor):
            result = openedx_mcp_server.tools.get_enrollment_stats('course_x', '2023-01-01', '2023-01-31')
            assert result == {'enrollment_count': 100, 'start_date': '2023-01-01', 'end_date': '2023-01-31'}


def test_get_grade_distribution():
    # Mock the database connection and query results
    with patch('openedx_mcp_server.database.get_connection') as mock_get_connection:
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [(50, 50, 50)]
        with patch('openedx_mcp_server.database.execute_query', return_value=mock_cursor):
            result = openedx_mcp_server.tools.get_grade_distribution('course_x')
            assert result == {'A': 50, 'B': 50, 'C': 50}


def test_get_problem_stats():
    # Mock the database connection and query results
    with patch('openedx_mcp_server.database.get_connection') as mock_get_connection:
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [(10, 5, 2)]
        with patch('openedx_mcp_server.database.execute_query', return_value=mock_cursor):
            result = openedx_mcp_server.tools.get_problem_stats('problem_id')
            assert result == {'attempt_count': 10, 'success_count': 5, 'difficulty_ranking': 2}


def test_get_learner_progress():
    # Mock the database connection and query results
    with patch('openedx_mcp_server.database.get_connection') as mock_get_connection:
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [(100, 90)]
        with patch('openedx_mcp_server.database.execute_query', return_value=mock_cursor):
            result = openedx_mcp_server.tools.get_learner_progress('learner_id', 'course_x')
            assert result == {'completion_count': 100, 'score': 90}


def test_get_certificate_stats():
    # Mock the database connection and query results
    with patch('openedx_mcp_server.database.get_connection') as mock_get_connection:
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [(50, 25)]
        with patch('openedx_mcp_server.database.execute_query', return_value=mock_cursor):
            result = openedx_mcp_server.tools.get_certificate_stats('course_x')
            assert result == {'issued_count': 50, 'passing_count': 25}


def test_list_active_courses():
    # Mock the database connection and query results
    with patch('openedx_mcp_server.database.get_connection') as mock_get_connection:
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [('course_x', 100)]
        with patch('openedx_mcp_server.database.execute_query', return_value=mock_cursor):
            result = openedx_mcp_server.tools.list_active_courses('org')
            assert result == [{'course_id': 'course_x', 'enrollment_count': 100}]
