@app.route('/recharge', methods=['GET', 'POST'])
def recharge():
    if 'username' not in session:
        return redirect('/login')

    if request.method == 'POST':
        username = session['username']
        amount = request.form.get('amount')
        utr = request.form.get('utr')

        conn = sqlite3.connect('/tmp/users.db')
        c = conn.cursor()

        c.execute("INSERT INTO recharge (username, amount, utr) VALUES (?, ?, ?)",
                  (username, amount, utr))
        conn.commit()
        conn.close()

        return "Recharge request submitted ✅"

    return render_template('recharge.html')
@app.route('/approve_recharge/<int:id>')
def approve_recharge(id):
    if 'admin' not in session:
        return redirect('/admin')

    conn = sqlite3.connect('/tmp/users.db')
    c = conn.cursor()

    # get recharge request
    c.execute("SELECT username, amount FROM recharge WHERE id=?", (id,))
    data = c.fetchone()

    if data:
        username = data[0]
        amount = int(data[1])

        # add coins
        c.execute("UPDATE users SET coins = coins + ? WHERE username=?", (amount, username))

        # delete request
        c.execute("DELETE FROM recharge WHERE id=?", (id,))

        conn.commit()

    conn.close()

    return redirect('/admin/dashboard')
