from django import forms


#検索用バリデーションはモデルを継承せずにフォームを作る
class SearchForm(forms.Form):
    search_word = forms.CharField(widget=forms.TextInput(attrs={"class":"input_search"}))

