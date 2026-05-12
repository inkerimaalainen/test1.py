import requests
from PIL import Image
from io import BytesIO


life = input('Есть 3 стула: на правый сядешь - женатым будешь, на левый сядешь - богатым будешь, на средний сядешь - смерть найдёшь \nChoose your chair! \n')
user_choice = life.lower()
if user_choice == 'правый':
    print("""         
       \`-._           __
            `-..____,.'  `.
         :`.         /    \`.
         :  )       :      : 
          ;'        '   ;  |  :
          )..      .. .:.`.;  :
         /::...  .:::...   ` ;
         ; _ '    __        /:
         `:o>   /\o_>      ;:. `.
        `-`.__ ;   __..--- /:.   
        === \_/   ;=====_.':.     ;
         ,/'`--'...`--....        ;
              ;                    ;
            .'                      ;
          .'                        ;
        .'     ..     ,      .       ;
       :       ::..  /      ;::.     |
      /      `.;::.  |       ;:..    ;
     :         |:.   :       ;:.    ;
     :         ::     ;:..   |.    ;
      :       :;      :::....|     |
      /\     ,/ \      ;:::::;     ;
    .:. \:..|    :     ; '.--|     ;
   ::.  :''  `-.,,;     ;'   ;     ;
.-'. _.'\      / `;      \,__:      
`---'    `----'   ;      /    \,.,,,/
                   `----`              
 """)
    print('Это вы')

    url = 'https://cdn.ruwiki.ru/commonswiki/files/9/9b/CroppedStalin1943.jpg'
    response = requests.get(url)
    stalin = Image.open(BytesIO(response.content))
    stalin.show()

    print('А это Сталин \nИ вы женаты')

elif user_choice == 'левый':
    print('Поздравляю! Теперь вы богаты')

elif user_choice == 'средний':
    print('Поздравляю!')
    url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTShzS79L5E8TJ0mwni2GTS367wND1e5rdnLw&s'
    response = requests.get(url)
    death = Image.open(BytesIO(response.content))
    death.show()

else:
    print('Стул не выбран, вынужден выкинуть вас из программы по выбору стульев')