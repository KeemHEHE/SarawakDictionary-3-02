make_admin.py 

"""
CLI script to make a user an admin in the Sarawak Dictionary app
Usage: python make_admin.py <username>
"""
import sqlite3
import sys

def make_user_admin(username):
    """Make a user an admin by username"""
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        # Check if user exists
        cursor.execute('SELECT id, username, admin FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        
        if not user:
            print(f"❌ Error: User '{username}' tidak dijumpai!")
            return False
        
        user_id, current_username, is_admin = user
        
        if is_admin == 1:
            print(f"ℹ️  User '{username}' sudah menjadi pentadbir!")
            return True
        
        # Make user admin
        cursor.execute('UPDATE users SET admin = 1 WHERE id = ?', (user_id,))
        conn.commit()
        
        print(f"✅ Berjaya! User '{username}' kini telah menjadi pentadbir.")
        return True
        
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
        return False
    finally:
        if conn:
            conn.close()

def list_all_users():
    """List all users and their admin status"""
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT id, username, admin FROM users ORDER BY username')
        users = cursor.fetchall()
        
        if not users:
            print("❌ Tiada pengguna dijumpai!")
            return
        
        print("\n📋 Senarai semua pengguna:")
        print("-" * 50)
        print(f"{'ID':<5} {'Username':<20} {'Status':<15}")
        print("-" * 50)
        
        for user_id, username, is_admin in users:
            status = "PENTADBIR" if is_admin == 1 else "PENGGUNA"
            print(f"{user_id:<5} {username:<20} {status:<15}")
        
        print("-" * 50)
        
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
    finally:
        if conn:
            conn.close()

def create_admin_user(username, password):
    """Create a new admin user"""
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        # Create users table if it doesn't exist
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            admin INTEGER DEFAULT 0
        )
        ''')
        
        # Check if username already exists
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            print(f"❌ Error: Username '{username}' sudah wujud!")
            return False
        
        # Insert new admin user
        cursor.execute('INSERT INTO users (username, password, admin) VALUES (?, ?, 1)', 
                      (username, password))
        conn.commit()
        
        print(f"✅ Berjaya! Pentadbir baru '{username}' telah dicipta.")
        return True
        
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
        return False
    finally:
        if conn:
            conn.close()

def main():
    if len(sys.argv) < 2:
        print("🔐 Sarawak Dictionary - Admin Management Tool")
        print("\nUsage:")
        print("  python make_admin.py list                    - Senarai semua pengguna")
        print("  python make_admin.py make <username>         - Jadikan pengguna sebagai pentadbir")
        print("  python make_admin.py create <username> <password> - Cipta pentadbir baru")
        print("\nContoh:")
        print("  python make_admin.py list")
        print("  python make_admin.py make john")
        print("  python make_admin.py create admin123 password123")
        return
    
    command = sys.argv[1].lower()
    
    if command == "list":
        list_all_users()
    elif command == "make":
        if len(sys.argv) < 3:
            print("❌ Error: Sila masukkan username!")
            print("Usage: python make_admin.py make <username>")
            return
        username = sys.argv[2]
        make_user_admin(username)
    elif command == "create":
        if len(sys.argv) < 4:
            print("❌ Error: Sila masukkan username dan password!")
            print("Usage: python make_admin.py create <username> <password>")
            return
        username = sys.argv[2]
        password = sys.argv[3]
        create_admin_user(username, password)
    else:
        print(f"❌ Error: Command '{command}' tidak dikenali!")
        print("Gunakan 'list', 'make', atau 'create'")

if __name__ == "__main__":
    main()