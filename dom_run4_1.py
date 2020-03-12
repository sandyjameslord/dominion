import random


class Card:
    def __init__(self, name, cost, abilities, victory_points, is_automatic_end_of_turn_play, is_playable, coins_worth):
        self.name = name
        self.cost = cost
        self.abilities = abilities
        self.victory_points = victory_points
        self.is_automatic_end_of_turn_play = is_automatic_end_of_turn_play
        self.is_playable = is_playable
        self.coins_worth = coins_worth


class BuyPile(Card):
    def __init__(self):
        chapels = [Card("chapel", 2, ["trash", "trash", "trash", "trash"], 0, False, True, 0) for i in range(10)]
        woodcutters = [Card("woodcutter", 3, ["coin", "coin", "buy"], 0, False, True, 0) for i in range(10)]
        villages = [Card("village", 3, ["draw", "action", "action"], 0, False, True, 0) for i in range(10)]
        smithies = [Card("smithy", 4, ["draw", "draw", "draw"], 0, False, True, 0) for i in range(10)]
        moneylenders = [Card("moneylender", 4, ["trash_copper"], 0, False, True, 0) for i in range(10)]
        remodels = [Card("remodel", 4, ["remodel"], 0, False, True, 0) for i in range(10)]
        thronerooms = [Card("throneroom", 4, ["play_twice"], 0, False, True, 0) for i in range(10)]
        festivals = [Card("festival", 5, ["buy", "action", "action", "coin", "coin"], 0, False, True, 0) for i in
                     range(10)]
        labs = [Card("lab", 5, ["draw", "draw", "action"], 0, False, True, 0) for i in range(10)]
        markets = [Card("market", 5, ["buy", "action", "coin", "draw"], 0, False, True, 0) for
                   i in range(10)]

        coppers = [Card("copper", 0, [], 0, True, False, 1) for i in range(30)]
        silvers = [Card("silver", 3, [], 0, True, False, 2) for i in range(30)]
        golds = [Card("gold", 6, [], 0, True, False, 3) for i in range(30)]

        estates = [Card("estate", 2, [], 1, False, False, 0) for i in range(8)]
        duchies = [Card("duchy", 5, [], 3, False, False, 0) for i in range(8)]
        provinces = [Card("province", 8, [], 6, False, False, 0) for i in range(8)]
        cahds = [chapels, woodcutters, villages, smithies, moneylenders, remodels, thronerooms, festivals, labs,
                 markets, coppers, silvers, golds, estates, duchies, provinces]
        self.buy_pile = cahds

    def get_buy_pile(self):
        cahds = ["chapels", "woodcutters", "villages", "smithies", "moneylenders", "remodels", "thronerooms", "festivals", "labs",
                 "markets", "coppers", "silvers", "golds", "estates", "duchies", "provinces"]
        text = ""
        for idx, pile in enumerate(self.buy_pile):
            try:
                text += f"{len(pile)} {pile[0].name}{str('s' if len(pile) != 1 else '')} left \n"
            except IndexError:
                text += f"0 {cahds[idx]} left \n"
        return text


class Deck:
    def __init__(self):
        self.hand = []
        self.draw_pile = []
        self.discard_pile = []
        coppers = [Card("copper", 0, [], 0, True, False, 1) for i in range(7)]
        estates = [Card("estate", 2, [], 1, False, False, 0) for i in range(3)]
        markets = [Card("market", 5, ["buy", "action", "coin", "draw"], 0, False, True, 0) for i in range(10)]
        self.draw_pile = coppers + estates + markets
        random.shuffle(self.draw_pile)
        self.deck = [self.hand, self.draw_pile, self.discard_pile]

    def get_deck(self):
        return self.deck

    def set_deck(self, cards_pile):
        self.deck = cards_pile


class Player:
    def __init__(self, player_name):
        self.player_name = player_name


def draw_a_card(not_playable_cards, playable_cards, draw_pile, discard_pile):
    try:
        first_card = draw_pile[0]
        if first_card.is_playable:
            print()
            print(f"You drew a {first_card.name} and added it to the playable pile")
            playable_cards.append(first_card)
        else:
            print()
            print(f"You drew a {first_card.name} and added it to your hand")
            not_playable_cards.append(first_card)
        draw_pile = draw_pile[1:]
    except:
        random.shuffle(discard_pile)
        draw_pile = discard_pile
        discard_pile = []
    return not_playable_cards, playable_cards, draw_pile, discard_pile


