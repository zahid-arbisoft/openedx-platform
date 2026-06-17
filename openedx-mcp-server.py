# openedx-mcp-server.py

import mcp
from mysql_connection import get_mysql_connection

def create_mcp_server():
    server = mcp.Server()
    server.add_tool(get_enrollment_stats)
    server.add_tool(get_active_learners)
    server.add_tool(get_grade_distribution)
    server.add_tool(get_problem_stats)
    server.add_tool(get_learner_progress)
    server.add_tool(get_certificate_stats)
    server.add_tool(list_active_courses)
    return server

if __name__ == "__main__":
    server = create_mcp_server()
    server.run()