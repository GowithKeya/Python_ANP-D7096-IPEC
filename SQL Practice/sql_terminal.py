import sqlite3
import os
import sys

def format_table(headers, rows):
    if not rows:
        return "No rows returned."
        
    # Convert all elements to strings
    str_rows = [[str(val) for val in row] for row in rows]
    
    # Calculate column widths
    col_widths = [len(h) for h in headers]
    for row in str_rows:
        for i, val in enumerate(row):
            col_widths[i] = max(col_widths[i], len(val))
            
    # Create divider line
    divider = "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"
    
    # Format header
    header_line = "|" + "|".join(f" {headers[i].ljust(col_widths[i])} " for i in range(len(headers))) + "|"
    
    # Format rows
    formatted_rows = []
    for row in str_rows:
        r_line = "|" + "|".join(f" {row[i].ljust(col_widths[i])} " for i in range(len(row))) + "|"
        formatted_rows.append(r_line)
        
    # Combine table parts
    table_lines = [divider, header_line, divider] + formatted_rows + [divider]
    return "\n".join(table_lines)

def run_terminal():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_file = os.path.join(script_dir, "college_db.db")
    
    # Automatically initialize DB if not present
    if not os.path.exists(db_file):
        print("Database file not found. Running setup_db.py to initialize...")
        try:
            import setup_db
            setup_db.setup_database()
        except Exception as e:
            print(f"Failed to auto-initialize database: {e}")
            return
            
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    print("=" * 60)
    print(" SQLite Interactive Terminal (college_db) ")
    print(" Type your SQL queries below.")
    print(" - End queries with a semicolon ';'")
    print(" - Type 'exit' or 'quit' to close terminal.")
    print(" - Type 'help' for special commands.")
    print("=" * 60)
    
    query_buffer = []
    
    while True:
        try:
            prompt = "... " if query_buffer else "sqlite> "
            line = input(prompt).strip()
            
            if not line:
                continue
                
            # Exit conditions
            if line.lower() in ("exit", "quit", "exit;", "quit;"):
                print("Exiting SQL terminal. Goodbye!")
                break
                
            # Special command: help
            if line.lower() in ("help", "help;"):
                print("\nSpecial commands:")
                print("  .tables - List all tables in the database")
                print("  .schema <table> - Show CREATE statement for a table")
                print("  exit/quit - Close terminal\n")
                continue
                
            # Special command: .tables
            if line.lower() == ".tables":
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
                tables = cursor.fetchall()
                print("\nTables:\n" + ", ".join(t[0] for t in tables) + "\n")
                continue
                
            # Special command: .schema
            if line.lower().startswith(".schema"):
                parts = line.split()
                if len(parts) > 1:
                    target_table = parts[1].replace(";", "")
                    cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name=?;", (target_table,))
                    schema = cursor.fetchone()
                    if schema:
                        print(f"\n{schema[0]}\n")
                    else:
                        print(f"\nTable '{target_table}' not found.\n")
                else:
                    cursor.execute("SELECT name, sql FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
                    for t_name, t_sql in cursor.fetchall():
                        print(f"\n-- Table: {t_name}\n{t_sql}\n")
                continue
            
            # Add line to buffer
            query_buffer.append(line)
            
            # If the last character is a semicolon, execute the query
            if line.endswith(";"):
                query = " ".join(query_buffer)
                query_buffer = [] # Reset buffer
                
                try:
                    cursor.execute(query)
                    
                    # Check if it was a SELECT query
                    if cursor.description:
                        headers = [desc[0] for desc in cursor.description]
                        rows = cursor.fetchall()
                        print("\n" + format_table(headers, rows) + "\n")
                    else:
                        conn.commit()
                        print(f"\nQuery OK, {cursor.rowcount} rows affected\n")
                        
                except sqlite3.Error as e:
                    print(f"\nSQL Error: {e}\n")
                    
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\nUse 'exit' to quit.")
            query_buffer = []
        except Exception as e:
            print(f"\nUnexpected error: {e}\n")
            query_buffer = []

    conn.close()

if __name__ == "__main__":
    run_terminal()
