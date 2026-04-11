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
