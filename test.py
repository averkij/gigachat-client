#%%

# from src import gigadoom as gd
import gigadoom as gd

# %%
CLIENT_SECRET = ""

acc_token, token_exp = gd.chat.get_access_token(CLIENT_SECRET)

# %%
gd.chat.get_models(acc_token)

# [{'id': 'GigaChat',
#   'object': 'model',
#   'owned_by': 'salutedevices',
#   'type': 'chat'},
#  {'id': 'GigaChat-Max',
#   'object': 'model',
#   'owned_by': 'salutedevices',
#   'type': 'chat'},
#  {'id': 'GigaChat-Plus',
#   'object': 'model',
#   'owned_by': 'salutedevices',
#   'type': 'chat'},
#  {'id': 'GigaChat-Pro',
#   'object': 'model',
#   'owned_by': 'salutedevices',
#   'type': 'chat'}]

# %%
system = "Ты отвечаешь в стиле Николая Гоголя, с юмором и глубоким смыслом."

query = "В чем смысл жизни?"
first_history = [{"content": system, "role": "system"}]

answer, history, usage = gd.chat.get_completion(query, acc_token, history=first_history, model="GigaChat-Max")

#Ах, батенька! Смысл жизни, говорят мудрецы, не в словах сокрыт, а в деяниях. Но что за подмостки — эти наши деяния? Разве не на волоске висят они от случая к случаю? Или вот другой пример: посмотрите же вокруг себя, сколько людей путается без цели и смысла по белу свету. А всё потому, что смысл этот столь гибкий и многогранный, что поймать его сразу просто невозможно. Ну, а если кого вдруг осенило понимание, это ли не повод задуматься о смирении перед этой простой истиной — жизнь есть вечное движение, а не стояние на месте в поисках ответа?

# %%
query = "А теперь расскажи про квантовую механику в общих чертах."
answer, history, usage = gd.chat.get_completion(query, acc_token, history=history)

answer, history

# %%
# Квантовая механика — это странная материя. Вот представьте себе шар. Это наше понимание мира, в котором всё очевидно и предсказуемо. Но представьте, что шар состоит из миллионов мелких шариков, каждый из которых живёт своей жизнью и способен в любой момент менять своё местоположение. Представьте теперь, как сложно будет просчитать траекторию каждого такого шарика и уложить их в единую картину. Вот такое состояние мира и описывает квантовая механика. Её законы показывают, как микроскопические частицы ведут себя, но до конца понять и предсказать их действия очень трудно, так как они могут существовать во множестве состояний одновременно и изменяют своё состояние при наблюдении или взаимодействии с окружающим миром.

#%%

import gigadoom as gd


SECRET_KEY = ""
acc_token, token_exp = gd.chat.get_access_token(SECRET_KEY)

#models
models = gd.chat.get_models(acc_token)

print(models)

#chat
system = "Ты отвечаешь в стиле Николая Гоголя, с юмором и глубоким смыслом."

query = "В чем смысл жизни?"
history = [{"content": system, "role": "system"}]

answer, history, usage = gd.chat.get_completion(query, acc_token, history=history, model="GigaChat-Max")

#use history
query = "А теперь расскажи про квантовую механику в общих чертах."
answer, history, usage = gd.chat.get_completion(query, acc_token, history=history)

print(answer)
print(history)

