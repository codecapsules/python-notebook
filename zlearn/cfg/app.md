### CFG

## Adding a Template Folder on settings.py.
TEMPLATES = [
    {
        ....
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        ....
    },
]

