from django.core.management.base import BaseCommand
from people.models import AdultLion, BabyLion
from generation.models import Generation

class Command(BaseCommand):
    def handle(self, *args, **options):
        generation6 = Generation.objects.get(number=6)
        generation7 = Generation.objects.get(number=7)
        generation8 = Generation.objects.get(number=8)
        generation9 = Generation.objects.get(number=9)
        generation10 = Generation.objects.get(number=10)
        generation11 = Generation.objects.get(number=11)
        generation12 = Generation.objects.get(number=12)

        adult_lion_data = [
            {'name': '김멋사', 'generation_id': generation6, 'part': 'FRONT-END', 'emoji': '운영진_이모지.jpg'},
            {'name': '김멋사', 'generation_id': generation7, 'part': 'FRONT-END', 'emoji': '운영진_이모지.jpg'},
            {'name': '김멋사', 'generation_id': generation8, 'part': 'FRONT-END', 'emoji': '운영진_이모지.jpg'},
            {'name': '김멋사', 'generation_id': generation9, 'part': 'FRONT-END', 'emoji': '운영진_이모지.jpg'},
            {'name': '김멋사', 'generation_id': generation10, 'part': 'FRONT-END', 'emoji': '운영진_이모지.jpg'},

            {'name': '한우석', 'generation_id': generation11, 'part': 'FRONT-END', 'emoji': '운영진_이모지.jpg'},
            {'name': '진민석', 'generation_id': generation11, 'part': 'FRONT-END', 'emoji': '운영진_이모지.jpg'},
            {'name': '김아영', 'generation_id': generation11, 'part': 'FRONT-END', 'emoji': '운영진_이모지.jpg'},
            {'name': '박채린', 'generation_id': generation11, 'part': 'FRONT-END', 'emoji': '운영진_이모지.jpg'},
            {'name': '정지우', 'generation_id': generation11, 'part': 'FRONT-END', 'emoji': '운영진_이모지.jpg'},
            {'name': '이종미', 'generation_id': generation11, 'part': 'BACK-END', 'emoji': '운영진_이모지.jpg'},
            {'name': '성현동', 'generation_id': generation11, 'part': 'BACK-END', 'emoji': '운영진_이모지.jpg'},
            {'name': '윤태호', 'generation_id': generation11, 'part': 'BACK-END', 'emoji': '운영진_이모지.jpg'},

            {'name': '정인영', 'generation_id': generation12, 'part': 'FRONT-END', 'emoji': '정인영.PNG'},
            {'name': '임정연', 'generation_id': generation12, 'part': 'BACK-END', 'emoji': '임정연.PNG'},
            {'name': '정고은', 'generation_id': generation12, 'part': 'FRONT-END', 'emoji': '정고은.PNG'},
            {'name': '이선명', 'generation_id': generation12, 'part': 'FRONT-END', 'emoji': '이선명.PNG'},
            {'name': '김유이', 'generation_id': generation12, 'part': 'BACK-END', 'emoji': '김유이.PNG'},
            {'name': '오은택', 'generation_id': generation12, 'part': 'BACK-END', 'emoji': '오은택.PNG'},
            {'name': '장세환', 'generation_id': generation12, 'part': 'FRONT-END', 'emoji': '장세환.PNG'},
        ]

        for lion_data in adult_lion_data:
            AdultLion.objects.create(**lion_data)
        
        baby_lion_data = [

            # 6기
            {'name': '강서현', 'generation_id': generation6, 'part': 'FRONT-END'},
            {'name': '권지상', 'generation_id': generation6, 'part': 'FRONT-END'},
            {'name': '김수민', 'generation_id': generation6, 'part': 'FRONT-END'},
            {'name': '김수빈', 'generation_id': generation6, 'part': 'FRONT-END'},
            {'name': '김한비', 'generation_id': generation6, 'part': 'FRONT-END'},
            {'name': '박성은', 'generation_id': generation6, 'part': 'FRONT-END'},
            {'name': '박진휘', 'generation_id': generation6, 'part': 'FRONT-END'},
            {'name': '백동선', 'generation_id': generation6, 'part': 'FRONT-END'},
            {'name': '백지수', 'generation_id': generation6, 'part': 'FRONT-END'},
            {'name': '신유라', 'generation_id': generation6, 'part': 'FRONT-END'},
            {'name': '연다은', 'generation_id': generation6, 'part': 'FRONT-END'},
            {'name': '유석환', 'generation_id': generation6, 'part': 'FRONT-END'},
            {'name': '윤재성', 'generation_id': generation6, 'part': 'FRONT-END'},
            {'name': '이은무', 'generation_id': generation6, 'part': 'FRONT-END'},
            {'name': '이재인', 'generation_id': generation6, 'part': 'FRONT-END'},
            {'name': '이준희', 'generation_id': generation6, 'part': 'FRONT-END'},
            {'name': '이지원', 'generation_id': generation6, 'part': 'FRONT-END'},
            {'name': '정윤진', 'generation_id': generation6, 'part': 'FRONT-END'},
            {'name': '조선미', 'generation_id': generation6, 'part': 'FRONT-END'},
            {'name': '채영서', 'generation_id': generation6, 'part': 'FRONT-END'},
            {'name': '하창권', 'generation_id': generation6, 'part': 'FRONT-END'},

            # 7기
            {'name': '강은비', 'generation_id': generation7, 'part': 'FRONT-END'},
            {'name': '고우준', 'generation_id': generation7, 'part': 'FRONT-END'},
            {'name': '김지연', 'generation_id': generation7, 'part': 'FRONT-END'},
            {'name': '김지웅', 'generation_id': generation7, 'part': 'FRONT-END'},
            {'name': '김현정', 'generation_id': generation7, 'part': 'FRONT-END'},
            {'name': '박재형', 'generation_id': generation7, 'part': 'FRONT-END'},
            {'name': '박진근', 'generation_id': generation7, 'part': 'FRONT-END'},
            {'name': '박채인', 'generation_id': generation7, 'part': 'FRONT-END'},
            {'name': '신누리', 'generation_id': generation7, 'part': 'FRONT-END'},
            {'name': '신현귀', 'generation_id': generation7, 'part': 'FRONT-END'},
            {'name': '양정인', 'generation_id': generation7, 'part': 'FRONT-END'},
            {'name': '윤석중', 'generation_id': generation7, 'part': 'FRONT-END'},
            {'name': '윤여경', 'generation_id': generation7, 'part': 'FRONT-END'},
            {'name': '이미정', 'generation_id': generation7, 'part': 'FRONT-END'},
            {'name': '이민주', 'generation_id': generation7, 'part': 'FRONT-END'},
            {'name': '이용욱', 'generation_id': generation7, 'part': 'FRONT-END'},
            {'name': '장주호', 'generation_id': generation7, 'part': 'FRONT-END'},
            {'name': '조형준', 'generation_id': generation7, 'part': 'FRONT-END'},

            # 8기
            {'name': '김대덕', 'generation_id': generation8, 'part': 'FRONT-END'},
            {'name': '김준형', 'generation_id': generation8, 'part': 'FRONT-END'},
            {'name': '김진형', 'generation_id': generation8, 'part': 'FRONT-END'},
            {'name': '박소희', 'generation_id': generation8, 'part': 'FRONT-END'},
            {'name': '박수진', 'generation_id': generation8, 'part': 'FRONT-END'},
            {'name': '박유림', 'generation_id': generation8, 'part': 'FRONT-END'},
            {'name': '박준형', 'generation_id': generation8, 'part': 'FRONT-END'},
            {'name': '박혜리', 'generation_id': generation8, 'part': 'FRONT-END'},
            {'name': '성유진', 'generation_id': generation8, 'part': 'FRONT-END'},
            {'name': '안서진', 'generation_id': generation8, 'part': 'FRONT-END'},
            {'name': '안재연', 'generation_id': generation8, 'part': 'FRONT-END'},
            {'name': '윤다영', 'generation_id': generation8, 'part': 'FRONT-END'},
            {'name': '이용환', 'generation_id': generation8, 'part': 'FRONT-END'},
            {'name': '이혜인', 'generation_id': generation8, 'part': 'FRONT-END'},
            {'name': '임지선', 'generation_id': generation8, 'part': 'FRONT-END'},
            {'name': '임하은', 'generation_id': generation8, 'part': 'FRONT-END'},
            {'name': '조휘건', 'generation_id': generation8, 'part': 'FRONT-END'},
            {'name': '최윤서', 'generation_id': generation8, 'part': 'FRONT-END'},

            # 9기
            {'name': '강현석', 'generation_id': generation9, 'part': 'FRONT-END'},
            {'name': '길민지', 'generation_id': generation9, 'part': 'FRONT-END'},
            {'name': '김동윤', 'generation_id': generation9, 'part': 'FRONT-END'},
            {'name': '김서연', 'generation_id': generation9, 'part': 'FRONT-END'},
            {'name': '김수미', 'generation_id': generation9, 'part': 'FRONT-END'},
            {'name': '김요욱', 'generation_id': generation9, 'part': 'FRONT-END'},
            {'name': '김재연', 'generation_id': generation9, 'part': 'FRONT-END'},
            {'name': '김찬수', 'generation_id': generation9, 'part': 'FRONT-END'},
            {'name': '김효진', 'generation_id': generation9, 'part': 'FRONT-END'},
            {'name': '민세은', 'generation_id': generation9, 'part': 'FRONT-END'},
            {'name': '박다빈', 'generation_id': generation9, 'part': 'FRONT-END'},
            {'name': '박채린', 'generation_id': generation9, 'part': 'FRONT-END'},
            {'name': '위서영', 'generation_id': generation9, 'part': 'FRONT-END'},
            {'name': '이강희', 'generation_id': generation9, 'part': 'FRONT-END'},
            {'name': '이상윤', 'generation_id': generation9, 'part': 'FRONT-END'},
            {'name': '이육샛별', 'generation_id': generation9, 'part': 'FRONT-END'},
            {'name': '이하은', 'generation_id': generation9, 'part': 'FRONT-END'},
            {'name': '임유경', 'generation_id': generation9, 'part': 'FRONT-END'},
            {'name': '조민경', 'generation_id': generation9, 'part': 'FRONT-END'},
            {'name': '함희원', 'generation_id': generation9, 'part': 'FRONT-END'},

            # 10기
            {'name': '곽도영', 'generation_id': generation10, 'part': 'FRONT-END'},
            {'name': '김건', 'generation_id': generation10, 'part': 'FRONT-END'},
            {'name': '김명윤', 'generation_id': generation10, 'part': 'FRONT-END'},
            {'name': '김민지', 'generation_id': generation10, 'part': 'FRONT-END'},
            {'name': '김아영', 'generation_id': generation10, 'part': 'FRONT-END'},
            {'name': '김효정', 'generation_id': generation10, 'part': 'FRONT-END'},
            {'name': '박정은', 'generation_id': generation10, 'part': 'FRONT-END'},
            {'name': '박정환', 'generation_id': generation10, 'part': 'FRONT-END'},
            {'name': '성현동', 'generation_id': generation10, 'part': 'FRONT-END'},
            {'name': '오대균', 'generation_id': generation10, 'part': 'FRONT-END'},
            {'name': '오창엽', 'generation_id': generation10, 'part': 'FRONT-END'},
            {'name': '유창호', 'generation_id': generation10, 'part': 'FRONT-END'},
            {'name': '윤태호', 'generation_id': generation10, 'part': 'FRONT-END'},
            {'name': '이승연', 'generation_id': generation10, 'part': 'FRONT-END'},
            {'name': '이용욱', 'generation_id': generation10, 'part': 'FRONT-END'},
            {'name': '이종미', 'generation_id': generation10, 'part': 'FRONT-END'},
            {'name': '정지우', 'generation_id': generation10, 'part': 'FRONT-END'},
            {'name': '진민석', 'generation_id': generation10, 'part': 'FRONT-END'},
            {'name': '최세은', 'generation_id': generation10, 'part': 'FRONT-END'},
            {'name': '최현수', 'generation_id': generation10, 'part': 'FRONT-END'},
            {'name': '한우석', 'generation_id': generation10, 'part': 'FRONT-END'},

            # 11기
            {'name': '김민지', 'generation_id': generation11, 'part': 'FRONT-END'},
            {'name': '송경호', 'generation_id': generation11, 'part': 'FRONT-END'},
            {'name': '김규빈', 'generation_id': generation11, 'part': 'BACK-END'},
            {'name': '임정연', 'generation_id': generation11, 'part': 'BACK-END'},
            {'name': '정태현', 'generation_id': generation11, 'part': 'BACK-END'},
            {'name': '권보미', 'generation_id': generation11, 'part': 'FRONT-END'},
            {'name': '정고은', 'generation_id': generation11, 'part': 'FRONT-END'},
            {'name': '강민석', 'generation_id': generation11, 'part': 'BACK-END'},
            {'name': '최승호', 'generation_id': generation11, 'part': 'BACK-END'},
            {'name': '오은택', 'generation_id': generation11, 'part': 'BACK-END'},
            {'name': '김기철', 'generation_id': generation11, 'part': 'FRONT-END'},
            {'name': '정인영', 'generation_id': generation11, 'part': 'FRONT-END'},
            {'name': '신선희', 'generation_id': generation11, 'part': 'BACK-END'},
            {'name': '윤성호', 'generation_id': generation11, 'part': 'BACK-END'},
            {'name': '이우찬', 'generation_id': generation11, 'part': 'BACK-END'},
            {'name': '문소정', 'generation_id': generation11, 'part': 'FRONT-END'},
            {'name': '장세환', 'generation_id': generation11, 'part': 'FRONT-END'},
            {'name': '노현서', 'generation_id': generation11, 'part': 'BACK-END'},
            {'name': '신명준', 'generation_id': generation11, 'part': 'BACK-END'},
            {'name': '김성현', 'generation_id': generation11, 'part': 'BACK-END'},
            {'name': '이상연', 'generation_id': generation11, 'part': 'FRONT-END'},
            {'name': '이선명', 'generation_id': generation11, 'part': 'FRONT-END'},
            {'name': '고유진', 'generation_id': generation11, 'part': 'BACK-END'},
            {'name': '김유이', 'generation_id': generation11, 'part': 'BACK-END'},
            {'name': '이건화', 'generation_id': generation11, 'part': 'BACK-END'},
        ]

        for lion_data in baby_lion_data:
            BabyLion.objects.create(**lion_data)


        self.stdout.write(self.style.SUCCESS('People data created!'))