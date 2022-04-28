# # 패키지 임포트
# import mymath
#
# # 서브패키지 임포트
# import mymath.shapes
#
# # 모듈 임포트
# import mymath.shapes.area
#
# # 모듈 안에 있는 변수나 함수는 이 방식으로 임포트 할 수 없음
# import mymath.shapes.area.circle # 오류
#
# # 패키지 안에 있는 패키지 임포트
# from mymath import shapes
#
# # 패키지 안에 있는 모듈 임포트
# from mymath.shapes import area
#
# # 모듈 안에 있는 함수 임포트
# from mymath.shapes.area import circle
#
# # import 뒤에는 . 을 쓸 수 없음
# from mymath import shapes.area # 오류