def get_initial_hand(hand, draw_pile):
    while len(hand) < 5:
        first_card = draw_pile[0]
        hand.append(first_card)
        draw_pile.remove(first_card)
    return hand, draw_pile


def get_new_hand(draw_pile, discard_pile):
    hand = []
    while len(hand) < 5:
        try:
            first_card = draw_pile[0]
            hand.append(first_card)
            draw_pile = draw_pile[1:]
        except:
            random.shuffle(discard_pile)
            draw_pile = discard_pile
            discard_pile = []
    text = "Cards in fresh hand before passing turn: "
    for card in hand:
        text += card.name + "  **  "
    print(text)
    return hand, draw_pile, discard_pile


def add_a_buy():
    return 1


def add_an_action():
    return 1


def add_a_coin():
    return 1


def trash_a_copper(not_playable_cards):
    for cahdd in not_playable_cards:
        if cahdd.name == "copper":
            print("copper trashed, 3 coins added")
            not_playable_cards.remove(cahdd)
            break
    return 3, not_playable_cards


def trash_a_card(not_playable_cards, playable_cards):
    all_possible_trash_cards = []
    for c in not_playable_cards:
        all_possible_trash_cards.append(c)
    for car in playable_cards:
        all_possible_trash_cards.append(car)
    t = ""
    for cardd in all_possible_trash_cards:
        t += cardd.name + " ** "
    print("Here are your possible cards to trash: ", t)
    choice = input("Would you like to use a trash? y/n")
    if choice == "y":
        i = 0
        while i < len(all_possible_trash_cards):
            choice2 = input(f"Trash a {all_possible_trash_cards[i].name}? y/n")
            if choice2 == "y":
                if all_possible_trash_cards[i] in not_playable_cards:
                    print(f"{all_possible_trash_cards[i].name} trashed")
                    not_playable_cards.remove(all_possible_trash_cards[i])
                    break
                elif all_possible_trash_cards[i] in playable_cards:
                    print(f"{all_possible_trash_cards[i].name} trashed")
                    playable_cards.remove(all_possible_trash_cards[i])
                    break
            else:
                i += 1
    else:
        print("Trash given up")
    return not_playable_cards, playable_cards


def remodel(not_playable_cards, playable_cards, discard_pile, buy_pile):
    all_possible_remodel_cards = []
    for c in not_playable_cards:
        all_possible_remodel_cards.append(c)
    for car in playable_cards:
        all_possible_remodel_cards.append(car)
    t = ""
    for carddd in all_possible_remodel_cards:
        t += carddd.name + " ** "
    print("Here are your possible cards to remodel: ", t)
    choice = input("Would you like to use a remodel? y/n")
    if choice == "y":
        value = 0
        i = 0
        while i < len(all_possible_remodel_cards):
            choice2 = input(f"Remodel a {all_possible_remodel_cards[i].name}? y/n")
            value = all_possible_remodel_cards[i].cost
            if choice2 == "y":
                if all_possible_remodel_cards[i] in not_playable_cards:
                    print(f"{all_possible_remodel_cards[i].name} trashed, waiting for upgrade")
                    not_playable_cards.remove(all_possible_remodel_cards[i])
                    break
                elif all_possible_remodel_cards[i] in playable_cards:
                    print(f"{all_possible_remodel_cards[i].name} trashed, waiting for upgrade")
                    playable_cards.remove(all_possible_remodel_cards[i])
                    break
            else:
                i += 1
        if value:
            print("choose a card worth 2 more than: ", value)
            print(buy_pile.get_buy_pile())
            for pile in buy_pile.buy_pile:
                if pile[0].cost == value + 2:
                    choice = input(
                        f"Get a {pile[0].name} y/n")
                    if choice == "y":
                        discard_pile.append(pile[0])
                        pile.remove(pile[0])
                        break
    else:
        print("Remodel given up")
    return not_playable_cards, playable_cards, discard_pile, buy_pile


