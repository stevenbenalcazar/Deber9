import os
import openai
openai.organization = 'org-bVEtCGEt2uFvJdT0vU38IFNZ'
openai.api_key = os.getenv("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")
class Document(BaseModel):
  prompt: str = ''
def inference(prompt: str) -> str:
  print('[PROSESANDO]'.center(40, '-'))
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": """Eres un profesor de programacion univercitario, genera un codigo cuenta numeros"
                                  E.G: programacion
     -es como armar un crusigrama"""},
    {"role": "user", "content": prompt}
  ]
)
content = completion.choices[0].message.content
total_tokens = completion.usage.total_tokens

print('[SE TERMINO DE PROCESAR]'.center(40, '-'))
return [content, total_tokens]
