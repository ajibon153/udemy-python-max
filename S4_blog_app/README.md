

# Template File
1. Add templates folder on main app, for global / base skeleton html file
2. Add templates on local app for specifict page, and call the base skeleton html in it
3. Don't forget to add BASE_DIR / 'templates' in setting.py on TEMPLATES = []
4. For automatic template detection. on INSTALLED_APPS, add 'blog' on array

# Styling template
1. Create folder static in global app and blog app
2. on static main app
- add app.css for general styling (app.css)
- call the css file inside base.html in link static href
- Go to setting.py in main, and then add base_dir static bellow STATIC_URL = 'static/' :
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

3. on static blog app
- add index.css for local styling (blog/index.css)
- call the css file on template/blog/index.html inside {% block css_file %}
don't forget to call {% load static %}

# INCLUDE template file on local app