def play_one_card_two_times(not_playable_cards, playable_cards, discard_pile, buy_pile, draw_pile, play_pile, coins, buys, actions):
    for card in playable_cards:
        print(f"playable pile card: {card.name}", end="  **  ")
    print()
    if len(playable_cards) > 0:
        print(f"Below are your playable cards. Choose 1 card to play twice.")
        play_names = []
        for card in playable_cards:
            play_names.append(card.name)
        if not play_names:
            print("Nothing available to play twice.")
            return not_playable_cards, playable_cards, discard_pile, buy_pile, draw_pile, play_pile, coins, buys, actions
        print(" ".join(play_names))
        index_of_card_to_play = int(input("Choose one of the above by its index (first slot is index 1)"))
        for idx, card in enumerate(playable_cards):
            if idx + 1 == index_of_card_to_play:
                cahd = playable_cards.pop(index_of_card_to_play - 1)
                play_pile.append(cahd)
                abilities_text = ""
                for ability in card.abilities:
                    abilities_text += f" || {str(ability)}"
                print(f"Using a {card.name} for: {str(abilities_text)} {str(abilities_text)}.")
                for ability in card.abilities:
                    if ability == "buy":
                        buys += add_a_buy() + add_a_buy()
                    if ability == "action":
                        actions += add_an_action() + add_an_action()
                    if ability == "coin":
                        coins += add_a_coin() + add_a_coin()
                    if ability == "trash":
                        not_playable_cards, playable_cards = trash_a_card(not_playable_cards, playable_cards)
                        not_playable_cards, playable_cards = trash_a_card(not_playable_cards, playable_cards)
                    if ability == "trash_copper":
                        num, not_playable_cards = trash_a_copper(not_playable_cards)
                        coins += num
                        num, not_playable_cards = trash_a_copper(not_playable_cards)
                        coins += num
                    if ability == "remodel":
                        not_playable_cards, playable_cards, discard_pile, buy_pile = remodel(not_playable_cards,
                                                                                             playable_cards,
                                                                                             discard_pile, buy_pile)
                        not_playable_cards, playable_cards, discard_pile, buy_pile = remodel(not_playable_cards,
                                                                                             playable_cards,
                                                                                             discard_pile, buy_pile)
                    if ability == "draw":
                        not_playable_cards, playable_cards, draw_pile, discard_pile = draw_a_card(
                            not_playable_cards, playable_cards, draw_pile, discard_pile)
                        not_playable_cards, playable_cards, draw_pile, discard_pile = draw_a_card(
                            not_playable_cards, playable_cards, draw_pile, discard_pile)
    return not_playable_cards, playable_cards, discard_pile, buy_pile, draw_pile, play_pile, coins, buys, actions


def buy_a_card(buys, coins, buy_pile):
    cards_bought = []
    choice = int(
        input(
            f"""You have {coins} coin{str('s' if coins != 1 else '')} to spend and {buys} buy{str('s' if buys != 1 else '')}.
                Either use a buy or subtract 1 buy from your buy total.
                (1) to use a buy to buy a card or
                (2) to subtract a buy from your buy total without buying a card"""))
    if choice == 1:
        buys -= 1
        print(buy_pile.get_buy_pile())
        for pile in buy_pile.buy_pile:
            if pile[0].cost <= coins:
                choice = input(f"Current coins: {coins}. Buy a {pile[0].name} for {pile[0].cost}? y/n")
                if choice == "y":
                    coins -= pile[0].cost
                    cards_bought.append(pile[0])
                    pile.remove(pile[0])
                    break
    else:
        buys -= 1
    return buys, coins, cards_bought, buy_pile


def determine_winner_and_print_results(players, decks):
    points = []
    for deck in decks:
        total_cs = []
        d = deck.get_deck()
        for part in d:
            for card in part:
                total_cs.append(card)
        score = 0
        for card in total_cs:
            score += card.victory_points
        points.append(score)
    high_score = points[0]
    winner = players[0]
    for idx, point in enumerate(points):
        if point >= high_score:
            high_score = point
            winner = players[idx]
    print("Final scores: ")
    i = 0
    while i < len(players):
        print(players[i].player_name, points[i])
        i += 1
    print(f"What a game! {winner.player_name} won with {high_score} points! ")
    print("Game over. Play again soon.")


def get_playable_and_not_playable_cards_from_hand(hand):
    playable_cards = []
    not_playable_cards = []
    play_pile = []
    for card in hand:
        if card.is_playable:
            playable_cards.append(card)
        else:
            not_playable_cards.append(card)
    return not_playable_cards, playable_cards


