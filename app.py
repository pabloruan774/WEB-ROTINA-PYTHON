from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('sistema_rotina.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    ultimo_peso = conn.execute('SELECT * FROM progresso_peso ORDER BY id DESC LIMIT 1').fetchone()
    # Puxa as últimas 10 atividades do Eren
    atividades_eren = conn.execute('SELECT * FROM cuidados_eren ORDER BY id DESC LIMIT 10').fetchall()
    conn.close()
    
    meta = 57.0 # Sua meta de ectomorfo
    peso_atual = ultimo_peso['peso'] if ultimo_peso else 0
    falta = meta - peso_atual if peso_atual > 0 else meta
    
    return render_template('index.html', peso=ultimo_peso, falta=falta, eren=atividades_eren)

@app.route('/registrar_peso', methods=['POST'])
def registrar_peso():
    peso = request.form['peso']
    data = datetime.now().strftime("%d/%m %H:%M")
    conn = get_db_connection()
    conn.execute('INSERT INTO progresso_peso (data, peso) VALUES (?, ?)', (data, peso))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/acao_eren', methods=['POST'])
def acao_eren():
    acao = request.form['acao']
    data = datetime.now().strftime("%d/%m %H:%M")
    conn = get_db_connection()
    conn.execute('INSERT INTO cuidados_eren (data, atividade) VALUES (?, ?)', (data, acao))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)