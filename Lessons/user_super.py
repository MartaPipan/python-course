# =====================================================================
# 1. БАТЬКІВСЬКИЙ КЛАС (Користувач системи)
# =====================================================================
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.is_logged_in = False

    def login(self):
        self.is_logged_in = True
        return f"👤 Користувач {self.username} увійшов у систему."


# =====================================================================
# 2. ДОЧІРНІЙ КЛАС (Адміністратор / Модератор з правами доступу)
# =====================================================================
class Admin(User):
    def __init__(self, username, email, permissions=None):
        super().__init__(username, email)
        
        # Запасний план: якщо права не передані, створюємо порожній список
        if permissions is None:
            permissions = []
            
        self.permissions = permissions

    # ФУНКЦІЯ 1: Блокування (вимагає право "ban")
    def ban_user(self, bad_user):
        if "ban" in self.permissions:
            return f"🔨 Адміністратор {self.username} ЗАБЛОКУВАВ користувача {bad_user}!"
        return f"❌ Помилка! У {self.username} немає прав для БЛОКУВАННЯ."

    # ФУНКЦІЯ 2: Видалення постів (вимагає право "delete_post")
    def delete_post(self, post_id):
        if "delete_post" in self.permissions:
            return f"🗑️ {self.username} ВИДАЛИВ пост №{post_id}."
        return f"❌ Помилка! У {self.username} немає прав для ВИДАЛЕННЯ ПОСТІВ."


# =====================================================================
# 🎮 СТВОРЕННЯ ОБ'ЄКТІВ ТА ТЕСТУВАННЯ ТРЬОХ РОЛЕЙ
# =====================================================================
if __name__ == "__main__":
    
    print("--- 👑 РОЛЬ 1: Головний Адмін (Повні права) ---")
    # Передаємо і "ban", і "delete_post"
    boss = Admin("alex_admin", "alex@site.com", ["ban", "delete_post"])
    print(boss.ban_user("spammer"))    # Успішно (є "ban")
    print(boss.delete_post(105))       # Успішно (є "delete_post")

    print("\n--- 📝 РОЛЬ 2: Модератор (Тільки видалення постів) ---")
    # Передаємо ТІЛЬКИ "delete_post". Значення None ігнорується.
    moderator = Admin("olena_mod", "olena@site.com", ["delete_post"])
    print(moderator.ban_user("spammer")) # ❌ Відмова! Бо слова "ban" немає в її списку
    print(moderator.delete_post(106))    # ✅ Успішно! Бо "delete_post" є в списку

    print("\n--- ❔ РОЛЬ 3: Помічник (Взагалі без прав) ---")
    # Третій аргумент НЕ передаємо. Спрацьовує автоматичний план permissions=None!
    helper = Admin("vanya_helper", "vanya@site.com")
    print(helper.ban_user("spammer"))    # ❌ Відмова! Список порожній []
    print(helper.delete_post(107))       # ❌ Відмова! Список порожній []
