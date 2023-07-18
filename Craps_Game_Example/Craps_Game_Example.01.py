from random import choice, randint

bots = ['batista', 'lilly', 'thor']
minimum_bet = 100

user_dict = {
    '1': {
        'user_name': 'mason',
        'password': '123',
        'safe': 1200
    },
    '2': {
        'user_name': 'alex',
        'passoword': '1234',
        'safe': 2200
    }
}

def assing_defult_bot(lst: list) -> str:
    return choice(lst)


def roil_dicle() -> int:
    return randint(1, 6) + randint(1, 6)


def bet_is_valid(bet: int, safe: int) -> bool:
    if minimum_bet <= bet <= safe:
        return True
    else:
        return False


def gain_daily_chips() -> int:
    return randint(1000, 2000)


def login(user_name: str, password: str) -> dict:
    is_user_active = False
    counter = ''
    for i in range(1, len(user_dict) + 1):
        if user_dict.get(str(i)).get('user_name') == user_name and \
                user_dict.get(str(i)).get('password') == password:
            is_user_active = True
            counter = str(i)
            break

    if is_user_active:
        return user_dict.get(counter)
    else:
        return {}


def main():
    user_name = input('User Name:')
    password = input('Password: ')
    auth_user = login(user_name, password)
    if auth_user != {}:
        print(auth_user)
        chips = gain_daily_chips()
        print(f'Welcome, Gain{chips} daily chips..!')
        auth_user.update({
            'safe': auth_user.get('safe') + chips
        })
        bet = int(input('Please type your bet'))
        if bet_is_valid(bet, auth_user.get('safe')):
            player_2 = assing_defult_bot(bots)

            player_1_roll = roil_dicle()
            player_2_roll = roil_dicle()

            print(f"{auth_user.get('user_name')} roller ==> {player_1_roll}")
            print(f"{player_2} roller ==> {player_2_roll}")

            if player_1_roll > player_2_roll:
                print(f"{auth_user.get('user_name')} has been victor..!")
                auth_user.update({
                    'safe': auth_user.get('safe') + bet ** 2
                })
            elif player_1_roll < player_2_roll:
                print(f"{player_2} has been victor..!")
                auth_user.update({
                    'safe': auth_user.get('safe') - bet
                })
        else:
            print("Your bet hasn't valid..!")

    else:
        print('Please check your account information..!')


main()