def play_a_card(players, current_turn, actions, coins, buys, playable_cards, not_playable_cards, discard_pile, draw_pile, play_pile, buy_pile):
    print(f"Actions: {actions} || Coins: {coins} || Buys: {buys}")
    print(f"Here are your playable cards for your {actions} action{str('s' if actions != 1 else '')}: ")
    play_names = []
    for card in playable_cards:
        play_names.append(card.name)
    print(" ".join(play_names))
    index_of_card_to_play = int(input("Choose one of the above by its index (first slot is index 1)"))
    for idx, card in enumerate(playable_cards):
        if idx + 1 == index_of_card_to_play:
            cahd = playable_cards.pop(index_of_card_to_play - 1)
            play_pile.append(cahd)
            abilities_text = ""
            for ability in card.abilities:
                abilities_text += f" || {str(ability)}"
            print(f"Using a {card.name} for: {str(abilities_text)}.")
            for ability in card.abilities:
                if ability == "buy":
                    buys += add_a_buy()
                if ability == "action":
                    actions += add_an_action()
                if ability == "coin":
                    coins += add_a_coin()
                if ability == "trash":
                    not_playable_cards, playable_cards = trash_a_card(not_playable_cards, playable_cards)
                if ability == "trash_copper":
                    num, not_playable_cards = trash_a_copper(not_playable_cards)
                    coins += num
                if ability == "remodel":
                    not_playable_cards, playable_cards, discard_pile, buy_pile = remodel(not_playable_cards,
                                                                                         playable_cards, discard_pile,
                                                                                         buy_pile)
                if ability == "draw":
                    not_playable_cards, playable_cards, draw_pile, discard_pile = draw_a_card(not_playable_cards,
                                                                                              playable_cards, draw_pile,
                                                                                              discard_pile)
                if ability == "play_twice":
                    not_playable_cards, playable_cards, discard_pile, buy_pile, draw_pile, play_pile, coins, buys, actions = play_one_card_two_times(
                        not_playable_cards, playable_cards, discard_pile, buy_pile, draw_pile, play_pile, coins, buys,
                        actions)
    actions -= 1
    return players, current_turn, actions, coins, buys, playable_cards, not_playable_cards, discard_pile, draw_pile, play_pile, buy_pile


def determine_coin_value_of_cards_in_hand(coins, not_playable_cards):
    for card in not_playable_cards:
        coins += card.coins_worth
    return coins, not_playable_cards


def get_names_of_players_and_initialize_decks():
    num_players = int(input("How many players today? 2-4"))
    players = [Player(input(f"Player {i + 1}'s name:")) for i in range(num_players)]
    decks = [Deck() for i in range(len(players))]
    return num_players, players, decks


def play_a_game():
    print("Welcome to Dominion!")
    buy_pile = BuyPile()
    num_players, players, decks = get_names_of_players_and_initialize_decks()
    input("Ready to begin? Press enter to start your game.")
    print()
    # decks = [Deck() for i in range(len(players))]
    turns_taken = 0
    turns_per_round = num_players
    current_turn = 0
    while len(buy_pile.buy_pile[-1]):
        hand, draw_pile, discard_pile = decks[current_turn].get_deck()
        print(f"***************             {players[current_turn].player_name}'s turn number {int((turns_taken / num_players))+1}             ***************")
        actions = 1
        coins = 0
        buys = 1
        while len(hand) == 0:
            hand, draw_pile = get_initial_hand(hand, draw_pile)
        print("Your hand: ")
        for card in hand:
            print(f"{card.name}", end="  **  ")
        not_playable_cards, playable_cards = get_playable_and_not_playable_cards_from_hand(hand)
        print()
        print("Entering action phase: ")
        play_pile = []
        while len(playable_cards) > 0:
            if actions > 0:
                players, current_turn, actions, coins, buys, playable_cards, not_playable_cards, discard_pile, draw_pile, play_pile, buy_pile = play_a_card(players, current_turn, actions, coins, buys, playable_cards, not_playable_cards, discard_pile, draw_pile, play_pile, buy_pile)
        print("Entering buy phase: ")
        coins, not_playable_cards = determine_coin_value_of_cards_in_hand(coins, not_playable_cards)
        # cards_bought = []
        while buys > 0:
            buys, coins, cards_bought, buy_pile = buy_a_card(buys, coins, buy_pile)
        for card in cards_bought:
            print("bought card: ", card.name)
            discard_pile.append(card)
        for card in play_pile:
            discard_pile.append(card)
        for card in not_playable_cards:
            discard_pile.append(card)
        hand.clear()
        hand, draw_pile, discard_pile = get_new_hand(draw_pile, discard_pile)
        decks[current_turn].set_deck([hand, draw_pile, discard_pile])
        print("\n\n\n\n\n\n")
        turns_taken += 1
        current_turn += 1
        if current_turn == turns_per_round:
            current_turn = 0
    determine_winner_and_print_results(players, decks)


play_a_game()

