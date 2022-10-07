# Python

###  
https://www.udemy.com/course/python-3-do-zero-ao-avancado/learn/lecture/15099364#overview

### Conventions
https://peps.python.org/pep-0008/#package-and-module-names

https://google.github.io/styleguide/pyguide.html#3164-guidelines-derived-from-guidos-recommendations

```text
Type	    Public            	            Internal
Packages	lower_with_under	
Modules 	lower_with_under            	_lower_with_under
Classes	    CapWords	                    _CapWords
Exceptions	CapWords	
Functions	lower_with_under()	            _lower_with_under()
Global/Class Constants CAPS_WITH_UNDER  	_CAPS_WITH_UNDER
Global/Class Variables	lower_with_under	_lower_with_under
Instance Variables	lower_with_under	    _lower_with_under (protected)
Method Names	lower_with_under()	        _lower_with_under() (protected)
Function/Method Parameters              	lower_with_under	
Local Variables	lower_with_under	
```

### Estrutura de diretórios 

```markdown
/project_folder
  /name
     project_name.py
     cli.py
  /tests
     __init__.py
     __pycache__
     test_name.py
  /docs
     index.md
 LICENSE
 mkdocs.yml
 poetry.lock
 pyproject.toml
```


### Formatadores de código
https://pep8.org

* blue
* dark
* isort
* autopep8
* YAPF
* darker*

#### install blue
```shell
$ poetry add --dev blue
$ blue seu_arquivo.py
$ git diff # to visualize
$ blue . # to apply to all files in your project.
$ poetry add --dev isort
$ isort . --c # -c to check
$ isort . # to apply
```


### Criadores de documentação

* mkdocs
* sphinx

```shell
$ poetry add --dev mkdocs
$ mkdocs new .
$ mkdcos serve
```


### Análise estática

* Erros de sintaxe
* Potenciais problemas
  * Nomes duplicados
  * Nomes ruins
  * Códigos inseguros
* Análise de complexidade de código
* Violações de convenções 
  * PEP-8
  * PEP-257

#### Ferramentas
* flake
* pylint
* pydocstyle
* bandit
* Radon
* Prospector
* mypy

```shell
$ poetry add --dev prospector
$ prospector # at projetct folder

```

#### GNU Make

Automatizar comandos

```shell
# install make
$ blue isort
# example
# Makefile
.PHONY: install formt lint test sec

install:
        @poetry install # @ oculta execuçao do comando.
format:
        @blue .
        @isort .
lint:
        @blue --check .
        @isort --check .
        @propector --with-tool pep257 --doc-warning
test:
        @pytest -v
sec:
        @pip-audit
   
# executando os comandos
$ make install
$ make format
$ make lint
$ make test  
```

```shell
$ nano .git/hooks/pre-commit
$ make lint 
$ chmod +x .git/hooks/pre-commit
$ git add . && git commit 'Test'
# error

```

