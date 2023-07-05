import pygame
from modules.level_map import screen, screen_height, screen_width

class Text():
    def __init__(self, text, color, size):
        self.text = text
        self.color = color
        self.font = pygame.font.SysFont('comicsansms', size)
        self.hitbox = None
        self.counter = 0
        if type(text) == list:
            self.width = self.font.size(text[0])[0]
            self.height = self.font.size(text[0])[1]
        self.text_list = text
        self.loading_image = pygame.image.load('images/__game_picture__/download_background2.png')
        self.loading_image = pygame.transform.scale(self.loading_image, (screen_width, screen_height))

    def draw_text(self, counter, x, y):
        for text in self.text[counter]:
            self.hitbox = self.font.render(text, True, self.color)
            screen.blit(self.hitbox, ((screen_width-self.font.size(text)[0])/2, y))
            y += screen_height*0.042
    
    def draw_game_text(self, x, y):
        self.width = self.font.size(self.text_list[0])[0]
        self.height = self.font.size(self.text_list[0])[1]
        for text in self.text_list:
            self.hitbox = self.font.render(text, True, self.color)
            screen.blit(self.hitbox, (x, y))
            y += 35

    def draw_credits_text(self, y):
      for text in self.text_list:
          self.hitbox = self.font.render(text, True, self.color)
          screen.blit(self.hitbox, ((screen_width-self.font.size(text)[0])/2, y))
          y += screen_height*0.051

text = Text(
    {
      #------------------------------Dialog 1-------------------------------------

    

      1 : ["Головний Ельф:",
          "Дорогі ельф'ята. У мене для вас погані",
          "новини."],

      2 : ["Головний Ельф:",
            "Кхм... Кхм..."],

      3 : ["Головний Ельф:","Дід Мороз захворів. І нам треба",
          "йому допомогти, щоб провести Новий Рік!"],

      4 : ["Головний Ельф:",
          "І так. Олег, Катя та Микола. Ви йдете до",
          "Діда Мороза, він сам видасть вам завдання."],

      5 : ["Головний Ельф:",
          "А решта, за мною."],

      #------------------------------------------------------------------------
    },
    (200,200,200), int(screen_width*0.021))

text2 = Text(
    {
      #------------------------------Dialog 2-----------------------------
      1 : ['Микола:',
          'Діду Мороз, ви нас викликали?'],
      
      2 : ['Дід Мороз:',
          'Так, викликав, потрібна ваша допомога.'],

      3 : ['Катя:',
          'Чим вам допомогти?'],

      4 : ['Дід мороз:',
          'Я дам для кожного завдання і ви повинні',
          'його виконати.'],

      5 : ['Дід Мороз:',
          'Так.'],

      6 : ['Дід Мороз:',
          'Олег. Ти маєш забрати на складі всі',
          'подарунки, які там залишилися.'],

      7 : ['Дід Мороз:',
          'Їх 10.'],

      8 : ['Дід Мороз:',
          'Впораєшся?'],

      9 : ['Олег:',
          'Так, звичайно, все буде зроблено у',
          'найкращому вигляді.'],

      10 : ['Дід Мороз:',
            'Ну от і добре.'],

      11 : ['Дід Мороз:',
            'Тепер ти Катя.'],

      12 : ['Дід Мороз:',
            'Йди теж до складу. Збери все для чаю.',
            "Лист чаю, воду, варення, чайник, чашку",
            "та ягоди"],

      13 : ['Катя:',
            'Для якого чаю?'],

      14 : ['Дід Мороз:',
            'Хо-хо-хо. Це особливий чай, він послаблює',
            'хворобу та надає імунітету до цієї хвороби.'],

      15 : ['Катя:',
            'Ого, звучить чудово.'],

      16 : ['Дід Мороз:',
            'Так, і я тебе попрошу зробити цей чай.'],

      17 : ['Катя:',
            'А я впораюся?'],

      18 : ['Дід Мороз:',
            'Звичайно впораєшся, це як звичайний чай,',
            'тільки робиться у спеціальному чайнику.'],

      19 : ['Катя:',
            'Ага, зрозуміла, тоді зроблю!'],

      20 : ['Дід Мороз:',
            'Так. Тепер Микола.'],

      21 : ['Микола:',
            'Так, слухаю вас.'],

      22 : ['Дід Мороз:',
            'Мені якийсь Дмитро, який називає',
            'себе Сергієм.'],

      23 : ['Дід Мороз:',
            'Замовив одну річ.'],

      24 : ['Микола:',
            'І що ж?'],

      25 : ['Дід Мороз:',
            'Це торішній хліб...'],

      26 : ['Микола:',
            '???'],

      27 : ['Олег:',
            'Хахаха.'],

      28 : ['Катя:',
            'А я бачу він гуморист...'],
      
      29 : ['Дід Мороз:',
            'Так. Ну якщо вже замовив, то треба',
            'доставити.'],

      30 : ['Микола:',
            'Але як мені його дістати?'],

      31 : ['Дід Мороз:',
            'Ти маєш на санях прилетіти на землю.'],

      32 : ['Дід Мороз:',
            'Я тобі дам карту.'],

      33 : ['Дід Мороз:',
            'Потім непомітно тобі треба',
            'підібратися до одного місця.'],

      34 : ['Дід Мороз:',
            'Забереш хліб, та залишиш там',
            '50 новодоларів.'],

      35 : ['Дід Мороз:',
            'Я дам тобі гроші.'],

      36 : ['Дід Мороз:',
            'Ти мене зрозумів?'],

      37 : ['Микола:',
            'Так. Зрозумів.'],

      38 : ['Дід Мороз:',
            'Ну і коли свої справи зробите, повертайтесь',
            'назад до мене.'],

      39 : ['Дід Мороз:',
            'Вдачі вам.']
    }, 
    (200,200,200), int(screen_width*0.021))

