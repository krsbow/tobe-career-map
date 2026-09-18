"""
Views package for TO BE Platform.
"""

from views.landing import render_landing_page
from views.auth_view import render_auth_view
from views.home import render_home_page
from views.discover import render_discover_page
from views.explore import render_explore_page
from views.compare import render_compare_page
from views.my_path import render_my_path_page
from views.mentor import render_mentor_page
from views.profile import render_profile_page

__all__ = [
    "render_landing_page",
    "render_auth_view",
    "render_home_page",
    "render_discover_page",
    "render_explore_page",
    "render_compare_page",
    "render_my_path_page",
    "render_mentor_page",
    "render_profile_page"
]
