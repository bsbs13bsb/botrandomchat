import sqlite3
import threading

coon = sqlite3.connect('db.sqlite3', check_same_thread=False)
cursor = coon.cursor()
lock = threading.Lock()

# يتم وضع اسماء الجداول مع الاعمدة الخاصة بها في هذا القاموس
tablesName = {
        'users':['id', 'username', "last_msg", "reports", "users_reports"],
            'message': ['msg', 'val'],
                'waiting': ['id'],
                    "chat_sessions": ["sessions", 'user_id', 'end_time'],
                        "sessions_messages":["session", "user_id", "msg_id", "msg_id_in_partner"],
            }