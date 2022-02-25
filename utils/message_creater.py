def create_single_text_message(message):
    message_length = 0
    productId = ""
    emojiId = ""

    if message == 'ありがとう':
        message = 'どういたしまして！'
    elif message == 'おはよう':
        message = 'おはよう！\n朝ごはんは目玉焼きだよ'
        message_length = len(message)
        message += '$'
        productId = "5ac1de17040ab15980c9b438"
        emojiId = "001"
    elif message == '疲れた':
        message = 'お疲れさま！がんばったね～\n今日はゆっくり休んでね'
        message_length = len(message)
        message += '$'
        productId = "5ac223c6040ab15980c9b44a"
        emojiId = "137"
    elif message == 'メリークリスマス！':
        message = 'メリークリスマス！'
        message_length = len(message)
        message += '$'
        productId = "5ac223c6040ab15980c9b44a"
        emojiId = "116"
    return create_message(message, message_length, productId, emojiId)


def create_message(message, index, productId, emojiId):
    if index == 0:
        test_message = [{
                        'type': 'text',
                        'text': message
                    }]
    else:
        test_message = [{
                        'type': 'text',
                        'text': message,
                        "emojis": [
                            {
                                "index": index,
                                "productId": productId,
                                "emojiId": emojiId
                            }
                        ]
                    }]
    return test_message