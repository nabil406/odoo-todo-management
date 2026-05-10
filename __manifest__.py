{
    "name": "ToDo Management",
    "author": "Nabil Atef",
    "version": "18.0.0.1.0",
    "depends": ["base", 'mail'
                ],
    "application": True,
    "data": [
        'security/ir.model.access.csv',
        'views/todo_view.xml',
        'views/base_menu.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'todo_management/static/src/css/todo.css',
        ],
    },

}
