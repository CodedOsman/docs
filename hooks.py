"""
MkDocs hook: back_navigation
Automatically injects a "← Back to Manual X.0" button at the top of every
individual lesson page (pages that live two folders deep inside a version dir).

Path pattern matched:  {version_dir}/{module_dir}/{lesson}.md
Example:               1.0/1.1.LED/1.1.1.LED_ON.md  →  ../../version1/
"""

VERSION_MAP = {
    "1.0": ("Manual 1.0", "../../version1/"),
    "2.0": ("Manual 2.0", "../../version2/"),
    "3.0": ("Manual 3.0", "../../version3/"),
}


def on_page_content(html, page, config, files, **kwargs):
    """
    Called after each page's Markdown is converted to HTML.
    Prepends a back-navigation bar for lesson pages only.
    """
    # Normalise path separators
    src_path = page.file.src_path.replace("\\", "/")
    parts = src_path.split("/")

    # Lesson pages are exactly 3 levels deep: version / module / lesson.md
    if len(parts) != 3:
        return html

    version_dir = parts[0]
    if version_dir not in VERSION_MAP:
        return html

    label, back_href = VERSION_MAP[version_dir]

    back_bar = (
        f'<div class="back-nav-bar">'
        f'<a href="{back_href}" class="back-nav-btn">'
        f'<span class="back-nav-arrow">&#8592;</span>'
        f'Back to {label}'
        f'</a>'
        f'</div>\n'
    )

    return back_bar + html
