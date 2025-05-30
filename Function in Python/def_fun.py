## Name Prameters


# def subj(Hindi, English, Math, Science, SScience):
#     print(f"Total number in Hindi = {Hindi}")
#     print(f"Total number in Hindi = {SScience}")
#     print(f"Total number in Hindi = {Math}")
#     print(f"Total number in Hindi = {Science}")
#     print(f"Total number in Hindi = {English}")
#     total = Hindi + English + Math + SScience + Science
#     print(f"Your Total Score is {total}")


# # subj(Hindi=90, Math=100, Science=50, SScience=80, English=70)
# subj(90, Math=100, Science=50, SScience=80, English=70)


## Default Values


# def subj(Hindi=0, English=0, Math=0, Science=0, SScience=0):
#     print(f"Total number in Hindi = {Hindi}")
#     print(f"Total number in SScience = {SScience}")
#     print(f"Total number in Math = {Math}")
#     print(f"Total number in Science = {Science}")
#     print(f"Total number in English = {English}")
#     total = Hindi + English + Math + SScience + Science
#     print(f"Your Total Score is {total}")


# subj(90, 70)


# Default Paramerers


def subj(Hindi, English, Math=60, Science=0, SScience=57):
    print(f"Total number in Hindi = {Hindi}")
    print(f"Total number in Hindi = {SScience}")
    print(f"Total number in Hindi = {Math}")
    print(f"Total number in Hindi = {Science}")
    print(f"Total number in Hindi = {English}")
    total = Hindi + English + Math + SScience + Science
    print(f"Your Total Score is {total}")


# subj(Hindi=90, Math=100, Science=50, SScience=80, English=70)
# subj(90, Math=100, Science=50, SScience=80, English=70)
subj(90, 100)
