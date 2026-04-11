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
    @app.route('/leaderboard')
    @app.route('/recharge')
def recharge():
    return "Pay and get coins (Coming Soon 💰)"
def leaderboard():
    conn = sqlite3.connect('/tmp/users.db')
    c = conn.cursor()

    c.execute("SELECT username, coins FROM users ORDER BY coins DESC LIMIT 10")
    users = c.fetchall()

    conn.close()

    return render_template('leaderboard.html', users=users)
    @app.route('/recharge', methods=['GET', 'POST'])
def recharge():
    if 'username' not in session:
        return redirect('/login')

    if request.method == 'POST':
        amount = request.form.get('amount')
        utr = request.form.get('utr')

        # simple message (later DB store చేస్తాం)
        return f"Recharge request submitted ₹{amount} ✅ (UTR: {utr})"

    return render_template('recharge.html')
