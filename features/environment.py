


def after_scenario(context, feature):
    if 'delete-board' in feature.tags:
        context.board.delete_board()
        print("board deleted")