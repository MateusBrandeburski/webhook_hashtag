from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from classes.database.database import Pagamentos


tratativas = Blueprint('tratativas', __name__, template_folder='template')


# redenderiza tabela que mostra os dados no banco de dados.
@tratativas.route('/tratativas')
def index():
    
    # verifica se o usuário está logado.
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login.index'))
      
    else:     
        # Número de itens por página
        itens_por_pagina = 10

        # Obtém o número da página atual a partir da query string, padrão é 1
        pagina = int(request.args.get('pagina', 1))

        # Obtém todos os registros do banco de dados
        pagamentos = Pagamentos.query.all()

        # Calcula o número total de páginas
        total_paginas = len(pagamentos) // itens_por_pagina + (len(pagamentos) % itens_por_pagina > 0)
        
        # Verifica se a página atual está além do total de páginas
        if pagina > total_paginas:
            # Redireciona para a última página com dados preenchidos
            return redirect(url_for('.index', pagina=total_paginas))

        # Calcula o índice inicial e final dos itens a serem exibidos
        indice_inicial = (pagina - 1) * itens_por_pagina
        indice_final = indice_inicial + itens_por_pagina

        # Obtém os itens da página atual
        itens_pagina = pagamentos[indice_inicial:indice_final]

        return render_template('home/info_pagamentos/info_pagamentos.html', pagamentos=itens_pagina, total_paginas=total_paginas, pagina_atual=pagina)
    

@tratativas.route('/filtro-por-email', methods=['GET','POST'])
def status_completo():
    
    # verifica se o usuário está logado.
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login.index'))
      
    else:   
        email_filtrado = request.form.get('email')
        filtros = Pagamentos.query.filter_by(email=email_filtrado).all()
        if filtros:
            return render_template('home/info_pagamentos/info_pagamentos.html', filtros=filtros)
        else:
            flash('Email não encontrado na base de dados!')
            return render_template('home/info_pagamentos/info_pagamentos.html', filtros=filtros)

