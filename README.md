# PCS2044 - Engenharia de Software II

Repositorio para controlar a versao dos documentos da materia de PCS2044

Aqueles que estao desenvolvendo a versao Mobile favor fazer commits sobre a pasta Mobile!

O mesmo vale para aqueles que estao desenvolvendo a versao Web!

1. WEB - Cuidado com Python, as vezes voces vao rodar um comando e ele pode reclamar de identacao, a identacao em Python eh o TAB

2. WEB - Meu banco de dados nao funciona ou meus models nao foram criados em tabelas - Provavelmente vc nao criou nada, rode: 
	
	```bash
	python manage.py syncdb
	```

3. WEB - Como eu rodo o servidor?

	```bash
	python manage.py runserver
	```

4. WEB - Como eu gero as migracoes necessarias do meu model/app ?
	
	```bash
	python manage.py sql SEU-APP-AQUI
	```

5. WEB - Como eu jogo fora meu banco e reconstruo ?

	```bash
	python manage.py reset SEU-APP-AQUI
	```