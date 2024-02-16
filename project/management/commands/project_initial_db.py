from django.core.management.base import BaseCommand
from generation.models import Generation
from project.models import Project

class Command(BaseCommand):
    def handle(self, *args, **options):
        generation11 = Generation.objects.get(number=11)
        generation12 = Generation.objects.get(number=12)

        project_data = [

            # 11기
            { 
                'title': 'TU:PL',
                'generation_id': generation11,
                'year': 2023,  
                'team_name': '튜플',
                'member_list': '강민석 고유진 권보미 김기철 오은택 임정연',
                'project_image': 'TUPL.png',  
                'content': '복잡한 과외 과정을 단 하나의 플랫폼으로 해결할 수 있는 통합 과외 관리 서비스입니다. 과외를 할\
                    때, 과외 일정 관리는 캘린더에서, 진도 기록은 메모장에서, 학생과의 소통은 메신저에서 따로따로\
                    해야 하는 불편함이 있습니다. 이러한 불편함을 해소하기 위해, 과외를 위해 필요한 기능들을 단 \
                    하나의 플랫폼으로 압축했습니다. 선생님-학생 연동, 캘린더, 수업 일지, 입금 관리 등의 기능이 있습\
                    니다.',
                'url': 'https://github.com/LIKELION-TUPLE'  
            },
            { 
                'title': 'Silver Campus',
                'generation_id': generation11,
                'year': 2023,  
                'team_name': '효를 아십니까',
                'member_list': '김규빈 김민지 송경호 임정연 정태현',
                'project_image': 'SILVERCAMPUS',
                'content': '연령에 따른 디지털 공간 격차를 해소하기 위한, 시니어 온라인 강의&커뮤니티 \
                    플랫폼입니다. 타 강의 웹 서비스와의 차별점은 다음과 같습니다. 간단하고 편리한 UI, 음성 안내 서비스, \
                    시니어 맞춤 컨텐츠, 소셜 페이지 ‘청년 광장 등의 서비스를 제공합니다.',
                'url': 'https://github.com/SilverCampus'  
            },
            { 
                'title': 'YouCheck',
                'generation_id': generation11,
                'year': 2023,  
                'team_name': '효자동개발자',
                'member_list': '이상연 이선명 고유진 김유이 이건화 윤태호 진민석',
                'project_image': 'YOUCHECK.png',  
                'content': 'One Click, More Check. \
                    유튜브를 통한 정보 습득이 증가하면서, 유튜브를 통한 뉴스 이용에 대해 많은 우려가 생겼어요.\
                    이에 팀 효자동개발자는 뉴미디어 리터러시가 낮아 유튜브 영상을 비판적으로 보기 어려운 사용자\
                    들이 다양한 의견에 노출되게 함으로써 사회 양극화를 막는 서비스를 개발했어요.\
                    유튜브 링크를 붙여 넣기만 하면 해당 영상의 요약본과 관련 기사들을 비교할 수 있어, \
                    영상과 관련된 정보를 쉽고 빠르게 찾아볼 수 있어요.',
                'url': "https://github.com/GoodBoyDevelopers"  
            },
            { 
                'title': 'SellPoint',
                'generation_id': generation11,
                'year': 2023,  
                'team_name': 'SellPoint',
                'member_list': '최승호 신명준 이건화 윤성호 진민석 이선명',
                'project_image': 'SELLPOINT.png',  
                'content': '팔 때를 아는 것, 그것이 진정한 투자의 시작. \
                    투자자들에게 종목에 대한 전문가의 의견을 제시해 주는 AI 기반의 애널리틱스 플랫폼.',
                'url': "https://github.com/sellpointSogang"  
            },
            { 
                'title': 'YouMap',
                'generation_id': generation11,
                'year': 2023,  
                'team_name': '복커톤 3조',
                'member_list': '송경호 이선명 김성현 김유이 신명준',
                'project_image': 'YOUMAP.png',  
                'content': '다양한 커뮤니티에 흩어져 있는 학교 정보, 꿀팁들의 핵심만 모아볼 수 있는 플랫폼. 지도를 바탕으로 혼자 공부하기 좋은, 팀플하기 좋은, 쉬기 좋은 장소 추천.',
                'url': "https://github.com/You-Map"  
            },
            { 
                'title': 'CREWS',
                'generation_id': generation11,
                'year': 2023,  
                'team_name': 'CREWS',
                'member_list': '송경호 정인영 정고은 정태현 이종미 김규빈',
                'project_image': 'CREWS.png',  
                'content': '동아리 홍보 모집, 리쿠르팅, 면접자 관리와 같은 서비스를 제공하는 웹.',
                'url': "https://www.instagram.com/p/C0MMCCpPecO/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA=="  
            },
            { 
                'title': '그땐그랬지',
                'generation_id': generation11,
                'year': 2023,  
                'team_name': '6학년 3반 이미정',
                'member_list': '강민석 오은택 권보미 정고은 최승호',
                'project_image': '그땐그랬지.jpg',  
                'content': '<그땐 그랬지>는 7080을 위한 특별한 모임 서비스입니다. 언제 어디서든, 그때의 따뜻한 감성과 추억을 느껴보세요!',
                'url': "https://github.com/LIKELION-THROWBACK"  
            },
            { 
                'title': 'Road Through Sogang',
                'generation_id': generation11,
                'year': 2023,  
                'team_name': 'RTS',
                'member_list': '김민지 김성현 문소정 이우찬 장세환',
                'project_image': 'RTS.png',  
                'content': '이수한 과목과 듣고 싶은 강의를 로드맵에 정리하여 학점 관리와 학기별 과목 배치를 한눈에 볼 수 있는 플랫폼으로 학점관리 및 수강계획에 도움을 주는 플랫폼입니다.',
                'url': "https://github.com/RTS-Road-Through-Sogang"  
            },
            { 
                'title': 'Koogle',
                'generation_id': generation11,
                'year': 2023,  
                'team_name': 'Koogle',
                'member_list': '김민지 김성현 문소정 이우찬 장세환',
                'project_image': 'KOOGLE.png',  
                'content': '외국인을 위한 맞춤형 맛집 탐색 플랫폼으로, 사용자 친화적인 번역 기능과 자체 리뷰 시스템을 통해 여행자가 현지의 맛집을 쉽게 찾고 경험할 수 있도록 돕는 플랫폼입니다.',
                'url': "https://github.com/SojeongM/Koogle_front"
            },

            # 12기
            { 
                'title': '멋쟁이사자차럼 서강대학교 공식 홈페이지 프로젝트',
                'generation_id': generation12,
                'year': 2024,  
                'team_name': '12기 운영진',
                'member_list': '김유이 이선명 임정연 장세환 정고은 정인영',
                'project_image': 'KakaoTalk_20240216_161310064.png',  
                'content': '멋쟁이사자처럼 서강대학교 공식 홈페이지입니다.',
                'url': "https://www.likelionsg.site/"  
            },
        ]

        for project in project_data:
            Project.objects.create(**project)

        self.stdout.write(self.style.SUCCESS('Project data created!'))