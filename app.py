@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            username = request.form.get('username')
            password = request.form.get('password')

            if not username or not password:
                return "Fill all fields ❌"

            conn = sqlite3.connect('/tmp/users.db')
            c = conn.cursor()

            c.execute("INSERT INTO users VALUES (?, ?, ?, ?)", (username, password, 1000, ""))
            conn.commit()
            conn.close()

            return redirect('/login')

        except Exception as e:
            return f"Signup Error: {str(e)} ❌"

    return render_template('signup.html')