text3 = Text(
    {
      #------------------------------Dialog 3-----------------------------
      1 : ['Дід Мороз:','Ну що ж.'],
      
      2 : ['Дід Мороз:','Дякую Каті за чай.',
        'Він був дуже смачним.'],

      3 : ['Дід Мороз:',
      'Та всім іншим.'],

      4 : ['Олег:','Завжди будь ласка.'],

      5 : ['Катя:','Ми завжди раді вам допомогти.'],

      6 : ['Дід Мороз:','Це добре.'],

      7 : ['Дід Мороз:','Микола. Як покатався на санях?'],

      8 : ['Микола:','Круто покатався. Я взагалі ',
        'найкращий водій саней.'],

      9 : ['Дід Мороз:','Хо-хо-хо. Я й не сумнівався.'],

      10 : ['Дід Мороз:','Ну що ж, ще раз',
        'дякую за допомогу.'],

      11 : ['Дід Мороз:','Але мені час йти.'],

      12 : ['Олег:','Куди?'],

      13 : ['Дід Мороз:','У мене ще одне ',
        'замовлення є особливе.'],

      14 : ['Катя:','Так ви ж хворієте.',
        'Вам краще залишатись тут.'],

      15 : ['Микола:','Давайте краще ми.'],

      16 : ['Дід Мороз:','Хо-хо-хо, мені вже краще, та я ',
        'хочу особисто доставити це одній людині.'],

      17 : ['Дід Мороз:',
      "Гаразд дорогі ельф'ята, мені ",
        'час, відзначте цей Новий Рік добре.'],

      18 : ['Олег:','Добре, дякую'],

      19 : ['Катя:','На все добре.'],

      20 : ['Микола:','До побачення!']

    },
    (200,200,200), int(screen_width*0.021))

credits_text = Text([
      "Christmas Adventure 2023",
      "-----------------------------------------",
      "",
      "Сценарист:",
      "",
      "Мамедов Артур",
      "",
      "",
      "",
      "",
      "",
      "Программісти:",
      "",
      "",
      "Іванов Максим",
      "",
      "Мамедов Артур",
      "",
      "Андросов Данило",
      "",
      "Сенчішин Артем",
      "",
      "Кравчук Андрій",
      "",
      "",
      "",
      "",
      "",
      "Дизайнери:",
      "",
      "",
      "Чекаліна Тома",
      "",
      "Мамедов Артур",
      "",
      "Бабай Роман",
      "",
      "",
      "",
      "",
      "",
      "Звукорежисери:",
      "",
      "",
      "Андросов Данило",
      "",
      "Мамедов Артур",
      "",
      "Іванов Максим",
      "",
      "",
      "",
      "",
      "",
      "Проектувальники:",
      "",
      "",
      "Косьмінін Сергій",
      "",
      "Мамедов Артур",
      "",
      "Кравчук Андрій",
      "",
      "Андросов Данило",
      "",
      "",
      "",
      "",
      "",
      "Члени команди:",
      "",
      "",
      "Мамедов Артур",
      "",
      "Іванов Максим",
      "",
      "Чекаліна Тома",
      "",
      "Андросов Данило",
      "",
      "Сенчішин Артем",
      "",
      "Косьмін Сергій",
      "",
      "Кравчук Андрій",
      "",
      "Бабай Рома",
      "",
      "",
      "",
      "",
      "",
      "Музика:",
      "",
      "",
      "Window · Іchika Nito",
      "",
      "Home · Іchika Nito",
      "",
      "i'm sorry · Іchika Nito",
      "",
      "Picturesque · Іchika Nito",
      "",
      "i miss you · Іchika Nito",
      "",
      "Щедрівочка(мінус)",

    ],
    (255,255,255), int(screen_width*0.026))