guest_list = ['jim hendrix', 'bob marley', 'jc']
invitation_letter = f'Dear {guest_list[0].title()}, please be my guest this Christmas. We will celebrate and make memory of the the we got saved'
print(invitation_letter)
invitation_letter = f'Dear {guest_list[1].title()}, please be my guest this Christmas. We will celebrate and make memory of the the we got saved'
print(invitation_letter)
invitation_letter = f'Dear {guest_list[2].title()}, please be my guest this Christmas. We will celebrate and make memory of the the we got saved'
print(invitation_letter)

guest_list = ['jim hendrix', 'bob marley', 'jc']
can_not_attend = 'bob marley'
guest_list.remove(can_not_attend)
guest_list.insert(0, 'rose')
guest_list.insert(1,'andrew')
guest_list.append('natasha')
#from here, we start to "uninvite" people
guests_univited_1 = guest_list.pop(0)
print(f'Please, forgive me. I am short of money and need to univite you {guests_univited_1.title()}')
guests_univited_2 = guest_list.pop(2)  
print(f'Please, forgive me. I am short of money and need to univite you {guests_univited_2.title()}')
guest_total = len(guest_list)
print(f' Number of attendees: {guest_total}')
print(guest_list)

invitation_letter = f'Dear {guest_list[0].title()}, please be my guest this Christmas. We will celebrate and make memory of the the we got saved'
print(invitation_letter)
invitation_letter = f'Dear {guest_list[1].title()}, please be my guest this Christmas. We will celebrate and make memory of the the we got saved'
print(invitation_letter)
invitation_letter = f'Dear {guest_list[2].title()}, please be my guest this Christmas. We will celebrate and make memory of the the we got saved'
print(invitation_letter)
#invitation_letter = f'Dear {guest_list[3].title()}, please be my guest this Christmas. We will celebrate and make memory of the the we got saved'
#print(invitation_letter)
#invitation_letter = f'Dear {guest_list[#].title()}, please be my guest this Christmas. We will celebrate and make memory of the the we got saved'
#print(invitation_letter)