from django.forms import ModelForm
from app.models import Livros

# Create the form class.
class LivrosForm(ModelForm):
   class Meta:
         model = Livros
         fields = ['cod_livro', 'ISBN', 'Titulo_livro', 'autor_livro','edicao_livro','ano_ancamento','cod_biblioteca','link_livro','status_livro']

